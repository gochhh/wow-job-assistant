"""Source adapters for searching public job listings.

Portal-specific HTTP and parsing stay behind this interface. Search orchestration,
candidate matching, persistence, and Telegram presentation can then use the same
normalized JobOffer model for every source.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Protocol

from career_features import JobOffer, enrich_pracuj_offer, fetch_pracuj_jobs


class JobSource(Protocol):
    """Contract implemented by each job-board connector."""

    source_id: str
    display_name: str
    country_code: str
    content_language: str
    search_locale: str
    country_name: str

    def search_page(
        self, query: str, location: str | None = None, page: int = 1
    ) -> list[JobOffer]: ...

    def enrich(self, offer: JobOffer) -> JobOffer: ...


class PracujPlSource:
    """Pracuj.pl adapter; legacy scraper/parser functions remain its implementation."""

    source_id = "pracuj_pl"
    display_name = "Pracuj.pl"
    country_code = "PL"
    content_language = "pl"
    search_locale = "pl-PL"
    country_name = "Poland"

    def search_page(
        self, query: str, location: str | None = None, page: int = 1
    ) -> list[JobOffer]:
        fetched_at = datetime.now(timezone.utc).isoformat()
        offers = fetch_pracuj_jobs(query, location, page)
        return [
            offer.model_copy(update={
                "source_id": self.source_id,
                "source": self.display_name,
                "country_code": self.country_code,
                "language_code": self.content_language,
                "fetched_at": fetched_at,
            })
            for offer in offers
        ]

    def enrich(self, offer: JobOffer) -> JobOffer:
        return enrich_pracuj_offer(offer)


_SOURCES: dict[str, JobSource] = {
    PracujPlSource.source_id: PracujPlSource(),
}


def get_job_source(source_id: str) -> JobSource:
    """Return a configured source adapter or fail clearly for an unknown ID."""
    try:
        return _SOURCES[source_id]
    except KeyError as exc:
        raise ValueError(f"Unsupported job source: {source_id}") from exc


def available_job_sources() -> tuple[JobSource, ...]:
    """List configured sources for future source selection in the bot UI."""
    return tuple(_SOURCES.values())
