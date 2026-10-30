from __future__ import annotations

from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

_ALLOWED_HOST = "pracuj.pl"
_MAX_PAGE_BYTES = 5_000_000


def _allowed_host(host: str | None) -> bool:
    return bool(host and (host == _ALLOWED_HOST or host.endswith("." + _ALLOWED_HOST)))


class _SameSiteRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new = urlsplit(newurl)
        if new.scheme != "https" or not _allowed_host(new.hostname):
            return None
        return super().redirect_request(req, fp, code, msg, headers, newurl)


class _FormFields(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.fields: list[dict[str, str]] = []
        self.labels: dict[str, str] = {}
        self.application_links: list[str] = []
        self._form_depth = 0
        self._label_for: str | None = None
        self._label_parts: list[str] = []
        self._inside_label = False
        self._anchor_href: str | None = None
        self._anchor_text: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        attrs = {key.lower(): value or "" for key, value in attrs}
        if tag == "form":
            self._form_depth += 1
        if tag == "a":
            self._anchor_href = attrs.get("href") or None
            self._anchor_text = []
        if tag == "label":
            self._label_for = attrs.get("for") or None
            self._label_parts = []
            self._inside_label = True
        if tag in ("input", "textarea", "select") and self._form_depth:
            field_type = (attrs.get("type") or "text").lower()
            if tag == "input" and field_type in {"hidden", "submit", "button", "reset", "image"}:
                return
            identity = attrs.get("id", "")
            name = attrs.get("name", "")
            placeholder = attrs.get("placeholder", "")
            aria = attrs.get("aria-label", "")
            field_hint = (identity + " " + name + " " + placeholder + " " + aria).lower()
            if any(mark in field_hint for mark in ("captcha", "recaptcha", "csrf", "token", "cookie")):
                return
            self.fields.append({"id": identity, "name": name, "placeholder": placeholder, "aria": aria, "inline": ""})

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._anchor_href:
            text = " ".join("".join(self._anchor_text).split()).casefold()
            href = self._anchor_href.casefold()
            if any(term in (text + " " + href) for term in ("aplikuj", "apply", "application", "aplikacja", "aplikację", "aplikowanie", "złóż")):
                self.application_links.append(self._anchor_href)
            self._anchor_href = None
            self._anchor_text = []
        if tag == "form" and self._form_depth:
            self._form_depth -= 1
        if tag == "label" and self._inside_label:
            text = " ".join("".join(self._label_parts).split())
            if self._label_for and text:
                self.labels[self._label_for] = text
            elif text:
                for field in reversed(self.fields):
                    if not field["inline"]:
                        field["inline"] = text
                        break
            self._label_for = None
            self._inside_label = False
            self._label_parts = []

    def handle_data(self, data: str) -> None:
        if self._inside_label:
            self._label_parts.append(data)
        if self._anchor_href:
            self._anchor_text.append(data)


def _fetch_page(url: str) -> tuple[str | None, str]:
    parsed = urlsplit(url)
    if parsed.scheme != "https" or not _allowed_host(parsed.hostname):
        return None, "external"
    request = Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; WOWJobAssistant/1.0)",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "pl-PL,pl;q=0.9,en;q=0.7",
    })
    try:
        with build_opener(_SameSiteRedirects()).open(request, timeout=15) as response:
            if not _allowed_host(urlsplit(response.geturl()).hostname):
                return None, "external"
            markup = response.read(_MAX_PAGE_BYTES + 1)
            if len(markup) > _MAX_PAGE_BYTES:
                return None, "too_large"
            charset = response.headers.get_content_charset() or "utf-8"
            return markup.decode(charset, errors="replace"), "ok"
    except HTTPError as exc:
        return None, "login_or_unavailable" if exc.code in (401, 403, 404) else "unavailable"
    except (URLError, TimeoutError, OSError, ValueError):
        return None, "unavailable"


def _parse_fields(markup: str) -> _FormFields | None:
    parser = _FormFields()
    try:
        parser.feed(markup)
    except Exception:
        return None
    return parser


def _field_labels(parser: _FormFields) -> list[str]:
    fields: list[str] = []
    seen: set[str] = set()
    for item in parser.fields:
        label = parser.labels.get(item["id"], "") or item["inline"] or item["aria"] or item["placeholder"] or item["name"]
        label = " ".join(label.split())
        if label and label.casefold() not in seen:
            seen.add(label.casefold())
            fields.append(label)
    return fields


def inspect_pracuj_application_form(url: str) -> tuple[list[str], str]:
    """Read public Pracuj.pl application fields without submitting data or following off-site links."""
    markup, status = _fetch_page(url)
    if markup is None:
        return [], status
    parser = _parse_fields(markup)
    if parser is None:
        return [], "unavailable"
    fields = _field_labels(parser)
    if fields:
        return fields, "ok"
    for href in parser.application_links[:5]:
        target = urljoin(url, href)
        target_parts = urlsplit(target)
        if target_parts.scheme != "https" or not _allowed_host(target_parts.hostname):
            return [], "external"
        form_markup, form_status = _fetch_page(target)
        if form_markup is None:
            if form_status in {"login_or_unavailable", "external"}:
                return [], form_status
            continue
        form_parser = _parse_fields(form_markup)
        if form_parser is None:
            continue
        fields = _field_labels(form_parser)
        if fields:
            return fields, "ok"
    return [], "dynamic_or_login"
