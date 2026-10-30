"""Telegram UI language preference and localized bot navigation."""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
SETTINGS_FILE = BASE_DIR / "data" / "bot_settings.json"
SUPPORTED_LANGUAGES = ("pl", "en", "ru", "uk", "es", "fr", "de")
LANGUAGE_NAMES = {
    "pl": "Polski", "en": "English", "ru": "Русский", "uk": "Українська",
    "es": "Español", "fr": "Français", "de": "Deutsch",
}

# Stable action IDs let button routing stay independent of the selected language.
MENU_ACTIONS = (
    "profile", "search_jobs", "selected_jobs", "prepare_applications",
    "bot_language", "help", "cancel",
)
MENU_LABELS = {
    "pl": ("👤 Mój profil", "🔎 Szukaj ofert", "⭐ Wybrane oferty", "📨 Przygotuj aplikacje", "🗣️ Język bota", "ℹ️ Informacje", "✖️ Anuluj operację"),
    "en": ("👤 My profile", "🔎 Search jobs", "⭐ Selected jobs", "📨 Prepare applications", "🗣️ Bot language", "ℹ️ About", "✖️ Cancel operation"),
    "ru": ("👤 Мой профиль", "🔎 Искать вакансии", "⭐ Избранные вакансии", "📨 Подготовить заявки", "🗣️ Язык бота", "ℹ️ О боте", "✖️ Отменить операцию"),
    "uk": ("👤 Мій профіль", "🔎 Шукати вакансії", "⭐ Обрані вакансії", "📨 Підготувати заявки", "🗣️ Мова бота", "ℹ️ Про бота", "✖️ Скасувати операцію"),
    "es": ("👤 Mi perfil", "🔎 Buscar ofertas", "⭐ Ofertas seleccionadas", "📨 Preparar solicitudes", "🗣️ Idioma del bot", "ℹ️ Información", "✖️ Cancelar operación"),
    "fr": ("👤 Mon profil", "🔎 Rechercher des offres", "⭐ Offres sélectionnées", "📨 Préparer les candidatures", "🗣️ Langue du bot", "ℹ️ À propos", "✖️ Annuler l’opération"),
    "de": ("👤 Mein Profil", "🔎 Stellen suchen", "⭐ Ausgewählte Stellen", "📨 Bewerbungen vorbereiten", "🗣️ Bot-Sprache", "ℹ️ Informationen", "✖️ Vorgang abbrechen"),
}
MENU_ROW_LAYOUT = ((0,), (1, 2), (3, 4), (5, 6))

PROFILE_ACTION_LABELS = {
    "pl": {"complete":"✍️ Uzupełnij profil","manage":"📚 Zarządzaj CV","language":"🌐 Język profilu","delete":"🗑️ Usuń aktywny profil","back_main":"🔙 Menu główne","back_profile":"🔙 Wróć do profilu"},
    "en": {"complete":"✍️ Complete profile","manage":"📚 Manage CVs","language":"🌐 Profile language","delete":"🗑️ Delete active profile","back_main":"🔙 Main menu","back_profile":"🔙 Back to profile"},
    "ru": {"complete":"✍️ Дополнить профиль","manage":"📚 Управление CV","language":"🌐 Язык профиля","delete":"🗑️ Удалить активный профиль","back_main":"🔙 Главное меню","back_profile":"🔙 Назад к профилю"},
    "uk": {"complete":"✍️ Доповнити профіль","manage":"📚 Керувати CV","language":"🌐 Мова профілю","delete":"🗑️ Видалити активний профіль","back_main":"🔙 Головне меню","back_profile":"🔙 Назад до профілю"},
    "es": {"complete":"✍️ Completar perfil","manage":"📚 Gestionar CV","language":"🌐 Idioma del perfil","delete":"🗑️ Eliminar perfil activo","back_main":"🔙 Menú principal","back_profile":"🔙 Volver al perfil"},
    "fr": {"complete":"✍️ Compléter le profil","manage":"📚 Gérer les CV","language":"🌐 Langue du profil","delete":"🗑️ Supprimer le profil actif","back_main":"🔙 Menu principal","back_profile":"🔙 Retour au profil"},
    "de": {"complete":"✍️ Profil ergänzen","manage":"📚 Lebensläufe verwalten","language":"🌐 Profilsprache","delete":"🗑️ Aktives Profil löschen","back_main":"🔙 Hauptmenü","back_profile":"🔙 Zurück zum Profil"},
}
PROFILE_EMPTY_TEXT = {
    "pl":"Nie ma zapisanego profilu. Wyślij CV w tym czacie; zapytam, czy przygotować z niego profil.",
    "en":"No profile is saved yet. Send a CV in this chat and I’ll ask whether to create a profile from it.",
    "ru":"Сохранённого профиля пока нет. Отправьте CV в этот чат — я спрошу, создать ли по нему профиль.",
    "uk":"Збереженого профілю ще немає. Надішліть CV у цей чат — я запитаю, чи створити з нього профіль.",
    "es":"Aún no hay un perfil guardado. Envía un CV en este chat y te preguntaré si quieres crear un perfil.",
    "fr":"Aucun profil n’est encore enregistré. Envoyez un CV dans ce chat et je vous demanderai si vous souhaitez créer un profil.",
    "de":"Es ist noch kein Profil gespeichert. Sende einen Lebenslauf in diesem Chat; ich frage dich, ob ich daraus ein Profil erstellen soll.",
}
INFO_TEXT = {
    "pl":"WOW Job Assistant pomaga utworzyć i uzupełniać profil na podstawie CV, wyszukiwać i oceniać pasujące oferty Pracuj.pl oraz przygotowywać treści aplikacji do samodzielnego wysłania. CV analizuję dopiero po Twojej zgodzie; aplikacji nie wysyłam za Ciebie.",
    "en":"WOW Job Assistant helps build and update a profile from your CV, find and assess matching Pracuj.pl jobs, and prepare application text for you to submit. Your CV is analyzed only after your consent; the bot does not submit applications for you.",
    "ru":"WOW Job Assistant помогает создать и дополнить профиль по CV, искать и оценивать подходящие вакансии на Pracuj.pl и готовить тексты заявок для самостоятельной отправки. CV анализируется только с вашего согласия; бот не отправляет заявки за вас.",
    "uk":"WOW Job Assistant допомагає створити й доповнити профіль за CV, шукати та оцінювати відповідні вакансії на Pracuj.pl і готувати текст заявки для самостійного надсилання. CV аналізується лише за вашою згодою; бот не надсилає заявки замість вас.",
    "es":"WOW Job Assistant ayuda a crear y completar un perfil a partir de tu CV, buscar y evaluar ofertas adecuadas en Pracuj.pl y preparar textos de solicitud para que los envíes. El CV se analiza solo con tu consentimiento; el bot no envía solicitudes por ti.",
    "fr":"WOW Job Assistant aide à créer et compléter un profil à partir de votre CV, à rechercher et évaluer les offres adaptées sur Pracuj.pl et à préparer le texte des candidatures que vous enverrez. Le CV n’est analysé qu’avec votre accord ; le bot n’envoie pas les candidatures à votre place.",
    "de":"WOW Job Assistant hilft dir, anhand deines Lebenslaufs ein Profil zu erstellen und zu ergänzen, passende Stellen auf Pracuj.pl zu finden und zu bewerten sowie Bewerbungstexte vorzubereiten. Dein Lebenslauf wird nur mit deiner Zustimmung analysiert; der Bot versendet keine Bewerbungen für dich.",
}
START_TEXT = {
    "pl": "Bot WOW Job Assistant działa. Wybierz funkcję z menu poniżej albo wyślij CV jako PDF, DOCX lub TXT (maks. 15 MB). Wybrane aplikacje sprawdzę i przygotuję do ręcznego wysłania — bot nie wysyła ich za Ciebie.",
    "en": "WOW Job Assistant is running. Choose an option below or send a CV as PDF, DOCX or TXT (max 15 MB). I can review selected applications and prepare them for you to send; the bot will not submit them for you.",
    "ru": "Бот WOW Job Assistant работает. Выберите функцию в меню или отправьте CV в формате PDF, DOCX или TXT (до 15 МБ). Я проверю выбранные заявки и подготовлю их для отправки вручную — бот не отправляет их за вас.",
    "uk": "Бот WOW Job Assistant працює. Виберіть функцію в меню або надішліть CV у форматі PDF, DOCX чи TXT (до 15 МБ). Я перевірю вибрані заявки та підготую їх для ручного надсилання — бот не надсилає їх за вас.",
    "es": "WOW Job Assistant está en funcionamiento. Elige una opción del menú o envía un CV en PDF, DOCX o TXT (máx. 15 MB). Revisaré las solicitudes seleccionadas y las prepararé para que las envíes; el bot no las enviará por ti.",
    "fr": "WOW Job Assistant est en marche. Choisissez une option dans le menu ou envoyez un CV en PDF, DOCX ou TXT (15 Mo max.). Je peux vérifier et préparer les candidatures sélectionnées pour que vous les envoyiez vous-même.",
    "de": "WOW Job Assistant läuft. Wähle eine Funktion im Menü oder sende einen Lebenslauf als PDF, DOCX oder TXT (max. 15 MB). Ich prüfe ausgewählte Bewerbungen und bereite sie zum manuellen Versand vor; der Bot versendet sie nicht für dich.",
}
LANGUAGE_PROMPT = {
    "pl": "Wybierz język interfejsu bota. Możesz wrócić do języka Telegrama:",
    "en": "Choose the bot interface language. You can switch back to Telegram's language:",
    "ru": "Выберите язык интерфейса бота. Можно вернуться к языку Telegram:",
    "uk": "Виберіть мову інтерфейсу бота. Можна повернутися до мови Telegram:",
    "es": "Elige el idioma de la interfaz del bot. Puedes volver al idioma de Telegram:",
    "fr": "Choisissez la langue de l’interface du bot. Vous pouvez revenir à la langue de Telegram :",
    "de": "Wähle die Sprache der Bot-Oberfläche. Du kannst zur Telegram-Sprache zurückkehren:",
}
AUTO_LANGUAGE_LABEL = {
    "pl": "Automatycznie (język Telegrama)", "en": "Automatic (Telegram language)",
    "ru": "Автоматически (язык Telegram)", "uk": "Автоматично (мова Telegram)",
    "es": "Automático (idioma de Telegram)", "fr": "Automatique (langue de Telegram)",
    "de": "Automatisch (Telegram-Sprache)",
}
LANGUAGE_SET_TEXT = {
    "pl": "Zapisano język interfejsu: {name}.", "en": "Interface language saved: {name}.",
    "ru": "Язык интерфейса сохранён: {name}.", "uk": "Мову інтерфейсу збережено: {name}.",
    "es": "Idioma de la interfaz guardado: {name}.", "fr": "Langue de l’interface enregistrée : {name}.",
    "de": "Oberflächensprache gespeichert: {name}.",
}
LANGUAGE_AUTO_TEXT = {
    "pl": "Włączono automatyczny wybór języka na podstawie ustawienia Telegrama: {name}.",
    "en": "Automatic language selection from Telegram is enabled: {name}.",
    "ru": "Включен автоматический выбор языка по настройке Telegram: {name}.",
    "uk": "Увімкнено автоматичний вибір мови за налаштуванням Telegram: {name}.",
    "es": "Se activó la selección automática según Telegram: {name}.",
    "fr": "La sélection automatique selon Telegram est activée : {name}.",
    "de": "Automatische Sprachauswahl nach Telegram ist aktiviert: {name}.",
}


def normalize_language(language: str | None) -> str:
    code = (language or "").strip().lower().replace("_", "-").split("-", 1)[0]
    return code if code in SUPPORTED_LANGUAGES else "en"


def _read_settings() -> dict[str, Any]:
    try:
        value = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def language_for_user(user: object | None) -> str:
    if user is None:
        return "en"
    user_id = getattr(user, "id", None)
    settings = _read_settings()
    users = settings.get("users", {})
    preference = users.get(str(user_id), {}) if isinstance(users, dict) else {}
    manual = preference.get("language") if isinstance(preference, dict) else None
    if manual in SUPPORTED_LANGUAGES:
        return manual
    return normalize_language(getattr(user, "language_code", None))


def set_user_language(user_id: int, language: str | None) -> None:
    settings = _read_settings()
    users = settings.setdefault("users", {})
    key = str(user_id)
    if language is None:
        users.pop(key, None)
    elif language in SUPPORTED_LANGUAGES:
        users[key] = {"language": language}
    SETTINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    temporary = SETTINGS_FILE.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(settings, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(temporary, SETTINGS_FILE)


# User-facing Polish phrases are the canonical source strings in the existing bot.
# Keep generated profile/job/form content intact, translating only known interface copy.
UI_PHRASES = {
    "Ten bot jest prywatny.": {"en":"This bot is private.","ru":"Этот бот закрытый.","uk":"Цей бот приватний.","es":"Este bot es privado.","fr":"Ce bot est privé.","de":"Dieser Bot ist privat."},
    "Nie rozpoznałem tego przycisku. Użyj /start, aby odświeżyć menu.": {"en":"I don't recognize this button. Use /start to refresh the menu.","ru":"Не удалось распознать эту кнопку. Используйте /start, чтобы обновить меню.","uk":"Не вдалося розпізнати цю кнопку. Використайте /start, щоб оновити меню.","es":"No reconozco este botón. Usa /start para actualizar el menú.","fr":"Je ne reconnais pas ce bouton. Utilisez /start pour actualiser le menu.","de":"Diese Schaltfläche ist unbekannt. Verwende /start, um das Menü zu aktualisieren."},
    "Wybierz język profilu:": {"en":"Choose the profile language:","ru":"Выберите язык профиля:","uk":"Виберіть мову профілю:","es":"Elige el idioma del perfil:","fr":"Choisissez la langue du profil :","de":"Profilsprache auswählen:"},
    "Wyślij w tym czacie plik PDF, DOCX lub TXT.": {"en":"Send a PDF, DOCX or TXT file in this chat.","ru":"Отправьте в этот чат файл PDF, DOCX или TXT.","uk":"Надішліть у цей чат файл PDF, DOCX або TXT.","es":"Envía aquí un archivo PDF, DOCX o TXT.","fr":"Envoyez ici un fichier PDF, DOCX ou TXT.","de":"Sende eine PDF-, DOCX- oder TXT-Datei in diesen Chat."},
    "Twój Telegram ID: ": {"en":"Your Telegram ID: ","ru":"Ваш Telegram ID: ","uk":"Ваш Telegram ID: ","es":"Tu ID de Telegram: ","fr":"Votre identifiant Telegram : ","de":"Deine Telegram-ID: "},
    "Obsługuję pliki PDF, DOCX lub TXT.": {"en":"Supported files: PDF, DOCX or TXT.","ru":"Поддерживаются файлы PDF, DOCX или TXT.","uk":"Підтримуються файли PDF, DOCX або TXT.","es":"Se admiten archivos PDF, DOCX o TXT.","fr":"Formats acceptés : PDF, DOCX ou TXT.","de":"Unterstützte Dateien: PDF, DOCX oder TXT."},
    "Plik jest za duży. Limit tej wersji to 15 MB.": {"en":"The file is too large. The limit for this version is 15 MB.","ru":"Файл слишком большой. Ограничение этой версии — 15 МБ.","uk":"Файл завеликий. Обмеження цієї версії — 15 МБ.","es":"El archivo es demasiado grande. El límite es 15 MB.","fr":"Le fichier est trop volumineux. La limite est de 15 Mo.","de":"Die Datei ist zu groß. Das Limit beträgt 15 MB."},
    "Odebrałem CV. Pobieram plik z Telegrama i zapisuję go lokalnie…": {"en":"CV received. Downloading it from Telegram and saving it locally…","ru":"Резюме получено. Скачиваю его из Telegram и сохраняю локально…","uk":"Резюме отримано. Завантажую його з Telegram і зберігаю локально…","es":"CV recibido. Descargando desde Telegram y guardándolo localmente…","fr":"CV reçu. Téléchargement depuis Telegram et enregistrement local…","de":"Lebenslauf erhalten. Wird von Telegram heruntergeladen und lokal gespeichert…"},
    "Nie udało się pobrać pliku. Spróbuj wysłać go ponownie.": {"en":"Couldn't download the file. Please send it again.","ru":"Не удалось скачать файл. Попробуйте отправить его ещё раз.","uk":"Не вдалося завантажити файл. Спробуйте надіслати його ще раз.","es":"No se pudo descargar el archivo. Inténtalo de nuevo.","fr":"Impossible de télécharger le fichier. Réessayez.","de":"Die Datei konnte nicht heruntergeladen werden. Bitte erneut senden."},
    "CV zapisane lokalnie. Jeśli klikniesz „Tak”, wyodrębnię tekst i przekażę go do OpenAI API, aby przygotować roboczy profil. Profil pokażę Ci do sprawdzenia; zapiszę go jako profil kandydata dopiero po Twoim zatwierdzeniu. Nie klikaj zgody, jeśli nie chcesz wysyłać treści CV do OpenAI. Analiza zużywa kredyty API.": {"en":"CV saved locally. If you choose “Yes”, I'll extract its text and send it to the OpenAI API to prepare a draft profile. I'll show it for your review and save it only after your approval. Don't consent if you don't want the CV sent to OpenAI. Analysis and translations use API credits.","ru":"Резюме сохранено локально. Если нажать «Да», я извлеку текст и отправлю его в OpenAI API для подготовки черновика профиля. Сначала покажу его вам и сохраню только после подтверждения. Не соглашайтесь, если не хотите передавать CV в OpenAI. Анализ и переводы расходуют кредиты API.","uk":"Резюме збережено локально. Якщо натиснути «Так», я витягну текст і надішлю його до OpenAI API, щоб підготувати чернетку профілю. Спочатку покажу її вам і збережу лише після підтвердження. Не погоджуйтеся, якщо не хочете передавати CV до OpenAI. Аналіз і переклади використовують кредити API.","es":"CV guardado localmente. Si eliges «Sí», extraeré el texto y lo enviaré a la API de OpenAI para preparar un borrador del perfil. Te lo mostraré y solo lo guardaré tras tu aprobación. No aceptes si no quieres enviar el CV a OpenAI. El análisis y las traducciones consumen créditos de API.","fr":"CV enregistré localement. Si vous choisissez « Oui », j’extrairai le texte et l’enverrai à l’API OpenAI pour préparer un brouillon du profil. Je vous le montrerai et ne l’enregistrerai qu’après votre validation. Ne donnez pas votre accord si vous ne souhaitez pas envoyer le CV à OpenAI. L’analyse et les traductions utilisent des crédits API.","de":"Lebenslauf lokal gespeichert. Wenn du „Ja“ wählst, extrahiere ich den Text und sende ihn an die OpenAI-API, um einen Profilentwurf zu erstellen. Ich zeige ihn dir und speichere ihn erst nach deiner Freigabe. Stimme nicht zu, wenn du den Lebenslauf nicht an OpenAI senden möchtest. Analyse und Übersetzungen verbrauchen API-Guthaben."},
    "Nie mam zapisanego CV. Prześlij plik PDF, DOCX lub TXT.": {"en":"No saved CV found. Send a PDF, DOCX or TXT file.","ru":"Сохранённое резюме не найдено. Отправьте файл PDF, DOCX или TXT.","uk":"Збережене резюме не знайдено. Надішліть файл PDF, DOCX або TXT.","es":"No hay ningún CV guardado. Envía un archivo PDF, DOCX o TXT.","fr":"Aucun CV enregistré. Envoyez un fichier PDF, DOCX ou TXT.","de":"Kein gespeicherter Lebenslauf gefunden. Sende eine PDF-, DOCX- oder TXT-Datei."},
    "Nie mam zatwierdzonego profilu. Wyślij CV i użyj /analyze.": {"en":"There is no approved profile yet. Send a CV and use /analyze.","ru":"Подтверждённого профиля пока нет. Отправьте CV и используйте /analyze.","uk":"Підтвердженого профілю ще немає. Надішліть CV і скористайтеся /analyze.","es":"Aún no hay un perfil aprobado. Envía un CV y usa /analyze.","fr":"Aucun profil n’a encore été validé. Envoyez un CV et utilisez /analyze.","de":"Es gibt noch kein freigegebenes Profil. Sende einen Lebenslauf und verwende /analyze."},
    "Nie ma jeszcze zapisanego profilu. Wyślij CV i zatwierdź jego analizę.": {"en":"No profile has been saved yet. Send a CV and approve its analysis.","ru":"Профиль ещё не сохранён. Отправьте CV и подтвердите его анализ.","uk":"Профіль ще не збережено. Надішліть CV і підтвердьте його аналіз.","es":"Aún no se ha guardado ningún perfil. Envía un CV y aprueba su análisis.","fr":"Aucun profil n’a encore été enregistré. Envoyez un CV et validez son analyse.","de":"Es wurde noch kein Profil gespeichert. Sende einen Lebenslauf und bestätige die Analyse."},
    "Zapisane profile. Wybierz CV, którego profil ma być aktywny:": {"en":"Saved profiles. Choose the CV profile to activate:","ru":"Сохранённые профили. Выберите профиль CV для активации:","uk":"Збережені профілі. Виберіть профіль CV для активації:","es":"Perfiles guardados. Elige el perfil CV que quieres activar:","fr":"Profils enregistrés. Choisissez le profil CV à activer :","de":"Gespeicherte Profile. Wähle das zu aktivierende Lebenslaufprofil:"},
    "Nie ma aktywnego profilu do usunięcia.": {"en":"There is no active profile to delete.","ru":"Нет активного профиля для удаления.","uk":"Немає активного профілю для видалення.","es":"No hay ningún perfil activo que eliminar.","fr":"Aucun profil actif à supprimer.","de":"Es gibt kein aktives Profil zum Löschen."},
    "Obsługiwane języki: pl, en, ru, uk.": {"en":"Supported profile languages: pl, en, ru, uk.","ru":"Поддерживаемые языки профиля: pl, en, ru, uk.","uk":"Підтримувані мови профілю: pl, en, ru, uk.","es":"Idiomas de perfil compatibles: pl, en, ru, uk.","fr":"Langues de profil prises en charge : pl, en, ru, uk.","de":"Unterstützte Profilsprache: pl, en, ru, uk."},
    "Najpierw zapisz profil poleceniem /analyze.": {"en":"First create a profile with /analyze.","ru":"Сначала создайте профиль командой /analyze.","uk":"Спочатку створіть профіль командою /analyze.","es":"Primero crea un perfil con /analyze.","fr":"Créez d’abord un profil avec /analyze.","de":"Erstelle zuerst mit /analyze ein Profil."},
    "Nie udało się przetłumaczyć profilu. Oryginalna wersja pozostała bez zmian.": {"en":"Couldn't translate the profile. The original version remains unchanged.","ru":"Не удалось перевести профиль. Исходная версия не изменена.","uk":"Не вдалося перекласти профіль. Початкова версія не змінилася.","es":"No se pudo traducir el perfil. La versión original no ha cambiado.","fr":"Impossible de traduire le profil. La version originale reste inchangée.","de":"Das Profil konnte nicht übersetzt werden. Die Originalversion bleibt unverändert."},
    "Nie udało się znaleźć ofert na tej stronie albo Pracuj.pl zablokował automatyczny odczyt. Spróbuj innego zapytania później.": {"en":"No jobs were found on this page, or Pracuj.pl blocked automatic access. Try another query later.","ru":"На этой странице вакансии не найдены или Pracuj.pl заблокировал автоматическое чтение. Попробуйте другой запрос позже.","uk":"На цій сторінці вакансії не знайдено або Pracuj.pl заблокував автоматичне читання. Спробуйте інший запит пізніше.","es":"No se encontraron ofertas en esta página o Pracuj.pl bloqueó el acceso automático. Prueba otra búsqueda más tarde.","fr":"Aucune offre trouvée sur cette page ou Pracuj.pl a bloqué l’accès automatique. Réessayez plus tard avec une autre recherche.","de":"Auf dieser Seite wurden keine Stellen gefunden oder Pracuj.pl hat den automatischen Zugriff blockiert. Versuche später eine andere Suche."},
    "Nie ma już ofert na tej stronie wyników.": {"en":"There are no more jobs on this results page.","ru":"На этой странице больше нет вакансий.","uk":"На цій сторінці більше немає вакансій.","es":"No hay más ofertas en esta página de resultados.","fr":"Il n’y a plus d’offres sur cette page de résultats.","de":"Auf dieser Ergebnisseite gibt es keine weiteren Stellen."},
    "Dopasowanie: ": {"en":"Match: ","ru":"Соответствие: ","uk":"Відповідність: ","es":"Coincidencia: ","fr":"Correspondance : ","de":"Passung: "},
    "Wersja profilu użyta do oceny: ": {"en":"Profile version used for assessment: ","ru":"Версия профиля для оценки: ","uk":"Версія профілю для оцінювання: ","es":"Versión del perfil usada para la evaluación: ","fr":"Version du profil utilisée pour l’évaluation : ","de":"Für die Bewertung verwendete Profilversion: "},
    "Pasuje: ": {"en":"Matches: ","ru":"Совпадения: ","uk":"Збіги: ","es":"Coincidencias: ","fr":"Correspondances : ","de":"Passende Punkte: "},
    "Braki: ": {"en":"Gaps: ","ru":"Пробелы: ","uk":"Прогалини: ","es":"Brechas: ","fr":"Écarts : ","de":"Lücken: "},
    "brak potwierdzonych dopasowań": {"en":"no confirmed matches","ru":"нет подтверждённых совпадений","uk":"немає підтверджених збігів","es":"sin coincidencias confirmadas","fr":"aucune correspondance confirmée","de":"keine bestätigten Übereinstimmungen"},
    "brak wskazanych luk": {"en":"no identified gaps","ru":"пробелы не выявлены","uk":"прогалин не виявлено","es":"sin brechas identificadas","fr":"aucun écart identifié","de":"keine erkannten Lücken"},
    "Firma niepodana": {"en":"Company not specified","ru":"Компания не указана","uk":"Компанію не вказано","es":"Empresa no especificada","fr":"Entreprise non précisée","de":"Unternehmen nicht angegeben"},
    "Lokalizacja niepodana": {"en":"Location not specified","ru":"Местоположение не указано","uk":"Місце не вказано","es":"Ubicación no especificada","fr":"Lieu non précisé","de":"Standort nicht angegeben"},
    "Oferta": {"en":"Job","ru":"Вакансия","uk":"Вакансія","es":"Oferta","fr":"Offre","de":"Stelle"},
    "Usuń z wybranych": {"en":"Remove from selected","ru":"Убрать из выбранных","uk":"Вилучити з обраних","es":"Quitar de seleccionadas","fr":"Retirer de la sélection","de":"Aus Auswahl entfernen"},
    "Wybieram tę ofertę": {"en":"Select this job","ru":"Выбрать вакансию","uk":"Обрати вакансію","es":"Elegir esta oferta","fr":"Choisir cette offre","de":"Diese Stelle auswählen"},
    "Następne oferty": {"en":"More jobs","ru":"Следующие вакансии","uk":"Наступні вакансії","es":"Más ofertas","fr":"Offres suivantes","de":"Weitere Stellen"},
    "Następna strona Pracuj.pl": {"en":"Next Pracuj.pl page","ru":"Следующая страница Pracuj.pl","uk":"Наступна сторінка Pracuj.pl","es":"Página siguiente de Pracuj.pl","fr":"Page suivante de Pracuj.pl","de":"Nächste Pracuj.pl-Seite"},
    "Najpierw zapisz aktywny profil poleceniem /analyze.": {"en":"First create an active profile with /analyze.","ru":"Сначала создайте активный профиль командой /analyze.","uk":"Спочатку створіть активний профіль командою /analyze.","es":"Primero crea un perfil activo con /analyze.","fr":"Créez d’abord un profil actif avec /analyze.","de":"Erstelle zuerst mit /analyze ein aktives Profil."},
    "Wyszukiwanie zakończone. Pracuj.pl nie zwrócił ofert dla tych kryteriów.": {"en":"Search finished. Pracuj.pl returned no jobs for these criteria.","ru":"Поиск завершён. Pracuj.pl не нашёл вакансий по этим критериям.","uk":"Пошук завершено. Pracuj.pl не знайшов вакансій за цими критеріями.","es":"Búsqueda terminada. Pracuj.pl no encontró ofertas con estos criterios.","fr":"Recherche terminée. Pracuj.pl n’a trouvé aucune offre pour ces critères.","de":"Suche abgeschlossen. Pracuj.pl hat keine passenden Stellen gefunden."},
    "Nie udało się pobrać lub ocenić ofert. Zakończyłem wyszukiwanie błędem; sprawdź połączenie i spróbuj ponownie.": {"en":"Couldn't retrieve or assess jobs. The search ended with an error; check your connection and try again.","ru":"Не удалось загрузить или оценить вакансии. Поиск завершился ошибкой; проверьте подключение и попробуйте снова.","uk":"Не вдалося завантажити або оцінити вакансії. Пошук завершився помилкою; перевірте з’єднання та спробуйте знову.","es":"No se pudieron obtener o evaluar las ofertas. La búsqueda terminó con un error; comprueba la conexión e inténtalo de nuevo.","fr":"Impossible de récupérer ou d’évaluer les offres. La recherche a échoué ; vérifiez votre connexion et réessayez.","de":"Stellen konnten nicht geladen oder bewertet werden. Die Suche endete mit einem Fehler. Prüfe deine Verbindung und versuche es erneut."},
    "Nie wybrano jeszcze ofert. Użyj /jobs, aby wyszukać i zaznaczyć oferty.": {"en":"No jobs selected yet. Use /jobs to search and select jobs.","ru":"Вакансии ещё не выбраны. Используйте /jobs, чтобы найти и выбрать вакансии.","uk":"Вакансії ще не обрано. Скористайтеся /jobs, щоб знайти й вибрати вакансії.","es":"Aún no has seleccionado ofertas. Usa /jobs para buscarlas y seleccionarlas.","fr":"Aucune offre sélectionnée. Utilisez /jobs pour rechercher et sélectionner des offres.","de":"Noch keine Stellen ausgewählt. Verwende /jobs, um Stellen zu suchen und auszuwählen."},
    "Wybrane oferty:": {"en":"Selected jobs:","ru":"Выбранные вакансии:","uk":"Обрані вакансії:","es":"Ofertas seleccionadas:","fr":"Offres sélectionnées :","de":"Ausgewählte Stellen:"},
    "Nie wybrano ofert. Najpierw zaznacz je w wynikach /jobs.": {"en":"No jobs selected. Select jobs in the /jobs results first.","ru":"Вакансии не выбраны. Сначала отметьте их в результатах /jobs.","uk":"Вакансії не вибрано. Спочатку позначте їх у результатах /jobs.","es":"No hay ofertas seleccionadas. Selecciónalas primero en los resultados de /jobs.","fr":"Aucune offre sélectionnée. Sélectionnez-en d’abord dans les résultats de /jobs.","de":"Keine Stellen ausgewählt. Wähle zuerst Stellen in den /jobs-Ergebnissen aus."},
    "Nie ma aktywnego profilu kandydata. Najpierw przeanalizuj i zatwierdź CV.": {"en":"There is no active candidate profile. Analyze and approve a CV first.","ru":"Нет активного профиля кандидата. Сначала проанализируйте и подтвердите CV.","uk":"Немає активного профілю кандидата. Спочатку проаналізуйте й підтвердьте CV.","es":"No hay un perfil de candidato activo. Primero analiza y aprueba un CV.","fr":"Aucun profil candidat actif. Analysez et validez d’abord un CV.","de":"Kein aktives Kandidatenprofil vorhanden. Analysiere zuerst einen Lebenslauf und bestätige ihn."},
    "Sprawdź przygotowane treści i samodzielnie wyślij aplikacje. Bot nie loguje się na konto i nie wysyła formularzy.": {"en":"Review the prepared content and submit applications yourself. The bot does not sign in or submit forms.","ru":"Проверьте подготовленные тексты и отправьте заявки самостоятельно. Бот не входит в аккаунты и не отправляет формы.","uk":"Перевірте підготовлені тексти й надішліть заявки самостійно. Бот не входить до облікових записів і не надсилає форми.","es":"Revisa el contenido y envía las solicitudes tú mismo. El bot no inicia sesión ni envía formularios.","fr":"Vérifiez les textes préparés et envoyez vous-même les candidatures. Le bot ne se connecte pas et ne soumet aucun formulaire.","de":"Prüfe die vorbereiteten Texte und sende Bewerbungen selbst ab. Der Bot meldet sich nicht an und übermittelt keine Formulare."},
    "Gotowe. Zakończyłem sprawdzanie wybranych formularzy; wysyłam podsumowanie.": {"en":"Done. I finished checking the selected forms; sending the summary.","ru":"Готово. Проверка выбранных форм завершена; отправляю сводку.","uk":"Готово. Перевірку обраних форм завершено; надсилаю підсумок.","es":"Listo. Terminé de revisar los formularios seleccionados; envío el resumen.","fr":"Terminé. La vérification des formulaires sélectionnés est achevée ; envoi du résumé.","de":"Fertig. Die ausgewählten Formulare wurden geprüft; die Zusammenfassung wird gesendet."},
    "Sprawdź dane. Po zatwierdzeniu zapiszę profil lokalnie i przygotuję wersje EN, RU i UK przez OpenAI; te dodatkowe wywołania zużyją kredyty API.": {"en":"Review the details. After approval, I'll save the profile locally and prepare EN, RU and UK versions using OpenAI; these extra calls use API credits.","ru":"Проверьте данные. После подтверждения профиль будет сохранён локально, а версии EN, RU и UK подготовлены через OpenAI за кредиты API.","uk":"Перевірте дані. Після підтвердження профіль буде збережено локально, а версії EN, RU та UK підготовлено через OpenAI за кредити API.","es":"Revisa los datos. Tras aprobarlo, guardaré el perfil localmente y crearé las versiones EN, RU y UK con OpenAI; estas llamadas consumen créditos.","fr":"Vérifiez les informations. Après validation, j’enregistrerai le profil localement et préparerai les versions EN, RU et UK avec OpenAI ; ces appels utilisent des crédits API.","de":"Prüfe die Angaben. Nach deiner Freigabe speichere ich das Profil lokal und erstelle EN-, RU- und UK-Versionen mit OpenAI; diese Aufrufe verbrauchen API-Guthaben."},
    "Zatwierdź i zapisz": {"en":"Approve and save","ru":"Подтвердить и сохранить","uk":"Підтвердити й зберегти","es":"Aprobar y guardar","fr":"Valider et enregistrer","de":"Bestätigen und speichern"},
    "Odrzuć": {"en":"Reject","ru":"Отклонить","uk":"Відхилити","es":"Rechazar","fr":"Refuser","de":"Ablehnen"},
    "Usuń profil": {"en":"Delete profile","ru":"Удалить профиль","uk":"Видалити профіль","es":"Eliminar perfil","fr":"Supprimer le profil","de":"Profil löschen"},
    "Anuluj": {"en":"Cancel","ru":"Отмена","uk":"Скасувати","es":"Cancelar","fr":"Annuler","de":"Abbrechen"},
    "Uzupełnij profil": {"en":"Complete profile","ru":"Дополнить профиль","uk":"Доповнити профіль","es":"Completar perfil","fr":"Compléter le profil","de":"Profil ergänzen"},
    "Usuń aktywny profil": {"en":"Delete active profile","ru":"Удалить активный профиль","uk":"Видалити активний профіль","es":"Eliminar perfil activo","fr":"Supprimer le profil actif","de":"Aktives Profil löschen"},
    "Gotowe. Profil przetłumaczono i zapisano równolegle z pozostałymi wersjami.": {"en":"Done. The profile has been translated and saved alongside the other versions.","ru":"Готово. Профиль переведён и сохранён вместе с остальными версиями.","uk":"Готово. Профіль перекладено та збережено разом з іншими версіями.","es":"Listo. El perfil se tradujo y guardó junto con las demás versiones.","fr":"Terminé. Le profil a été traduit et enregistré avec les autres versions.","de":"Fertig. Das Profil wurde übersetzt und zusammen mit den anderen Versionen gespeichert."},
    "Anulowano. Profil pozostał zapisany.": {"en":"Cancelled. The profile remains saved.","ru":"Отменено. Профиль остался сохранён.","uk":"Скасовано. Профіль залишився збереженим.","es":"Cancelado. El perfil sigue guardado.","fr":"Annulé. Le profil reste enregistré.","de":"Abgebrochen. Das Profil bleibt gespeichert."},
    "Oferta została dodana do wybranych. Zobacz listę przez /selected.": {"en":"Job added to your selection. View the list with /selected.","ru":"Вакансия добавлена в выбранные. Список: /selected.","uk":"Вакансію додано до обраних. Список: /selected.","es":"Oferta añadida a la selección. Consulta la lista con /selected.","fr":"Offre ajoutée à la sélection. Consultez la liste avec /selected.","de":"Stelle zur Auswahl hinzugefügt. Liste mit /selected anzeigen."},
    "Usunięto ofertę z wybranych.": {"en":"Job removed from your selection.","ru":"Вакансия удалена из выбранных.","uk":"Вакансію вилучено з обраних.","es":"Oferta eliminada de la selección.","fr":"Offre retirée de la sélection.","de":"Stelle aus der Auswahl entfernt."},
    "Wyszukiwanie wygasło. Uruchom /jobs ponownie.": {"en":"The search has expired. Run /jobs again.","ru":"Срок действия поиска истёк. Запустите /jobs ещё раз.","uk":"Термін дії пошуку минув. Запустіть /jobs ще раз.","es":"La búsqueda ha caducado. Ejecuta /jobs de nuevo.","fr":"La recherche a expiré. Relancez /jobs.","de":"Die Suche ist abgelaufen. Starte /jobs erneut."},
    "Anulowano oczekującą operację. Zapisany oryginał CV pozostał na komputerze.": {"en":"Pending operation cancelled. The original CV remains saved on this computer.","ru":"Операция отменена. Исходное CV осталось на этом компьютере.","uk":"Операцію скасовано. Початкове CV залишилося на цьому комп’ютері.","es":"Operación cancelada. El CV original sigue guardado en este equipo.","fr":"Opération annulée. Le CV original reste enregistré sur cet ordinateur.","de":"Vorgang abgebrochen. Der ursprüngliche Lebenslauf bleibt auf diesem Computer gespeichert."},
    "Nie udało się dokończyć tej operacji. Bot odebrał polecenie, ale wystąpił błąd; spróbuj ponownie.": {"en":"The operation couldn't be completed. The bot received your request but encountered an error; please try again.","ru":"Не удалось завершить операцию. Бот получил команду, но произошла ошибка; попробуйте ещё раз.","uk":"Не вдалося завершити операцію. Бот отримав команду, але сталася помилка; спробуйте ще раз.","es":"No se pudo completar la operación. El bot recibió la orden, pero ocurrió un error; inténtalo de nuevo.","fr":"Impossible de terminer l’opération. Le bot a reçu la commande, mais une erreur est survenue ; réessayez.","de":"Der Vorgang konnte nicht abgeschlossen werden. Der Bot hat den Auftrag erhalten, aber ein Fehler ist aufgetreten. Bitte versuche es erneut."},
}


def translate_ui_text(text: Any, language: str) -> Any:
    if not isinstance(text, str) or language == "pl":
        return text
    language = normalize_language(language)
    exact = UI_PHRASES.get(text)
    if exact:
        return exact.get(language, text)

    # Translate complete lines or unmistakable UI prefixes/suffixes only. This
    # keeps CV facts, offer titles and other user/source content unchanged.
    lines = text.split("\n")
    sources = sorted(UI_PHRASES, key=len, reverse=True)
    for index, line in enumerate(lines):
        exact_line = UI_PHRASES.get(line)
        if exact_line:
            lines[index] = exact_line.get(language, line)
            continue
        value = line
        for source in sources:
            replacement = UI_PHRASES[source].get(language)
            if not replacement:
                continue
            position = value.find(source)
            if position == 0:
                value = replacement + value[len(source):]
            elif position <= 3 and position > 0 and value[:position].strip() in {"🟢", "🟡", "🔴", "⚪"}:
                value = value[:position] + replacement + value[position + len(source):]
            elif source == " profilu " and line.startswith("Wyświetlam wersję ") and position >= 0:
                value = value[:position] + replacement + value[position + len(source):]
            elif source == " Nadal trwa (" and position > 0:
                value = value[:position] + replacement + value[position + len(source):]
            elif source.startswith((" ", ".", ")")) and len(source) >= 18 and position >= 0:
                value = value[:position] + replacement + value[position + len(source):]
        if line.startswith("Pokazano ") and " z " in value:
            connectors = {"en": " of ", "ru": " из ", "uk": " з ", "es": " de ", "fr": " sur ", "de": " von "}
            value = value.replace(" z ", connectors[language], 1)
        if line.startswith(("Pobrano ", "Gotowe: pobrano ")) and " ofert (" in value:
            units = {"en": " jobs (", "ru": " вакансий (", "uk": " вакансій (", "es": " ofertas (", "fr": " offres (", "de": " Stellen ("}
            value = value.replace(" ofert (", units[language], 1)
        lines[index] = value
    return "\n".join(lines)


_TELEGRAM_LANGUAGES: dict[int, str] = {}


def remember_telegram_language(user_id: int, language_code: str | None) -> None:
    # Store the current language code only in memory: Telegram supplies it on every update.
    _TELEGRAM_LANGUAGES[user_id] = normalize_language(language_code)


def language_for_chat(chat_id: int | str | None) -> str:
    if chat_id is None:
        return "en"
    settings = _read_settings()
    users = settings.get("users", {})
    preference = users.get(str(chat_id), {}) if isinstance(users, dict) else {}
    manual = preference.get("language") if isinstance(preference, dict) else None
    if manual in SUPPORTED_LANGUAGES:
        return manual
    try:
        return _TELEGRAM_LANGUAGES.get(int(chat_id), "en")
    except (TypeError, ValueError):
        return "en"


def localize_markup(markup: Any, language: str) -> Any:
    if markup is None or language == "pl":
        return markup
    data = markup.to_dict() if hasattr(markup, "to_dict") else None
    if not isinstance(data, dict):
        return markup
    for attribute in ("keyboard", "inline_keyboard"):
        rows = data.get(attribute)
        if rows:
            for row in rows:
                for button in row:
                    if isinstance(button, dict) and button.get("text"):
                        button["text"] = translate_ui_text(button["text"], language)
    try:
        return type(markup).de_json(data)
    except (AttributeError, TypeError, ValueError):
        return markup


# Small interface labels also occur inside inline keyboards and composed result messages.
_extra = {
    "Uzupełnij profil": {"en":"Complete profile","ru":"Дополнить профиль","uk":"Доповнити профіль","es":"Completar perfil","fr":"Compléter le profil","de":"Profil ergänzen"},
    "Usuń aktywny profil": {"en":"Delete active profile","ru":"Удалить активный профиль","uk":"Видалити активний профіль","es":"Eliminar perfil activo","fr":"Supprimer le profil actif","de":"Aktives Profil löschen"},
    "Usuń profil": {"en":"Delete profile","ru":"Удалить профиль","uk":"Видалити профіль","es":"Eliminar perfil","fr":"Supprimer le profil","de":"Profil löschen"},
    "Anuluj": {"en":"Cancel","ru":"Отмена","uk":"Скасувати","es":"Cancelar","fr":"Annuler","de":"Abbrechen"},
    "Zatwierdź i zapisz": {"en":"Approve and save","ru":"Подтвердить и сохранить","uk":"Підтвердити й зберегти","es":"Aprobar y guardar","fr":"Valider et enregistrer","de":"Bestätigen und speichern"},
    "Odrzuć": {"en":"Reject","ru":"Отклонить","uk":"Відхилити","es":"Rechazar","fr":"Refuser","de":"Ablehnen"},
    "Wybieram tę ofertę": {"en":"Select this job","ru":"Выбрать вакансию","uk":"Обрати вакансію","es":"Elegir esta oferta","fr":"Choisir cette offre","de":"Diese Stelle auswählen"},
    "Usuń z wybranych": {"en":"Remove from selected","ru":"Убрать из выбранных","uk":"Вилучити з обраних","es":"Quitar de seleccionadas","fr":"Retirer de la sélection","de":"Aus Auswahl entfernen"},
    "Następne oferty": {"en":"More jobs","ru":"Следующие вакансии","uk":"Наступні вакансії","es":"Más ofertas","fr":"Offres suivantes","de":"Weitere Stellen"},
    "Następna strona Pracuj.pl": {"en":"Next Pracuj.pl page","ru":"Следующая страница Pracuj.pl","uk":"Наступна сторінка Pracuj.pl","es":"Página siguiente de Pracuj.pl","fr":"Page suivante de Pracuj.pl","de":"Nächste Pracuj.pl-Seite"},
    "Dopasowanie: ": {"en":"Match: ","ru":"Соответствие: ","uk":"Відповідність: ","es":"Coincidencia: ","fr":"Correspondance : ","de":"Passung: "},
    "Wersja profilu użyta do oceny: ": {"en":"Profile version used for assessment: ","ru":"Версия профиля для оценки: ","uk":"Версія профілю для оцінювання: ","es":"Versión del perfil usada para la evaluación: ","fr":"Version du profil utilisée pour l’évaluation : ","de":"Für die Bewertung verwendete Profilversion: "},
    "Pasuje: ": {"en":"Matches: ","ru":"Совпадения: ","uk":"Збіги: ","es":"Coincidencias: ","fr":"Correspondances : ","de":"Passende Punkte: "},
    "Braki: ": {"en":"Gaps: ","ru":"Пробелы: ","uk":"Прогалини: ","es":"Brechas: ","fr":"Écarts : ","de":"Lücken: "},
    "Wybrane oferty:": {"en":"Selected jobs:","ru":"Выбранные вакансии:","uk":"Обрані вакансії:","es":"Ofertas seleccionadas:","fr":"Offres sélectionnées :","de":"Ausgewählte Stellen:"},
    "Strona formularza: ": {"en":"Application form page: ","ru":"Страница формы заявки: ","uk":"Сторінка форми заявки: ","es":"Página del formulario: ","fr":"Page du formulaire : ","de":"Bewerbungsformular-Seite: "},
    "Status: nie udało się odczytać pól formularza automatycznie.": {"en":"Status: couldn't read form fields automatically.","ru":"Статус: не удалось автоматически прочитать поля формы.","uk":"Статус: не вдалося автоматично прочитати поля форми.","es":"Estado: no se pudieron leer automáticamente los campos.","fr":"État : impossible de lire automatiquement les champs du formulaire.","de":"Status: Formularfelder konnten nicht automatisch gelesen werden."},
    "Formularz nie jest publicznie dostępny.": {"en":"The form is not publicly accessible.","ru":"Форма недоступна публично.","uk":"Форма недоступна публічно.","es":"El formulario no es accesible públicamente.","fr":"Le formulaire n’est pas accessible publiquement.","de":"Das Formular ist nicht öffentlich zugänglich."},
    "Zewnętrzna strona aplikacji: ": {"en":"External application page: ","ru":"Внешняя страница заявки: ","uk":"Зовнішня сторінка заявки: ","es":"Página externa de solicitud: ","fr":"Page externe de candidature : ","de":"Externe Bewerbungsseite: "},
    "Pola zostały odczytane, ale przygotowanie odpowiedzi nie powiodło się.": {"en":"Fields were read, but answer preparation failed.","ru":"Поля прочитаны, но подготовить ответы не удалось.","uk":"Поля прочитано, але підготувати відповіді не вдалося.","es":"Se leyeron los campos, pero no se pudieron preparar las respuestas.","fr":"Les champs ont été lus, mais la préparation des réponses a échoué.","de":"Die Felder wurden gelesen, aber die Antworten konnten nicht vorbereitet werden."},
    "Odczytane pola: ": {"en":"Fields read: ","ru":"Прочитано полей: ","uk":"Прочитано полів: ","es":"Campos leídos: ","fr":"Champs lus : ","de":"Gelesene Felder: "},
    "Odpowiedź do skopiowania: ": {"en":"Answer to copy: ","ru":"Ответ для копирования: ","uk":"Відповідь для копіювання: ","es":"Respuesta para copiar: ","fr":"Réponse à copier : ","de":"Antwort zum Kopieren: "},
    "Brak danych: ": {"en":"Missing information: ","ru":"Недостающие данные: ","uk":"Бракує даних: ","es":"Información faltante: ","fr":"Informations manquantes : ","de":"Fehlende Angaben: "},
    "uzupełnij tę informację ręcznie": {"en":"please provide this information manually","ru":"укажите эту информацию вручную","uk":"укажіть цю інформацію вручну","es":"completa esta información manualmente","fr":"veuillez compléter cette information manuellement","de":"bitte diese Angabe manuell ergänzen"},
    "Wybierz funkcję z menu": {"en":"Choose a menu option","ru":"Выберите функцию в меню","uk":"Виберіть функцію в меню","es":"Elige una opción del menú","fr":"Choisissez une option","de":"Wähle eine Funktion im Menü"},
    "Oryginalny plik CV pozostanie lokalnie. Usunąć zapisany profil?": {"en":"The original CV file will remain local. Delete the saved profile?","ru":"Исходный файл CV останется локально. Удалить сохранённый профиль?","uk":"Початковий файл CV залишиться локально. Видалити збережений профіль?","es":"El archivo CV original permanecerá local. ¿Eliminar el perfil guardado?","fr":"Le CV original restera en local. Supprimer le profil enregistré ?","de":"Die Originaldatei bleibt lokal gespeichert. Gespeichertes Profil löschen?"},
    "Oryginalny plik CV pozostanie lokalnie. Usunąć zapisany profil?": {"en":"The original CV file will remain local. Delete the saved profile?","ru":"Исходный файл CV останется локально. Удалить сохранённый профиль?","uk":"Початковий файл CV залишиться локально. Видалити збережений профіль?","es":"El archivo CV original permanecerá local. ¿Eliminar el perfil guardado?","fr":"Le CV original restera en local. Supprimer le profil enregistré ?","de":"Die Originaldatei bleibt lokal gespeichert. Gespeichertes Profil löschen?"},
    "Nie znaleziono publicznego linku Aplikuj ani formularza HTML. Strona aplikacji może wymagać logowania lub dynamicznego widoku.": {"en":"No public Apply link or HTML form was found. The application page may require sign-in or dynamic rendering.","ru":"Не найдена публичная ссылка «Откликнуться» или HTML-форма. Страница может требовать входа или динамического отображения.","uk":"Не знайдено публічного посилання «Відгукнутися» або HTML-форми. Сторінка може вимагати входу чи динамічного відображення.","es":"No se encontró un enlace público para solicitar ni un formulario HTML. La página puede requerir iniciar sesión o contenido dinámico.","fr":"Aucun lien public de candidature ni formulaire HTML trouvé. La page peut nécessiter une connexion ou un affichage dynamique.","de":"Kein öffentlicher Bewerbungslink oder kein HTML-Formular gefunden. Die Seite erfordert möglicherweise eine Anmeldung oder dynamische Darstellung."},
    "Link do formularza nie używa HTTPS.": {"en":"The application form link does not use HTTPS.","ru":"Ссылка на форму не использует HTTPS.","uk":"Посилання на форму не використовує HTTPS.","es":"El enlace del formulario no utiliza HTTPS.","fr":"Le lien du formulaire n’utilise pas HTTPS.","de":"Der Formularlink verwendet kein HTTPS."},
    "Oferta kieruje do zewnętrznego systemu rekrutacyjnego; bot nie loguje się tam ani nie odczytuje jego formularza.": {"en":"This job uses an external recruitment system. The bot does not sign in or read its form.","ru":"Вакансия ведёт во внешнюю систему найма; бот не входит туда и не читает форму.","uk":"Вакансія веде до зовнішньої системи найму; бот не входить туди й не читає форму.","es":"La oferta utiliza un sistema externo. El bot no inicia sesión ni lee su formulario.","fr":"Cette offre utilise un système externe. Le bot ne s’y connecte pas et ne lit pas son formulaire.","de":"Diese Stelle nutzt ein externes Bewerbersystem. Der Bot meldet sich dort nicht an und liest das Formular nicht."},
    "Formularz nie jest widoczny w publicznym HTML. Może wymagać logowania do Pracuj.pl albo dynamicznego widoku; bot nie korzysta z konta użytkownika.": {"en":"The form is not visible in public HTML. It may require a Pracuj.pl login or dynamic rendering; the bot does not use your account.","ru":"Форма не видна в открытом HTML. Может потребоваться вход на Pracuj.pl или динамическая загрузка; бот не использует вашу учётную запись.","uk":"Форма не видна у відкритому HTML. Може знадобитися вхід на Pracuj.pl або динамічне завантаження; бот не використовує ваш обліковий запис.","es":"El formulario no aparece en el HTML público. Puede requerir iniciar sesión en Pracuj.pl o contenido dinámico; el bot no usa tu cuenta.","fr":"Le formulaire n’apparaît pas dans le HTML public. Une connexion à Pracuj.pl ou un affichage dynamique peut être nécessaire ; le bot n’utilise pas votre compte.","de":"Das Formular ist im öffentlichen HTML nicht sichtbar. Es erfordert möglicherweise eine Anmeldung bei Pracuj.pl oder dynamische Darstellung; der Bot nutzt dein Konto nicht."},
}
for _key, _value in _extra.items():
    UI_PHRASES.setdefault(_key, _value)

BOT_COMMAND_DESCRIPTIONS = {
    "pl": ["Instrukcje i stan bota", "Pokaż swój identyfikator Telegram", "Przygotuj profil z zapisanego CV", "Pokaż aktywny profil", "Zarządzaj profilami CV", "Zmień aktywny profil", "Uzupełnij brakujące informacje", "Usuń aktywny profil", "Przetłumacz profil", "Szukaj ofert na Pracuj.pl", "Pokaż wybrane oferty", "Sprawdź formularze wybranych ofert", "Anuluj oczekującą operację", "Zmień język interfejsu bota"],
    "en": ["Bot status and instructions", "Show your Telegram ID", "Build a profile from saved CV", "Show active profile", "Manage CV profiles", "Change active profile", "Complete missing information", "Delete active profile", "Translate profile", "Search Pracuj.pl jobs", "Show selected jobs", "Review selected application forms", "Cancel pending operation", "Change bot interface language"],
    "ru": ["Состояние и инструкции бота", "Показать Telegram ID", "Создать профиль из сохранённого CV", "Показать активный профиль", "Управление профилями CV", "Сменить активный профиль", "Дополнить недостающие сведения", "Удалить активный профиль", "Перевести профиль", "Искать вакансии на Pracuj.pl", "Показать выбранные вакансии", "Проверить формы выбранных заявок", "Отменить текущую операцию", "Изменить язык интерфейса бота"],
    "uk": ["Стан та інструкції бота", "Показати Telegram ID", "Створити профіль зі збереженого CV", "Показати активний профіль", "Керувати профілями CV", "Змінити активний профіль", "Доповнити відсутні дані", "Видалити активний профіль", "Перекласти профіль", "Шукати вакансії на Pracuj.pl", "Показати обрані вакансії", "Перевірити форми обраних заявок", "Скасувати поточну операцію", "Змінити мову інтерфейсу бота"],
    "es": ["Estado e instrucciones del bot", "Mostrar tu ID de Telegram", "Crear perfil desde CV guardado", "Mostrar perfil activo", "Gestionar perfiles CV", "Cambiar perfil activo", "Completar datos que faltan", "Eliminar perfil activo", "Traducir perfil", "Buscar ofertas en Pracuj.pl", "Mostrar ofertas seleccionadas", "Revisar formularios seleccionados", "Cancelar operación pendiente", "Cambiar idioma de la interfaz"],
    "fr": ["État et instructions du bot", "Afficher votre identifiant Telegram", "Créer un profil depuis le CV enregistré", "Afficher le profil actif", "Gérer les profils CV", "Changer le profil actif", "Compléter les informations manquantes", "Supprimer le profil actif", "Traduire le profil", "Rechercher des offres sur Pracuj.pl", "Afficher les offres sélectionnées", "Vérifier les formulaires sélectionnés", "Annuler l’opération en attente", "Changer la langue de l’interface"],
    "de": ["Botstatus und Anleitungen", "Telegram-ID anzeigen", "Profil aus gespeichertem Lebenslauf erstellen", "Aktives Profil anzeigen", "CV-Profile verwalten", "Aktives Profil wechseln", "Fehlende Angaben ergänzen", "Aktives Profil löschen", "Profil übersetzen", "Stellen auf Pracuj.pl suchen", "Ausgewählte Stellen anzeigen", "Ausgewählte Formulare prüfen", "Laufenden Vorgang abbrechen", "Sprache der Bot-Oberfläche ändern"],
}

COMMANDS = ("start", "id", "analyze", "profile", "cvs", "complete", "deleteprofile", "jobs", "selected", "apply", "cancel", "language")
BOT_COMMAND_DESCRIPTIONS = {
 "pl": ["Otwórz menu bota", "Pokaż identyfikator Telegram", "Przygotuj profil z CV", "Pokaż profil użytkownika", "Zarządzaj CV i profilami", "Uzupełnij profil", "Usuń aktywny profil", "Szukaj pasujących ofert", "Pokaż wybrane oferty", "Przygotuj odpowiedzi do aplikacji", "Anuluj bieżącą operację", "Zmień język interfejsu"],
 "en": ["Open the bot menu", "Show Telegram ID", "Build a profile from a CV", "Show your profile", "Manage CVs and profiles", "Complete your profile", "Delete the active profile", "Search matching jobs", "Show selected jobs", "Prepare application answers", "Cancel the current operation", "Change interface language"],
 "ru": ["Открыть меню бота", "Показать Telegram ID", "Создать профиль по CV", "Показать профиль", "Управлять CV и профилями", "Дополнить профиль", "Удалить активный профиль", "Искать подходящие вакансии", "Показать выбранные вакансии", "Подготовить ответы для заявки", "Отменить текущую операцию", "Изменить язык интерфейса"],
 "uk": ["Відкрити меню бота", "Показати Telegram ID", "Створити профіль із CV", "Показати профіль", "Керувати CV та профілями", "Доповнити профіль", "Видалити активний профіль", "Шукати відповідні вакансії", "Показати вибрані вакансії", "Підготувати відповіді для заявки", "Скасувати поточну дію", "Змінити мову інтерфейсу"],
 "es": ["Abrir el menú del bot", "Mostrar ID de Telegram", "Crear perfil desde el CV", "Mostrar tu perfil", "Gestionar CV y perfiles", "Completar el perfil", "Eliminar el perfil activo", "Buscar ofertas adecuadas", "Mostrar ofertas seleccionadas", "Preparar respuestas de solicitud", "Cancelar la operación actual", "Cambiar idioma de interfaz"],
 "fr": ["Ouvrir le menu du bot", "Afficher l’identifiant Telegram", "Créer un profil depuis le CV", "Afficher votre profil", "Gérer CV et profils", "Compléter le profil", "Supprimer le profil actif", "Rechercher des offres adaptées", "Afficher les offres sélectionnées", "Préparer les réponses de candidature", "Annuler l’opération en cours", "Changer la langue de l’interface"],
 "de": ["Botmenü öffnen", "Telegram-ID anzeigen", "Profil aus Lebenslauf erstellen", "Profil anzeigen", "Lebensläufe und Profile verwalten", "Profil ergänzen", "Aktives Profil löschen", "Passende Stellen suchen", "Ausgewählte Stellen anzeigen", "Bewerbungsantworten vorbereiten", "Aktuellen Vorgang abbrechen", "Oberflächensprache ändern"],
}


def commands_for_language(language: str) -> list[tuple[str, str]]:
    descriptions = BOT_COMMAND_DESCRIPTIONS.get(normalize_language(language), BOT_COMMAND_DESCRIPTIONS["en"])
    return list(zip(COMMANDS, descriptions))

_MORE_PHRASES = {
"Dostęp nie jest skonfigurowany. Wyślij /id, wpisz wynik jako TELEGRAM_OWNER_ID w lokalnym .env i uruchom bota ponownie.": ["Access is not configured. Send /id, add the result as TELEGRAM_OWNER_ID to your local .env, then restart the bot.","Доступ не настроен. Отправьте /id, добавьте полученное значение в TELEGRAM_OWNER_ID в локальном .env и перезапустите бота.","Доступ не налаштовано. Надішліть /id, додайте отримане значення до TELEGRAM_OWNER_ID у локальному .env і перезапустіть бота.","El acceso no está configurado. Envía /id, añade el resultado como TELEGRAM_OWNER_ID a tu .env local y reinicia el bot.","L’accès n’est pas configuré. Envoyez /id, ajoutez le résultat à TELEGRAM_OWNER_ID dans votre .env local, puis redémarrez le bot.","Der Zugriff ist nicht eingerichtet. Sende /id, trage den Wert als TELEGRAM_OWNER_ID in deine lokale .env ein und starte den Bot neu."],
"Nie rozpoznałem tego przycisku. Użyj /start, aby odświeżyć menu.": ["I don't recognize this button. Use /start to refresh the menu.","Не удалось распознать кнопку. Используйте /start, чтобы обновить меню.","Не вдалося розпізнати кнопку. Скористайтеся /start, щоб оновити меню.","No reconozco este botón. Usa /start para actualizar el menú.","Je ne reconnais pas ce bouton. Utilisez /start pour actualiser le menu.","Diese Schaltfläche ist unbekannt. Verwende /start, um das Menü zu aktualisieren."],
"Nie mam zatwierdzonego profilu. Wyślij CV i użyj /analyze.": ["There is no approved profile yet. Send a CV and use /analyze.","Подтверждённого профиля пока нет. Отправьте CV и используйте /analyze.","Підтвердженого профілю ще немає. Надішліть CV і скористайтеся /analyze.","Aún no hay un perfil aprobado. Envía un CV y usa /analyze.","Aucun profil n’a été validé. Envoyez un CV et utilisez /analyze.","Es gibt noch kein freigegebenes Profil. Sende einen Lebenslauf und verwende /analyze."],
"Nie ma jeszcze zapisanego profilu. Wyślij CV i zatwierdź jego analizę.": ["No profile has been saved yet. Send a CV and approve its analysis.","Профиль ещё не сохранён. Отправьте CV и подтвердите анализ.","Профіль ще не збережено. Надішліть CV і підтвердьте його аналіз.","Aún no se ha guardado ningún perfil. Envía un CV y aprueba su análisis.","Aucun profil n’a encore été enregistré. Envoyez un CV et validez son analyse.","Es wurde noch kein Profil gespeichert. Sende einen Lebenslauf und bestätige die Analyse."],
"Najpierw zapisz profil przyciskiem „Przygotuj profil z CV”.": ["First create a profile using “Build profile from CV”.","Сначала создайте профиль кнопкой «Создать профиль из CV».","Спочатку створіть профіль кнопкою «Створити профіль із CV».","Primero crea un perfil con «Crear perfil desde el CV».","Créez d’abord un profil avec « Créer un profil depuis le CV ».","Erstelle zuerst mit „Profil aus Lebenslauf erstellen“ ein Profil."],
"Nie ma aktywnego profilu do usunięcia.": ["There is no active profile to delete.","Нет активного профиля для удаления.","Немає активного профілю для видалення.","No hay ningún perfil activo que eliminar.","Aucun profil actif à supprimer.","Es gibt kein aktives Profil zum Löschen."],
"Najpierw zapisz profil poleceniem /analyze.": ["First create a profile with /analyze.","Сначала создайте профиль командой /analyze.","Спочатку створіть профіль командою /analyze.","Primero crea un perfil con /analyze.","Créez d’abord un profil avec /analyze.","Erstelle zuerst mit /analyze ein Profil."],
"Nie udało się znaleźć ofert na tej stronie albo Pracuj.pl zablokował automatyczny odczyt. Spróbuj innego zapytania później.": ["No jobs were found on this page, or Pracuj.pl blocked automatic access. Try another query later.","Вакансии не найдены или Pracuj.pl заблокировал автоматическое чтение. Попробуйте позже с другим запросом.","Вакансій не знайдено або Pracuj.pl заблокував автоматичне читання. Спробуйте пізніше з іншим запитом.","No se encontraron ofertas o Pracuj.pl bloqueó el acceso automático. Prueba otra búsqueda más tarde.","Aucune offre trouvée ou Pracuj.pl a bloqué l’accès automatique. Réessayez plus tard avec une autre recherche.","Keine Stellen gefunden oder Pracuj.pl hat den automatischen Zugriff blockiert. Versuche später eine andere Suche."],
"Nie ma już ofert na tej stronie wyników.": ["There are no more jobs on this results page.","На этой странице больше нет вакансий.","На цій сторінці більше немає вакансій.","No hay más ofertas en esta página.","Il n’y a plus d’offres sur cette page.","Auf dieser Ergebnisseite gibt es keine weiteren Stellen."],
"Najpierw zapisz aktywny profil poleceniem /analyze.": ["First create an active profile with /analyze.","Сначала создайте активный профиль командой /analyze.","Спочатку створіть активний профіль командою /analyze.","Primero crea un perfil activo con /analyze.","Créez d’abord un profil actif avec /analyze.","Erstelle zuerst mit /analyze ein aktives Profil."],
"Nie wybrano jeszcze ofert. Użyj /jobs, aby wyszukać i zaznaczyć oferty.": ["No jobs selected yet. Use /jobs to search and select jobs.","Вакансии ещё не выбраны. Используйте /jobs, чтобы найти и выбрать вакансии.","Вакансії ще не вибрано. Скористайтеся /jobs, щоб знайти й обрати їх.","Aún no has seleccionado ofertas. Usa /jobs para buscarlas y seleccionarlas.","Aucune offre sélectionnée. Utilisez /jobs pour rechercher et sélectionner des offres.","Noch keine Stellen ausgewählt. Verwende /jobs, um Stellen zu suchen und auszuwählen."],
"Nie wybrano ofert. Najpierw zaznacz je w wynikach /jobs.": ["No jobs selected. Select them in the /jobs results first.","Вакансии не выбраны. Сначала отметьте их в результатах /jobs.","Вакансії не вибрано. Спочатку позначте їх у результатах /jobs.","No hay ofertas seleccionadas. Selecciónalas primero en los resultados de /jobs.","Aucune offre sélectionnée. Sélectionnez-en d’abord dans les résultats de /jobs.","Keine Stellen ausgewählt. Wähle zuerst Stellen in den /jobs-Ergebnissen aus."],
"Nie ma aktywnego profilu kandydata. Najpierw przeanalizuj i zatwierdź CV.": ["There is no active candidate profile. Analyze and approve a CV first.","Нет активного профиля кандидата. Сначала проанализируйте и подтвердите CV.","Немає активного профілю кандидата. Спочатку проаналізуйте й підтвердьте CV.","No hay un perfil activo. Primero analiza y aprueba un CV.","Aucun profil candidat actif. Analysez et validez d’abord un CV.","Kein aktives Kandidatenprofil vorhanden. Analysiere zuerst einen Lebenslauf und bestätige ihn."],
"Nie ma aktywnego profilu. Wyślij CV i uruchom /analyze.": ["There is no active profile. Send a CV and run /analyze.","Нет активного профиля. Отправьте CV и запустите /analyze.","Немає активного профілю. Надішліть CV і запустіть /analyze.","No hay un perfil activo. Envía un CV y ejecuta /analyze.","Aucun profil actif. Envoyez un CV et lancez /analyze.","Kein aktives Profil. Sende einen Lebenslauf und starte /analyze."],
"Wyślij tekstowe informacje do dopisania albo /cancel.": ["Send the text to add, or use /cancel.","Отправьте текст для дополнения или используйте /cancel.","Надішліть текст для доповнення або скористайтеся /cancel.","Envía el texto que quieres añadir o usa /cancel.","Envoyez le texte à ajouter ou utilisez /cancel.","Sende die Angaben zum Ergänzen oder verwende /cancel."],
"Nie rozpoznałem oczekiwanej odpowiedzi. Użyj /start, aby zobaczyć dostępne polecenia.": ["I couldn't identify the expected response. Use /start to see available commands.","Не удалось распознать ожидаемый ответ. Используйте /start, чтобы увидеть команды.","Не вдалося розпізнати очікувану відповідь. Скористайтеся /start, щоб побачити команди.","No pude identificar la respuesta esperada. Usa /start para ver los comandos.","Je n’ai pas reconnu la réponse attendue. Utilisez /start pour voir les commandes.","Die erwartete Antwort wurde nicht erkannt. Verwende /start für die verfügbaren Befehle."],
"Ta oferta nie znajduje się już w wynikach. Uruchom /jobs ponownie.": ["This job is no longer in the results. Run /jobs again.","Этой вакансии больше нет в результатах. Запустите /jobs ещё раз.","Цієї вакансії більше немає в результатах. Запустіть /jobs ще раз.","Esta oferta ya no aparece. Ejecuta /jobs de nuevo.","Cette offre n’est plus dans les résultats. Relancez /jobs.","Diese Stelle ist nicht mehr in den Ergebnissen. Starte /jobs erneut."],
"Ta oferta nie znajduje się na liście wybranych. Użyj /selected, aby sprawdzić wybór.": ["This job is not selected. Use /selected to review your selection.","Эта вакансия не выбрана. Проверьте список командой /selected.","Цю вакансію не обрано. Перевірте список командою /selected.","Esta oferta no está seleccionada. Usa /selected para revisar la lista.","Cette offre n’est pas sélectionnée. Utilisez /selected pour vérifier votre sélection.","Diese Stelle ist nicht ausgewählt. Prüfe die Auswahl mit /selected."],
"Podaj stanowisko lub słowa kluczowe: /jobs Kierownik projektu | Wrocław": ["Enter a job title or keywords: /jobs Project Manager | London","Укажите должность или ключевые слова: /jobs Руководитель проекта | Москва","Вкажіть посаду або ключові слова: /jobs Керівник проєкту | Київ","Indica el puesto o palabras clave: /jobs Project Manager | Madrid","Indiquez un poste ou des mots-clés : /jobs Chef de projet | Paris","Gib eine Stellenbezeichnung oder Stichwörter ein: /jobs Projektleiter | Berlin"],
"Anulowano. Profil pozostał zapisany.": ["Cancelled. The profile remains saved.","Отменено. Профиль остался сохранён.","Скасовано. Профіль залишився збереженим.","Cancelado. El perfil sigue guardado.","Annulé. Le profil reste enregistré.","Abgebrochen. Das Profil bleibt gespeichert."],
"Oferta została dodana do wybranych. Zobacz listę przez /selected.": ["Job added to your selection. View it with /selected.","Вакансия добавлена в выбранные. Список: /selected.","Вакансію додано до обраних. Перегляньте список: /selected.","Oferta añadida a tu selección. Consulta /selected.","Offre ajoutée à la sélection. Consultez /selected.","Stelle zur Auswahl hinzugefügt. Mit /selected anzeigen."],
"Usunięto ofertę z wybranych.": ["Job removed from your selection.","Вакансия удалена из выбранных.","Вакансію вилучено з обраних.","Oferta eliminada de la selección.","Offre retirée de la sélection.","Stelle aus der Auswahl entfernt."],
"Gotowe. Zakończyłem sprawdzanie wybranych formularzy; wysyłam podsumowanie.": ["Done. I finished checking the selected forms; sending the summary.","Готово. Проверка выбранных форм завершена; отправляю сводку.","Готово. Перевірку обраних форм завершено; надсилаю підсумок.","Listo. Terminé de revisar los formularios; envío el resumen.","Terminé. Vérification des formulaires achevée ; envoi du résumé.","Fertig. Die ausgewählten Formulare wurden geprüft; die Zusammenfassung wird gesendet."],
"Oryginalny plik CV pozostanie lokalnie. Usunąć zapisany profil?": ["The original CV file will remain local. Delete the saved profile?","Исходный CV останется локально. Удалить сохранённый профиль?","Початкове CV залишиться локально. Видалити збережений профіль?","El CV original permanecerá local. ¿Eliminar el perfil guardado?","Le CV original restera en local. Supprimer le profil enregistré ?","Die Originaldatei bleibt lokal. Gespeichertes Profil löschen?"],
"Wybierz język profilu:": ["Choose the profile language:","Выберите язык профиля:","Виберіть мову профілю:","Elige el idioma del perfil:","Choisissez la langue du profil :","Profilsprache auswählen:"],
"Zapisane profile. Wybierz CV, którego profil ma być aktywny:": ["Saved profiles. Choose which CV profile to activate:","Сохранённые профили. Выберите профиль CV для активации:","Збережені профілі. Виберіть профіль CV для активації:","Perfiles guardados. Elige qué perfil CV activar:","Profils enregistrés. Choisissez le profil CV à activer :","Gespeicherte Profile. Wähle das zu aktivierende CV-Profil:"],
"Nie udało się dokończyć tej operacji. Bot odebrał polecenie, ale wystąpił błąd; spróbuj ponownie.": ["The operation couldn't be completed. The bot received your request but encountered an error; try again.","Не удалось завершить операцию. Бот получил команду, но произошла ошибка; попробуйте снова.","Не вдалося завершити операцію. Бот отримав команду, але сталася помилка; спробуйте ще раз.","No se pudo completar la operación. El bot recibió la solicitud, pero ocurrió un error; inténtalo de nuevo.","Impossible de terminer l’opération. Le bot a reçu la demande, mais une erreur est survenue ; réessayez.","Der Vorgang konnte nicht abgeschlossen werden. Der Bot erhielt den Auftrag, aber ein Fehler trat auf. Bitte erneut versuchen."],
"Anulowano oczekującą operację. Zapisany oryginał CV pozostał na komputerze.": ["Pending operation cancelled. The original CV remains saved on this computer.","Операция отменена. Исходное CV осталось на этом компьютере.","Операцію скасовано. Початкове CV залишилося на цьому комп’ютері.","Operación cancelada. El CV original sigue guardado en este equipo.","Opération annulée. Le CV original reste enregistré sur cet ordinateur.","Vorgang abgebrochen. Der ursprüngliche Lebenslauf bleibt auf diesem Computer gespeichert."],
}
for _source, _values in _MORE_PHRASES.items():
    UI_PHRASES[_source] = dict(zip(("en", "ru", "uk", "es", "fr", "de"), _values))


_MORE_UI = {
"Nie mam zapisanego CV. Prześlij plik PDF, DOCX lub TXT.":["No saved CV found. Send a PDF, DOCX or TXT file.","Сохранённое CV не найдено. Отправьте PDF, DOCX или TXT.","Збережене CV не знайдено. Надішліть PDF, DOCX або TXT.","No hay CV guardado. Envía un PDF, DOCX o TXT.","Aucun CV enregistré. Envoyez un PDF, DOCX ou TXT.","Kein CV gespeichert. Sende eine PDF-, DOCX- oder TXT-Datei."],
"Nie mam zatwierdzonego profilu. Wyślij CV i użyj /analyze.":["There is no approved profile yet. Send a CV and use /analyze.","Подтверждённого профиля пока нет. Отправьте CV и используйте /analyze.","Підтвердженого профілю ще немає. Надішліть CV і скористайтеся /analyze.","Aún no hay perfil aprobado. Envía un CV y usa /analyze.","Aucun profil validé. Envoyez un CV et utilisez /analyze.","Noch kein Profil freigegeben. Sende einen Lebenslauf und nutze /analyze."],
"Nie ma aktywnego profilu. Wyślij CV i uruchom /analyze.":["There is no active profile. Send a CV and run /analyze.","Нет активного профиля. Отправьте CV и запустите /analyze.","Немає активного профілю. Надішліть CV і запустіть /analyze.","No hay perfil activo. Envía un CV y ejecuta /analyze.","Aucun profil actif. Envoyez un CV et lancez /analyze.","Kein aktives Profil. Sende einen Lebenslauf und starte /analyze."],
"Nie ma aktywnego profilu do usunięcia.":["There is no active profile to delete.","Нет активного профиля для удаления.","Немає активного профілю для видалення.","No hay perfil activo que eliminar.","Aucun profil actif à supprimer.","Kein aktives Profil zum Löschen."],
"Nie ma aktywnego profilu.":["There is no active profile.","Нет активного профиля.","Немає активного профілю.","No hay un perfil activo.","Aucun profil actif.","Kein aktives Profil vorhanden."],
"Nie znaleziono tego profilu.":["This profile was not found.","Профиль не найден.","Профіль не знайдено.","No se encontró este perfil.","Profil introuvable.","Profil nicht gefunden."],
"Nie wybrano ofert. Najpierw zaznacz je w wynikach /jobs.":["No jobs selected. Select them in the /jobs results first.","Вакансии не выбраны. Сначала отметьте их в результатах /jobs.","Вакансії не обрано. Спочатку позначте їх у результатах /jobs.","No hay ofertas seleccionadas. Selecciónalas primero en /jobs.","Aucune offre sélectionnée. Sélectionnez-en d’abord dans /jobs.","Keine Stellen ausgewählt. Wähle zuerst Stellen in /jobs aus."],
"Nie ma aktywnego profilu kandydata. Najpierw przeanalizuj i zatwierdź CV.":["There is no active candidate profile. Analyze and approve a CV first.","Нет активного профиля кандидата. Сначала проанализируйте и подтвердите CV.","Немає активного профілю кандидата. Спочатку проаналізуйте й підтвердьте CV.","No hay perfil de candidato activo. Primero analiza y aprueba un CV.","Aucun profil candidat actif. Analysez et validez d’abord un CV.","Kein aktives Kandidatenprofil. Analysiere zuerst einen Lebenslauf und bestätige ihn."],
"Wyślij tekstowe informacje do dopisania albo /cancel.":["Send the information to add, or use /cancel.","Отправьте сведения для добавления или используйте /cancel.","Надішліть відомості для доповнення або скористайтеся /cancel.","Envía la información que quieres añadir o usa /cancel.","Envoyez les informations à ajouter ou utilisez /cancel.","Sende die Angaben zum Ergänzen oder nutze /cancel."],
"Ta oferta nie znajduje się już w wynikach. Uruchom /jobs ponownie.":["This job is no longer in the results. Run /jobs again.","Этой вакансии больше нет в результатах. Запустите /jobs ещё раз.","Цієї вакансії більше немає в результатах. Запустіть /jobs ще раз.","Esta oferta ya no aparece. Ejecuta /jobs de nuevo.","Cette offre n’est plus dans les résultats. Relancez /jobs.","Diese Stelle ist nicht mehr in den Ergebnissen. Starte /jobs erneut."],
"Ta oferta nie znajduje się na liście wybranych. Użyj /selected, aby sprawdzić wybór.":["This job isn't selected. Use /selected to review your selection.","Эта вакансия не выбрана. Проверьте список с помощью /selected.","Цю вакансію не обрано. Перевірте список за допомогою /selected.","Esta oferta no está seleccionada. Usa /selected para revisar tu lista.","Cette offre n’est pas sélectionnée. Vérifiez avec /selected.","Diese Stelle ist nicht ausgewählt. Prüfe die Auswahl mit /selected."],
"Nie udało się przetłumaczyć profilu. Oryginalna wersja pozostała bez zmian.":["Couldn't translate the profile. The original version is unchanged.","Не удалось перевести профиль. Исходная версия не изменена.","Не вдалося перекласти профіль. Початкова версія не змінилася.","No se pudo traducir el perfil. La versión original sigue igual.","Impossible de traduire le profil. La version originale reste inchangée.","Das Profil konnte nicht übersetzt werden. Die Originalversion bleibt unverändert."],
"Zapisane profile. Wybierz CV, którego profil ma być aktywny:":["Saved profiles. Choose which CV profile to activate:","Сохранённые профили. Выберите профиль CV для активации:","Збережені профілі. Виберіть профіль CV для активації:","Perfiles guardados. Elige el perfil CV que quieres activar:","Profils enregistrés. Choisissez le profil CV à activer :","Gespeicherte Profile. Wähle das zu aktivierende CV-Profil:"],
"Oryginalny plik CV pozostanie lokalnie. Usunąć zapisany profil?":["The original CV file stays local. Delete the saved profile?","Исходный файл CV останется локально. Удалить сохранённый профиль?","Початковий файл CV залишиться локально. Видалити збережений профіль?","El CV original seguirá local. ¿Eliminar el perfil guardado?","Le CV original reste en local. Supprimer le profil enregistré ?","Die Originaldatei bleibt lokal. Gespeichertes Profil löschen?"],
"Gotowe. Zakończyłem sprawdzanie wybranych formularzy; wysyłam podsumowanie.":["Done. I finished checking the selected forms; sending the summary.","Готово. Проверка выбранных форм завершена; отправляю сводку.","Готово. Перевірку обраних форм завершено; надсилаю підсумок.","Listo. Terminé de revisar los formularios; envío el resumen.","Terminé. Vérification des formulaires achevée ; envoi du résumé.","Fertig. Die ausgewählten Formulare wurden geprüft; die Zusammenfassung wird gesendet."],
"Podaj stanowisko lub słowa kluczowe: /jobs Kierownik projektu | Wrocław":["Enter a job title or keywords: /jobs Project Manager | London","Укажите должность или ключевые слова: /jobs Руководитель проекта | Москва","Вкажіть посаду або ключові слова: /jobs Керівник проєкту | Київ","Indica un puesto o palabras clave: /jobs Project Manager | Madrid","Indiquez un poste ou des mots-clés : /jobs Chef de projet | Paris","Gib einen Stellentitel oder Stichwörter ein: /jobs Projektleiter | Berlin"],
"Anulowano oczekującą operację. Zapisany oryginał CV pozostał na komputerze.":["Pending operation cancelled. The original CV remains on this computer.","Операция отменена. Исходное CV осталось на этом компьютере.","Операцію скасовано. Початкове CV залишилося на цьому комп’ютері.","Operación cancelada. El CV original sigue en este equipo.","Opération annulée. Le CV original reste sur cet ordinateur.","Vorgang abgebrochen. Der ursprüngliche Lebenslauf bleibt auf diesem Computer."],
"Wybrano wersję ":["Selected version ","Выбрана версия ","Вибрано версію ","Versión seleccionada ","Version sélectionnée ","Version ausgewählt: "],
"Aktywny profil zmieniono na ":["Active profile changed to ","Активный профиль изменён на ","Активний профіль змінено на ","Perfil activo cambiado a ","Profil actif changé : ","Aktives Profil geändert zu "],
"Twój Telegram ID: ":["Your Telegram ID: ","Ваш Telegram ID: ","Ваш Telegram ID: ","Tu ID de Telegram: ","Votre identifiant Telegram : ","Deine Telegram-ID: "],
"Strona formularza: ":["Application form page: ","Страница формы заявки: ","Сторінка форми заявки: ","Página del formulario: ","Page du formulaire : ","Bewerbungsformular-Seite: "],
"Odczytane pola: ":["Fields read: ","Прочитано полей: ","Прочитано полів: ","Campos leídos: ","Champs lus : ","Gelesene Felder: "],
"Odpowiedź do skopiowania: ":["Answer to copy: ","Ответ для копирования: ","Відповідь для копіювання: ","Respuesta para copiar: ","Réponse à copier : ","Antwort zum Kopieren: "],
"Brak danych: ":["Missing information: ","Недостающие данные: ","Бракує даних: ","Información faltante: ","Informations manquantes : ","Fehlende Angaben: "],
"brak potwierdzonych dopasowań":["no confirmed matches","нет подтверждённых совпадений","немає підтверджених збігів","sin coincidencias confirmadas","aucune correspondance confirmée","keine bestätigten Übereinstimmungen"],
"brak wskazanych luk":["no identified gaps","пробелы не указаны","прогалин не вказано","sin brechas identificadas","aucun écart identifié","keine erkannten Lücken"],
"Nie udało się automatycznie otworzyć publicznej strony oferty: ":["Couldn't automatically open the public job page: ","Не удалось автоматически открыть публичную страницу вакансии: ","Не вдалося автоматично відкрити публічну сторінку вакансії: ","No se pudo abrir automáticamente la página pública: ","Impossible d’ouvrir automatiquement la page publique de l’offre : ","Öffentliche Stellenseite konnte nicht automatisch geöffnet werden: "],
"Nie udało się automatycznie otworzyć strony formularza: ":["Couldn't automatically open the application form page: ","Не удалось автоматически открыть страницу формы заявки: ","Не вдалося автоматично відкрити сторінку форми заявки: ","No se pudo abrir automáticamente la página del formulario: ","Impossible d’ouvrir automatiquement la page du formulaire : ","Bewerbungsformular-Seite konnte nicht automatisch geöffnet werden: "],
"Teraz oceniam dopasowanie do profilu…":["Now assessing matches to your profile…","Теперь оцениваю соответствие профилю…","Тепер оцінюю відповідність профілю…","Ahora evalúo la coincidencia con tu perfil…","Évaluation de la correspondance avec le profil…","Passung zum Profil wird bewertet…"],
"Wysyłam wyniki…":["Sending results…","Отправляю результаты…","Надсилаю результати…","Enviando resultados…","Envoi des résultats…","Ergebnisse werden gesendet…"],
"Sprawdzam formularz ":["Checking application form ","Проверяю форму заявки ","Перевіряю форму заявки ","Revisando el formulario ","Vérification du formulaire ","Bewerbungsformular wird geprüft: "],
"Przygotowuję odpowiedzi ":["Preparing answers ","Готовлю ответы ","Готую відповіді ","Preparando respuestas ","Préparation des réponses ","Antworten werden vorbereitet: "],
"Nadal trwa (":["Still running (","Всё ещё выполняется (","Ще виконується (","Sigue en curso (","Toujours en cours (","Läuft weiterhin ("],
}
for _source, _values in _MORE_UI.items():
    UI_PHRASES[_source] = dict(zip(("en","ru","uk","es","fr","de"), _values))


_FINAL_COPY = {
"Nie mam zapisanego CV. Prześlij plik PDF, DOCX lub TXT.":["No saved CV found. Send a PDF, DOCX or TXT file.","Сохранённое CV не найдено. Отправьте PDF, DOCX или TXT.","Збережене CV не знайдено. Надішліть PDF, DOCX або TXT.","No hay un CV guardado. Envía un PDF, DOCX o TXT.","Aucun CV enregistré. Envoyez un PDF, DOCX ou TXT.","Kein CV gespeichert. Sende eine PDF-, DOCX- oder TXT-Datei."],
"Nie mam zatwierdzonego profilu. Wyślij CV i użyj /analyze.":["There is no approved profile yet. Send a CV and use /analyze.","Подтверждённого профиля пока нет. Отправьте CV и используйте /analyze.","Підтвердженого профілю ще немає. Надішліть CV і скористайтеся /analyze.","Aún no hay un perfil aprobado. Envía un CV y usa /analyze.","Aucun profil validé. Envoyez un CV et utilisez /analyze.","Noch kein Profil freigegeben. Sende einen Lebenslauf und nutze /analyze."],
"Nie ma aktywnego profilu. Wyślij CV i uruchom /analyze.":["There is no active profile. Send a CV and run /analyze.","Нет активного профиля. Отправьте CV и запустите /analyze.","Немає активного профілю. Надішліть CV і запустіть /analyze.","No hay un perfil activo. Envía un CV y ejecuta /analyze.","Aucun profil actif. Envoyez un CV et lancez /analyze.","Kein aktives Profil. Sende einen Lebenslauf und starte /analyze."],
"Nie ma aktywnego profilu do usunięcia.":["There is no active profile to delete.","Нет активного профиля для удаления.","Немає активного профілю для видалення.","No hay un perfil activo que eliminar.","Aucun profil actif à supprimer.","Kein aktives Profil zum Löschen."],
"Nie ma aktywnego profilu.":["There is no active profile.","Нет активного профиля.","Немає активного профілю.","No hay un perfil activo.","Aucun profil actif.","Kein aktives Profil vorhanden."],
"Nie znaleziono tego profilu.":["This profile was not found.","Профиль не найден.","Профіль не знайдено.","No se encontró este perfil.","Profil introuvable.","Profil nicht gefunden."],
"Nie udało się znaleźć ofert na tej stronie albo Pracuj.pl zablokował automatyczny odczyt. Spróbuj innego zapytania później.":["No jobs were found on this page, or Pracuj.pl blocked automatic access. Try another query later.","Вакансии не найдены или Pracuj.pl заблокировал автоматическое чтение. Попробуйте позже другой запрос.","Вакансій не знайдено або Pracuj.pl заблокував автоматичне читання. Спробуйте інший запит пізніше.","No se encontraron ofertas o Pracuj.pl bloqueó el acceso automático. Prueba otra búsqueda más tarde.","Aucune offre trouvée ou Pracuj.pl a bloqué l’accès automatique. Réessayez plus tard.","Keine Stellen gefunden oder Pracuj.pl blockiert den automatischen Zugriff. Versuche später eine andere Suche."],
"Nie ma już ofert na tej stronie wyników.":["There are no more jobs on this results page.","На этой странице больше нет вакансий.","На цій сторінці більше немає вакансій.","No hay más ofertas en esta página.","Il n’y a plus d’offres sur cette page.","Keine weiteren Stellen auf dieser Ergebnisseite."],
"Najpierw zapisz aktywny profil poleceniem /analyze.":["First create an active profile with /analyze.","Сначала создайте активный профиль командой /analyze.","Спочатку створіть активний профіль командою /analyze.","Primero crea un perfil activo con /analyze.","Créez d’abord un profil actif avec /analyze.","Erstelle zuerst mit /analyze ein aktives Profil."],
"Nie wybrano jeszcze ofert. Użyj /jobs, aby wyszukać i zaznaczyć oferty.":["No jobs selected yet. Use /jobs to search and select jobs.","Вакансии ещё не выбраны. Используйте /jobs, чтобы найти и выбрать их.","Вакансії ще не вибрано. Скористайтеся /jobs, щоб знайти й обрати їх.","Aún no hay ofertas seleccionadas. Usa /jobs para buscarlas y seleccionarlas.","Aucune offre sélectionnée. Utilisez /jobs pour rechercher et sélectionner des offres.","Noch keine Stellen ausgewählt. Verwende /jobs zum Suchen und Auswählen."],
"Nie wybrano ofert. Najpierw zaznacz je w wynikach /jobs.":["No jobs selected. Select them in the /jobs results first.","Вакансии не выбраны. Сначала отметьте их в результатах /jobs.","Вакансії не обрано. Спочатку позначте їх у результатах /jobs.","No hay ofertas seleccionadas. Selecciónalas primero en /jobs.","Aucune offre sélectionnée. Sélectionnez-en d’abord dans /jobs.","Keine Stellen ausgewählt. Wähle zuerst Stellen in /jobs aus."],
"Nie ma aktywnego profilu kandydata. Najpierw przeanalizuj i zatwierdź CV.":["There is no active candidate profile. Analyze and approve a CV first.","Нет активного профиля кандидата. Сначала проанализируйте и подтвердите CV.","Немає активного профілю кандидата. Спочатку проаналізуйте й підтвердьте CV.","No hay perfil de candidato activo. Primero analiza y aprueba un CV.","Aucun profil candidat actif. Analysez et validez d’abord un CV.","Kein aktives Kandidatenprofil. Analysiere zuerst einen Lebenslauf und bestätige ihn."],
"Wyślij tekstowe informacje do dopisania albo /cancel.":["Send the information to add, or use /cancel.","Отправьте сведения для добавления или используйте /cancel.","Надішліть відомості для доповнення або скористайтеся /cancel.","Envía la información que quieres añadir o usa /cancel.","Envoyez les informations à ajouter ou utilisez /cancel.","Sende die Angaben zum Ergänzen oder nutze /cancel."],
"Nie rozpoznałem oczekiwanej odpowiedzi. Użyj /start, aby zobaczyć dostępne polecenia.":["I couldn't identify the expected response. Use /start to see available commands.","Не удалось распознать ответ. Используйте /start, чтобы увидеть команды.","Не вдалося розпізнати відповідь. Скористайтеся /start, щоб побачити команди.","No reconocí la respuesta esperada. Usa /start para ver los comandos.","Je n’ai pas reconnu la réponse attendue. Utilisez /start pour afficher les commandes.","Antwort nicht erkannt. Verwende /start, um die Befehle anzuzeigen."],
"Ta oferta nie znajduje się już w wynikach. Uruchom /jobs ponownie.":["This job is no longer in the results. Run /jobs again.","Этой вакансии больше нет в результатах. Запустите /jobs ещё раз.","Цієї вакансії більше немає в результатах. Запустіть /jobs ще раз.","Esta oferta ya no está en los resultados. Ejecuta /jobs de nuevo.","Cette offre n’est plus dans les résultats. Relancez /jobs.","Diese Stelle ist nicht mehr in den Ergebnissen. Starte /jobs erneut."],
"Ta oferta nie znajduje się na liście wybranych. Użyj /selected, aby sprawdzić wybór.":["This job isn't selected. Use /selected to review your selection.","Эта вакансия не выбрана. Проверьте список с помощью /selected.","Цю вакансію не обрано. Перевірте список за допомогою /selected.","Esta oferta no está seleccionada. Usa /selected para revisar tu selección.","Cette offre n’est pas sélectionnée. Vérifiez avec /selected.","Diese Stelle ist nicht ausgewählt. Prüfe die Auswahl mit /selected."],
"Nie udało się przetłumaczyć profilu. Oryginalna wersja pozostała bez zmian.":["Couldn't translate the profile. The original version remains unchanged.","Не удалось перевести профиль. Исходная версия не изменена.","Не вдалося перекласти профіль. Початкова версія не змінилася.","No se pudo traducir el perfil. La versión original sigue igual.","Impossible de traduire le profil. La version originale reste inchangée.","Das Profil konnte nicht übersetzt werden. Die Originalversion bleibt unverändert."],
"Zapisane profile. Wybierz CV, którego profil ma być aktywny:":["Saved profiles. Choose which CV profile to activate:","Сохранённые профили. Выберите профиль CV для активации:","Збережені профілі. Виберіть профіль CV для активації:","Perfiles guardados. Elige el perfil CV que quieres activar:","Profils enregistrés. Choisissez le profil CV à activer :","Gespeicherte Profile. Wähle das zu aktivierende CV-Profil:"],
"Oryginalny plik CV pozostanie lokalnie. Usunąć zapisany profil?":["The original CV file stays local. Delete the saved profile?","Исходный файл CV останется локально. Удалить сохранённый профиль?","Початковий файл CV залишиться локально. Видалити збережений профіль?","El CV original seguirá local. ¿Eliminar el perfil guardado?","Le CV original reste en local. Supprimer le profil enregistré ?","Die Originaldatei bleibt lokal. Gespeichertes Profil löschen?"],
"Nie udało się pobrać lub ocenić ofert. Zakończyłem wyszukiwanie błędem; sprawdź połączenie i spróbuj ponownie.":["Couldn't retrieve or assess jobs. Check your connection and try again.","Не удалось загрузить или оценить вакансии. Проверьте подключение и попробуйте снова.","Не вдалося завантажити або оцінити вакансії. Перевірте з’єднання та спробуйте знову.","No se pudieron obtener o evaluar las ofertas. Comprueba la conexión e inténtalo de nuevo.","Impossible de récupérer ou d’évaluer les offres. Vérifiez votre connexion et réessayez.","Stellen konnten nicht geladen oder bewertet werden. Prüfe die Verbindung und versuche es erneut."],
"Anulowano oczekującą operację. Zapisany oryginał CV pozostał na komputerze.":["Pending operation cancelled. The original CV remains on this computer.","Операция отменена. Исходное CV осталось на этом компьютере.","Операцію скасовано. Початкове CV залишилося на цьому комп’ютері.","Operación cancelada. El CV original sigue en este equipo.","Opération annulée. Le CV original reste sur cet ordinateur.","Vorgang abgebrochen. Der ursprüngliche Lebenslauf bleibt auf diesem Computer."],
"Gotowe. Zakończyłem sprawdzanie wybranych formularzy; wysyłam podsumowanie.":["Done. I finished checking the selected forms; sending the summary.","Готово. Проверка выбранных форм завершена; отправляю сводку.","Готово. Перевірку обраних форм завершено; надсилаю підсумок.","Listo. Terminé de revisar los formularios; envío el resumen.","Terminé. La vérification des formulaires est achevée ; envoi du résumé.","Fertig. Die ausgewählten Formulare wurden geprüft; die Zusammenfassung wird gesendet."],
}
for _source, _values in _FINAL_COPY.items():
    UI_PHRASES[_source] = dict(zip(("en","ru","uk","es","fr","de"), _values))


_REMAINING = {
"Aby przygotować profil, wyodrębnię tekst z najnowszego lokalnego CV i przekażę go do OpenAI API. Profil pokażę Ci do sprawdzenia, a zapiszę dopiero po zatwierdzeniu. Czy wyrażasz zgodę na wysłanie tekstu tego CV do OpenAI?":["To prepare a profile, I'll extract the text from your latest local CV and send it to the OpenAI API. I'll show you the profile and save it only after approval. Do you consent to sending this CV text to OpenAI?","Чтобы подготовить профиль, я извлеку текст из последнего локального CV и отправлю его в OpenAI API. Сначала покажу профиль и сохраню только после подтверждения. Вы согласны отправить текст CV в OpenAI?","Щоб підготувати профіль, я витягну текст з останнього локального CV і надішлю його до OpenAI API. Спочатку покажу профіль і збережу лише після підтвердження. Ви погоджуєтеся на надсилання тексту CV до OpenAI?","Para preparar el perfil, extraeré el texto del CV local más reciente y lo enviaré a la API de OpenAI. Te mostraré el perfil y solo lo guardaré tras tu aprobación. ¿Aceptas enviar el texto del CV a OpenAI?","Pour préparer le profil, j’extrairai le texte du CV local le plus récent et l’enverrai à l’API OpenAI. Je vous montrerai le profil et ne l’enregistrerai qu’après validation. Acceptez-vous l’envoi du texte du CV à OpenAI ?","Zur Profilerstellung extrahiere ich den Text aus dem neuesten lokalen Lebenslauf und sende ihn an die OpenAI-API. Ich zeige dir das Profil und speichere es erst nach deiner Freigabe. Stimmst du dem Senden des CV-Texts an OpenAI zu?"],
"Usunę zapisany profil kandydata. Oryginalny plik CV pozostanie lokalnie i będzie można ponownie go przeanalizować. Potwierdzasz?":["I will delete the saved candidate profile. The original CV file will remain local and can be analyzed again. Do you confirm?","Я удалю сохранённый профиль кандидата. Исходный файл CV останется локально, и его можно будет проанализировать снова. Подтверждаете?","Я видалю збережений профіль кандидата. Початковий файл CV залишиться локально, і його можна буде проаналізувати знову. Підтверджуєте?","Eliminaré el perfil guardado. El CV original seguirá local y podrá analizarse de nuevo. ¿Confirmas?","Je vais supprimer le profil candidat enregistré. Le CV original restera en local et pourra être analysé à nouveau. Confirmez-vous ?","Ich lösche das gespeicherte Kandidatenprofil. Der ursprüngliche Lebenslauf bleibt lokal und kann erneut analysiert werden. Bestätigst du?"],
"Dopisano i zapisano informacje lokalnie. Tłumaczenia profilu wymagają odświeżenia; użyj /translate en, /translate ru lub /translate uk.":["Information added and saved locally. Profile translations need refreshing; use /translate en, /translate ru or /translate uk.","Информация добавлена и сохранена локально. Переводы профиля нужно обновить: используйте /translate en, /translate ru или /translate uk.","Інформацію додано й збережено локально. Переклади профілю потрібно оновити: скористайтеся /translate en, /translate ru або /translate uk.","Información añadida y guardada localmente. Actualiza las traducciones con /translate en, /translate ru o /translate uk.","Informations ajoutées et enregistrées localement. Actualisez les traductions avec /translate en, /translate ru ou /translate uk.","Angaben hinzugefügt und lokal gespeichert. Profilübersetzungen müssen aktualisiert werden: /translate en, /translate ru oder /translate uk."],
"Napisz dodatkowe informacje, których brakuje w profilu. Zapiszę je lokalnie. /cancel anuluje.":["Send the additional information missing from your profile. It will be saved locally. Use /cancel to stop.","Напишите, каких сведений не хватает в профиле. Они будут сохранены локально. Для отмены используйте /cancel.","Надішліть додаткові відомості, яких бракує у профілі. Їх буде збережено локально. Для скасування скористайтеся /cancel.","Escribe la información que falta en el perfil. Se guardará localmente. Usa /cancel para cancelar.","Indiquez les informations manquantes dans le profil. Elles seront enregistrées localement. Utilisez /cancel pour annuler.","Sende die fehlenden Profilangaben. Sie werden lokal gespeichert. Mit /cancel abbrechen."],
"Anulowano. CV pozostało zapisane lokalnie i nie zostało wysłane do OpenAI.":["Cancelled. The CV remains saved locally and was not sent to OpenAI.","Отменено. CV осталось сохранённым локально и не отправлялось в OpenAI.","Скасовано. CV залишилося збереженим локально й не надсилалося до OpenAI.","Cancelado. El CV sigue guardado localmente y no se envió a OpenAI.","Annulé. Le CV reste enregistré localement et n’a pas été envoyé à OpenAI.","Abgebrochen. Der Lebenslauf bleibt lokal gespeichert und wurde nicht an OpenAI gesendet."],
"Odebrałem zgodę. Odczytuję CV i przygotowuję profil; będę informować, jeśli analiza potrwa dłużej.":["Consent received. I'm reading the CV and preparing the profile; I'll let you know if the analysis takes longer.","Согласие получено. Читаю CV и готовлю профиль; если анализ затянется, сообщу.","Згоду отримано. Читаю CV та готую профіль; якщо аналіз затягнеться, повідомлю.","Consentimiento recibido. Leo el CV y preparo el perfil; te avisaré si el análisis tarda.","Consentement reçu. Je lis le CV et prépare le profil ; je vous informerai si l’analyse prend du temps.","Einwilligung erhalten. Ich lese den Lebenslauf und erstelle das Profil; bei längerer Analyse informiere ich dich."],
"Analiza CV zakończona. Przygotowałem roboczy profil do Twojej weryfikacji.":["CV analysis complete. A draft profile is ready for your review.","Анализ CV завершён. Черновик профиля готов к проверке.","Аналіз CV завершено. Чернетка профілю готова до перевірки.","Análisis del CV terminado. El borrador está listo para revisarlo.","Analyse du CV terminée. Le brouillon est prêt à être vérifié.","CV-Analyse abgeschlossen. Der Entwurf kann geprüft werden."],
"Profil zapisany lokalnie. Przygotowuję automatyczne wersje EN, RU i UK…":["Profile saved locally. Preparing automatic EN, RU and UK versions…","Профиль сохранён локально. Готовлю автоматические версии EN, RU и UK…","Профіль збережено локально. Готую автоматичні версії EN, RU та UK…","Perfil guardado localmente. Preparando versiones automáticas EN, RU y UK…","Profil enregistré localement. Préparation des versions automatiques EN, RU et UK…","Profil lokal gespeichert. Automatische Versionen EN, RU und UK werden erstellt…"],
"Nie mogę znaleźć tego CV. Wyślij plik ponownie.":["I can't find this CV. Send the file again.","Не могу найти это CV. Отправьте файл ещё раз.","Не можу знайти це CV. Надішліть файл ще раз.","No encuentro este CV. Vuelve a enviar el archivo.","Impossible de trouver ce CV. Renvoyez le fichier.","Dieses CV wurde nicht gefunden. Bitte erneut senden."],
"Brak lokalnego OPENAI_API_KEY w .env. Nie wysłano CV.":["The local OPENAI_API_KEY is missing from .env. The CV was not sent.","В локальном .env отсутствует OPENAI_API_KEY. CV не отправлено.","У локальному .env немає OPENAI_API_KEY. CV не надіслано.","Falta OPENAI_API_KEY en el .env local. No se envió el CV.","OPENAI_API_KEY manque dans le .env local. Le CV n’a pas été envoyé.","OPENAI_API_KEY fehlt in der lokalen .env. Das CV wurde nicht gesendet."],
"Nie ma roboczego profilu do zapisania. Wyślij /analyze, aby przygotować go ponownie.":["There is no draft profile to save. Use /analyze to prepare it again.","Нет черновика профиля для сохранения. Запустите /analyze, чтобы подготовить его снова.","Немає чернетки профілю для збереження. Запустіть /analyze, щоб підготувати її знову.","No hay borrador para guardar. Usa /analyze para prepararlo de nuevo.","Aucun brouillon à enregistrer. Utilisez /analyze pour le recréer.","Kein Profilentwurf zum Speichern. Erstelle ihn erneut mit /analyze."],
"Nie udało się przygotować profilu. Treść CV nie została zapisana w profilu. Jeśli to skan PDF, ta wersja nie ma jeszcze OCR.":["Couldn't prepare the profile. CV content wasn't saved. Scanned PDFs aren't supported by OCR yet.","Не удалось подготовить профиль. Данные CV не сохранены. Для сканированных PDF пока нет OCR.","Не вдалося підготувати профіль. Дані CV не збережено. Для сканованих PDF OCR поки не підтримується.","No se pudo preparar el perfil. El CV no se guardó. Aún no hay OCR para PDF escaneados.","Impossible de préparer le profil. Le contenu du CV n’a pas été enregistré. L’OCR des PDF numérisés n’est pas encore disponible.","Profil konnte nicht erstellt werden. CV-Inhalt wurde nicht gespeichert. Für gescannte PDFs gibt es noch keine OCR."],
}
for _src,_vals in _REMAINING.items():
    UI_PHRASES[_src]=dict(zip(("en","ru","uk","es","fr","de"),_vals))


_DYNAMIC_COPY = {
"Znaleziono zapisany wynik wyszukiwania (":["Found cached search results (","Найдены сохранённые результаты поиска (","Знайдено збережені результати пошуку (","Se encontraron resultados guardados (","Résultats de recherche enregistrés trouvés (","Gespeicherte Suchergebnisse gefunden ("],
" ofert); pomijam ponowne pobieranie i ocenę.":[" jobs); skipping retrieval and reassessment."," вакансий); повторная загрузка и оценка пропущены."," вакансій); повторне завантаження й оцінювання пропущено."," ofertas); se omiten la descarga y la evaluación."," offres) ; téléchargement et nouvelle évaluation ignorés."," Stellen); erneutes Laden und Bewerten wird übersprungen."],
"Pobrano ":[ "Retrieved ", "Загружено ", "Завантажено ", "Obtenidas ", "Récupéré ", "Geladen: "],
" ofert (":[" jobs ("," вакансий ("," вакансій ("," ofertas ("," offres ("," Stellen ("],
"). Teraz oceniam dopasowanie do profilu…":["). Now assessing matches to your profile…","). Теперь оцениваю соответствие профилю…","). Тепер оцінюю відповідність профілю…","). Ahora evalúo la coincidencia con tu perfil…","). Évaluation de la correspondance avec le profil…","). Passung zum Profil wird bewertet…"],
"Gotowe: pobrano ":[ "Done: retrieved ", "Готово: загружено ", "Готово: завантажено ", "Listo: obtenidas ", "Terminé : récupéré ", "Fertig: geladen "],
" ofert i oceniono ":[ " jobs and assessed ", " вакансий, оценено ", " вакансій, оцінено ", " ofertas y evaluadas ", " offres, évaluées ", " Stellen, bewertet "],
"). Wysyłam wyniki…":["). Sending results…","). Отправляю результаты…","). Надсилаю результати…","). Enviando resultados…","). Envoi des résultats…","). Ergebnisse werden gesendet…"],
"Pokazano ":[ "Showing ", "Показано ", "Показано ", "Mostrando ", "Affichage de ", "Angezeigt: "],
"–":[ "–", "–", "–", "–", "–", "–"],
" z ":[ " of ", " из ", " з ", " de ", " sur ", " von "],
" ofert pobranych z tej strony. Użyj przycisku, aby zobaczyć dalsze pozycje.":[" jobs retrieved from this page. Use the button to see more."," вакансий загружено с этой страницы. Нажмите кнопку, чтобы увидеть следующие."," вакансій завантажено з цієї сторінки. Натисніть кнопку, щоб переглянути далі."," ofertas obtenidas en esta página. Usa el botón para ver más."," offres récupérées sur cette page. Utilisez le bouton pour en voir davantage."," Stellen von dieser Seite geladen. Nutze die Schaltfläche für weitere Ergebnisse."],
" ofert z bieżącej strony. Możesz przejść do kolejnej strony wyników.":[" jobs from the current page. You can open the next results page."," вакансий на текущей странице. Можно перейти к следующей странице."," вакансій на поточній сторінці. Можна перейти до наступної сторінки."," ofertas de la página actual. Puedes pasar a la página siguiente."," offres sur la page actuelle. Vous pouvez passer à la page suivante."," Stellen auf der aktuellen Seite. Du kannst zur nächsten Ergebnisseite wechseln."],
" ofert pobranych z tej strony Pracuj.pl.":[" jobs retrieved from this Pracuj.pl page."," вакансий загружено с этой страницы Pracuj.pl."," вакансій завантажено з цієї сторінки Pracuj.pl."," ofertas obtenidas de esta página de Pracuj.pl."," offres récupérées sur cette page Pracuj.pl."," Stellen von dieser Pracuj.pl-Seite geladen."],
"Użyj /apply, aby bot sprawdził formularze wszystkich wybranych ofert. Możesz wskazać jedną ofertę: /apply ID_OFERTY.":["Use /apply to have the bot review forms for all selected jobs. To review one job: /apply JOB_ID.","Используйте /apply, чтобы проверить формы всех выбранных вакансий. Для одной вакансии: /apply ID_OFERTY.","Скористайтеся /apply, щоб перевірити форми всіх обраних вакансій. Для однієї: /apply ID_ВАКАНСІЇ.","Usa /apply para revisar los formularios de todas las ofertas seleccionadas. Para una: /apply ID_OFERTA.","Utilisez /apply pour vérifier les formulaires de toutes les offres sélectionnées. Pour une seule : /apply ID_OFFRE.","Mit /apply prüft der Bot alle ausgewählten Formulare. Für eine Stelle: /apply JOB_ID."],
"Sprawdzam formularz ":[ "Checking application form ", "Проверяю форму заявки ", "Перевіряю форму заявки ", "Revisando el formulario ", "Vérification du formulaire ", "Bewerbungsformular wird geprüft: "],
"Odczytuję formularz ":[ "Reading form ", "Читаю форму ", "Читаю форму ", "Leyendo el formulario ", "Lecture du formulaire ", "Formular wird gelesen: "],
"Przygotowuję odpowiedzi ":[ "Preparing answers ", "Готовлю ответы ", "Готую відповіді ", "Preparando respuestas ", "Préparation des réponses ", "Antworten werden vorbereitet: "],
"Status: nie udało się odczytać pól formularza automatycznie.":["Status: couldn't read form fields automatically.","Статус: не удалось автоматически прочитать поля формы.","Статус: не вдалося автоматично прочитати поля форми.","Estado: no se pudieron leer automáticamente los campos.","État : impossible de lire automatiquement les champs du formulaire.","Status: Formularfelder konnten nicht automatisch gelesen werden."],
"Formularz nie jest publicznie dostępny.":["The form is not publicly accessible.","Форма недоступна публично.","Форма недоступна публічно.","El formulario no es accesible públicamente.","Le formulaire n’est pas accessible publiquement.","Das Formular ist nicht öffentlich zugänglich."],
"Zewnętrzna strona aplikacji: ":[ "External application page: ", "Внешняя страница заявки: ", "Зовнішня сторінка заявки: ", "Página externa de solicitud: ", "Page externe de candidature : ", "Externe Bewerbungsseite: "],
"Pola zostały odczytane, ale przygotowanie odpowiedzi nie powiodło się.":["Fields were read, but answer preparation failed.","Поля прочитаны, но подготовить ответы не удалось.","Поля прочитано, але підготувати відповіді не вдалося.","Se leyeron los campos, pero no se pudieron preparar las respuestas.","Les champs ont été lus, mais la préparation des réponses a échoué.","Die Felder wurden gelesen, aber die Antworten konnten nicht vorbereitet werden."],
"Sprawdź przygotowane treści i samodzielnie wyślij aplikacje. Bot nie loguje się na konto i nie wysyła formularzy.":["Review the prepared content and submit the applications yourself. The bot does not sign in or submit forms.","Проверьте подготовленные тексты и отправьте заявки самостоятельно. Бот не входит в аккаунты и не отправляет формы.","Перевірте підготовлені тексти й надішліть заявки самостійно. Бот не входить в облікові записи й не надсилає форми.","Revisa el contenido y envía las solicitudes tú mismo. El bot no inicia sesión ni envía formularios.","Vérifiez les textes préparés et envoyez vous-même les candidatures. Le bot ne se connecte pas et ne soumet aucun formulaire.","Prüfe die vorbereiteten Texte und sende Bewerbungen selbst. Der Bot meldet sich nicht an und übermittelt keine Formulare."],
"Oferta została dodana do wybranych. Zobacz listę przez /selected.":["Job added to your selection. View it with /selected.","Вакансия добавлена в выбранные. Список: /selected.","Вакансію додано до обраних. Перегляньте список: /selected.","Oferta añadida. Consulta la lista con /selected.","Offre ajoutée. Consultez la liste avec /selected.","Stelle ausgewählt. Liste mit /selected anzeigen."],
"Usunięto ofertę z wybranych.":["Job removed from your selection.","Вакансия удалена из выбранных.","Вакансію вилучено з обраних.","Oferta eliminada de la selección.","Offre retirée de la sélection.","Stelle aus der Auswahl entfernt."],
"Wybrane oferty:":["Selected jobs:","Выбранные вакансии:","Обрані вакансії:","Ofertas seleccionadas:","Offres sélectionnées :","Ausgewählte Stellen:"],
"Sprawdzam formularze ":[ "Checking forms for ", "Проверяю формы для ", "Перевіряю форми для ", "Revisando formularios de ", "Vérification des formulaires pour ", "Formulare werden geprüft: "],
" wybranych ofert; przygotuję odpowiedzi do skopiowania.":[" selected jobs; I'll prepare answers for you to copy."," выбранных вакансий; подготовлю ответы для копирования."," обраних вакансій; підготую відповіді для копіювання."," ofertas seleccionadas; prepararé respuestas para copiar."," offres sélectionnées ; je préparerai des réponses à copier."," ausgewählte Stellen; Antworten zum Kopieren werden vorbereitet."],
"Polecenie zostało odebrane. ":[ "Request received. ", "Команда получена. ", "Команду отримано. ", "Solicitud recibida. ", "Demande reçue. ", "Auftrag erhalten. "],
}
for _src,_vals in _DYNAMIC_COPY.items():
    UI_PHRASES[_src]=dict(zip(("en","ru","uk","es","fr","de"),_vals))


UI_PHRASES.update({
"Tak, przekaż CV do OpenAI":{"en":"Yes, send the CV to OpenAI","ru":"Да, отправить CV в OpenAI","uk":"Так, надіслати CV до OpenAI","es":"Sí, enviar el CV a OpenAI","fr":"Oui, envoyer le CV à OpenAI","de":"Ja, Lebenslauf an OpenAI senden"},
"Anuluj":{"en":"Cancel","ru":"Отмена","uk":"Скасувати","es":"Cancelar","fr":"Annuler","de":"Abbrechen"},
"Zatwierdź i zapisz":{"en":"Approve and save","ru":"Подтвердить и сохранить","uk":"Підтвердити й зберегти","es":"Aprobar y guardar","fr":"Valider et enregistrer","de":"Bestätigen und speichern"},
"Odrzuć":{"en":"Reject","ru":"Отклонить","uk":"Відхилити","es":"Rechazar","fr":"Refuser","de":"Ablehnen"},
"Usuń profil":{"en":"Delete profile","ru":"Удалить профиль","uk":"Видалити профіль","es":"Eliminar perfil","fr":"Supprimer le profil","de":"Profil löschen"},
"Uzupełnij profil":{"en":"Complete profile","ru":"Дополнить профиль","uk":"Доповнити профіль","es":"Completar perfil","fr":"Compléter le profil","de":"Profil ergänzen"},
"Usuń aktywny profil":{"en":"Delete active profile","ru":"Удалить активный профиль","uk":"Видалити активний профіль","es":"Eliminar perfil activo","fr":"Supprimer le profil actif","de":"Aktives Profil löschen"},
"Usuń z wybranych":{"en":"Remove from selected","ru":"Убрать из выбранных","uk":"Вилучити з обраних","es":"Quitar de seleccionadas","fr":"Retirer de la sélection","de":"Aus Auswahl entfernen"},
"Wybieram tę ofertę":{"en":"Select this job","ru":"Выбрать вакансию","uk":"Обрати вакансію","es":"Elegir esta oferta","fr":"Choisir cette offre","de":"Diese Stelle auswählen"},
"Następne oferty":{"en":"More jobs","ru":"Следующие вакансии","uk":"Наступні вакансії","es":"Más ofertas","fr":"Offres suivantes","de":"Weitere Stellen"},
"Następna strona Pracuj.pl":{"en":"Next Pracuj.pl page","ru":"Следующая страница Pracuj.pl","uk":"Наступна сторінка Pracuj.pl","es":"Página siguiente de Pracuj.pl","fr":"Page suivante de Pracuj.pl","de":"Nächste Pracuj.pl-Seite"},
})


UI_PHRASES.update({
"Odebrałem polecenie. Tłumaczę profil na język ":{"en":"Request received. Translating the profile into ","ru":"Команда получена. Перевожу профиль на ","uk":"Команду отримано. Перекладаю профіль мовою ","es":"Solicitud recibida. Traduciendo el perfil al ","fr":"Demande reçue. Traduction du profil en ","de":"Auftrag erhalten. Profil wird ins "}
,"Odebrałem polecenie. Sprawdzam formularze ":{"en":"Request received. Checking the forms for ","ru":"Команда получена. Проверяю формы для ","uk":"Команду отримано. Перевіряю форми для ","es":"Solicitud recibida. Revisando formularios de ","fr":"Demande reçue. Vérification des formulaires pour ","de":"Auftrag erhalten. Formulare werden geprüft für "}
," ofert; przygotuję odpowiedzi do skopiowania.":{"en":" selected jobs; I'll prepare answers for you to copy.","ru":" выбранных вакансий; подготовлю ответы для копирования.","uk":" обраних вакансій; підготую відповіді для копіювання.","es":" ofertas seleccionadas; prepararé respuestas para copiar.","fr":" offres sélectionnées ; je préparerai des réponses à copier.","de":" ausgewählte Stellen; Antworten zum Kopieren werden vorbereitet."}
," Nadal trwa (":{"en":" Still running (","ru":" Всё ещё выполняется (","uk":" Ще триває (","es":" Sigue en curso (","fr":" Toujours en cours (","de":" Läuft weiterhin ("}
,"Brak zapisanej wersji ":{"en":"No saved version for ","ru":"Нет сохранённой версии ","uk":"Немає збереженої версії ","es":"No hay versión guardada para ","fr":"Aucune version enregistrée pour ","de":"Keine gespeicherte Version für "}
,". Przygotowuję tłumaczenie…":{ "en":". Preparing the translation…","ru":". Готовлю перевод…","uk":". Готую переклад…","es":". Preparando la traducción…","fr":". Préparation de la traduction…","de":". Übersetzung wird vorbereitet…"}
,". Wszystkie wersje językowe pozostają zapisane równolegle w tym samym profilu.":{ "en":". All language versions remain saved together in the same profile.","ru":". Все языковые версии остаются сохранены вместе в одном профиле.","uk":". Усі мовні версії залишаються збереженими разом в одному профілі.","es":". Todas las versiones siguen guardadas juntas en el mismo perfil.","fr":". Toutes les versions restent enregistrées ensemble dans le même profil.","de":". Alle Sprachversionen bleiben gemeinsam in diesem Profil gespeichert."}
,". Użyj /profile, aby go wyświetlić.":{ "en":". Use /profile to view it.","ru":". Используйте /profile, чтобы посмотреть его.","uk":". Скористайтеся /profile, щоб переглянути його.","es":". Usa /profile para verlo.","fr":". Utilisez /profile pour l’afficher.","de":". Mit /profile anzeigen."}
,". Przygotowuję profil z OpenAI…":{ "en":". Preparing the profile with OpenAI…","ru":". Готовлю профиль с помощью OpenAI…","uk":". Готую профіль за допомогою OpenAI…","es":". Preparando el perfil con OpenAI…","fr":". Préparation du profil avec OpenAI…","de":". Profil wird mit OpenAI erstellt…"}
,". Teraz oceniam dopasowanie do profilu…":{ "en":". Now assessing matches to your profile…","ru":". Теперь оцениваю соответствие профилю…","uk":". Тепер оцінюю відповідність профілю…","es":". Ahora evalúo la coincidencia con tu perfil…","fr":". Évaluation de la correspondance avec le profil…","de":". Passung zum Profil wird bewertet…"}
,". Wysyłam wyniki…":{ "en":". Sending results…","ru":". Отправляю результаты…","uk":". Надсилаю результати…","es":". Enviando resultados…","fr":". Envoi des résultats…","de":". Ergebnisse werden gesendet…"}
,"Przygotowuję profil z OpenAI…":{"en":"Preparing a profile with OpenAI…","ru":"Готовлю профиль с помощью OpenAI…","uk":"Готую профіль за допомогою OpenAI…","es":"Preparando el perfil con OpenAI…","fr":"Préparation du profil avec OpenAI…","de":"Profil wird mit OpenAI erstellt…"}
,"Zapisuję przesłane CV lokalnie.":{"en":"Saving the uploaded CV locally.","ru":"Сохраняю полученное CV локально.","uk":"Зберігаю отримане CV локально.","es":"Guardando el CV localmente.","fr":"Enregistrement du CV en local.","de":"Hochgeladenes CV wird lokal gespeichert."}
,"Wyodrębniam tekst z CV.":{"en":"Extracting text from the CV.","ru":"Извлекаю текст из CV.","uk":"Витягую текст із CV.","es":"Extrayendo texto del CV.","fr":"Extraction du texte du CV.","de":"Text wird aus dem Lebenslauf extrahiert."}
,"Analizuję CV i składam profil z jego fragmentów.":{"en":"Analyzing the CV and assembling the profile from its sections.","ru":"Анализирую CV и собираю профиль из его частей.","uk":"Аналізую CV і складаю профіль з його частин.","es":"Analizando el CV y creando el perfil a partir de sus secciones.","fr":"Analyse du CV et création du profil à partir de ses sections.","de":"Lebenslauf wird analysiert und das Profil aus den Abschnitten erstellt."}
,"Pobieram oferty z Pracuj.pl.":{"en":"Retrieving jobs from Pracuj.pl.","ru":"Загружаю вакансии с Pracuj.pl.","uk":"Завантажую вакансії з Pracuj.pl.","es":"Obteniendo ofertas de Pracuj.pl.","fr":"Récupération des offres de Pracuj.pl.","de":"Stellen werden von Pracuj.pl geladen."}
,"Przygotowuję odpowiedzi do skopiowania.":{"en":"Preparing answers for you to copy.","ru":"Готовлю ответы для копирования.","uk":"Готую відповіді для копіювання.","es":"Preparando respuestas para copiar.","fr":"Préparation des réponses à copier.","de":"Antworten zum Kopieren werden vorbereitet."}
})


UI_PHRASES.pop("Oferta", None)
UI_PHRASES.update({
"Oceniam dopasowanie ":{ "en":"Assessing matches for ","ru":"Оцениваю соответствие для ","uk":"Оцінюю відповідність для ","es":"Evaluando la coincidencia de ","fr":"Évaluation de la correspondance pour ","de":"Passung wird bewertet für "},
"Zapisuję przesłane CV lokalnie.":{"en":"Saving the uploaded CV locally.","ru":"Сохраняю полученное CV локально.","uk":"Зберігаю отримане CV локально.","es":"Guardando el CV localmente.","fr":"Enregistrement du CV en local.","de":"Hochgeladenes CV wird lokal gespeichert."},
"Przygotowuję automatyczne wersje ":{ "en":"Preparing automatic versions ","ru":"Готовлю автоматические версии ","uk":"Готую автоматичні версії ","es":"Preparando versiones automáticas ","fr":"Préparation des versions automatiques ","de":"Automatische Versionen werden erstellt: "},
"Profil zapisany. Tłumaczę teraz wersję ":{ "en":"Profile saved. Translating version ","ru":"Профиль сохранён. Перевожу версию ","uk":"Профіль збережено. Перекладаю версію ","es":"Perfil guardado. Traduciendo la versión ","fr":"Profil enregistré. Traduction de la version ","de":"Profil gespeichert. Übersetze Version "},
"Wyświetlam wersję ":{ "en":"Showing version ","ru":"Показываю версию ","uk":"Показую версію ","es":"Mostrando la versión ","fr":"Affichage de la version ","de":"Angezeigte Version: "},
" profilu ":{ "en":" of profile ","ru":" профиля ","uk":" профілю ","es":" del perfil ","fr":" du profil ","de":" des Profils "},
" Profil ":{ "en":" Profile ","ru":" Профиль ","uk":" Профіль ","es":" Perfil ","fr":" Profil ","de":" Profil "},
" Wyświetlana wersja: ":{ "en":" Showing version: ","ru":" Показана версия: ","uk":" Показано версію: ","es":" Versión mostrada: ","fr":" Version affichée : ","de":" Angezeigte Version: "},
" Wszystkie wersje językowe są zapisane równolegle i należą do jednego profilu.":{ "en":" All language versions are stored together as one profile.","ru":" Все языковые версии сохранены вместе в одном профиле.","uk":" Усі мовні версії збережені разом в одному профілі.","es":" Todas las versiones se guardan juntas en un único perfil.","fr":" Toutes les versions sont conservées ensemble dans un seul profil.","de":" Alle Sprachversionen werden gemeinsam als ein Profil gespeichert."},
"Oferta nie znajduje się na liście wybranych. Użyj /selected, aby sprawdzić wybór.":{ "en":"Job isn't selected. Use /selected to review your selection.","ru":"Вакансия не выбрана. Проверьте список с помощью /selected.","uk":"Вакансію не обрано. Перевірте список за допомогою /selected.","es":"La oferta no está seleccionada. Usa /selected para revisar la lista.","fr":"L’offre n’est pas sélectionnée. Vérifiez avec /selected.","de":"Stelle nicht ausgewählt. Prüfe die Liste mit /selected."},
"Znaleziona":{ "en":"Found","ru":"Найдена","uk":"Знайдено","es":"Encontrada","fr":"Trouvée","de":"Gefunden"}
})


UI_PHRASES.update({
"Odczytano tekst CV (":{"en":"CV text extracted (","ru":"Извлечён текст CV (","uk":"Витягнуто текст CV (","es":"Texto del CV extraído (","fr":"Texte du CV extrait (","de":"CV-Text extrahiert ("},
" tego samego profilu.":{"en":" of the same profile.","ru":" этого же профиля.","uk":" цього самого профілю.","es":" del mismo perfil.","fr":" du même profil.","de":" desselben Profils."},
" s). Wysyłam wyniki…":{"en":" s). Sending results…","ru":" с). Отправляю результаты…","uk":" с). Надсилаю результати…","es":" s). Enviando resultados…","fr":" s). Envoi des résultats…","de":" s). Ergebnisse werden gesendet…"},
" znaków). Przygotowuję profil z OpenAI…":{"en":" characters). Preparing the profile with OpenAI…","ru":" знаков). Готовлю профиль с помощью OpenAI…","uk":" символів). Готую профіль за допомогою OpenAI…","es":" caracteres). Preparando el perfil con OpenAI…","fr":" caractères). Préparation du profil avec OpenAI…","de":" Zeichen). Profil wird mit OpenAI erstellt…"},
})

UI_PHRASES.update({
"Wyszukiwanie zakończone.": {"en":"Search complete.","ru":"Поиск завершён.","uk":"Пошук завершено.","es":"Búsqueda finalizada.","fr":"Recherche terminée.","de":"Suche abgeschlossen."},
"Sprawdzone oferty:": {"en":"Jobs reviewed:","ru":"Проверено вакансий:","uk":"Перевірено вакансій:","es":"Ofertas revisadas:","fr":"Offres vérifiées :","de":"Geprüfte Stellen:"},
"Oferty spełniające próg dopasowania 60%:": {"en":"Jobs meeting the 60% fit threshold:","ru":"Вакансий прошли порог соответствия 60%:","uk":"Вакансій пройшли поріг відповідності 60%:","es":"Ofertas que superan el umbral de compatibilidad del 60%:","fr":"Offres dépassant le seuil de correspondance de 60 % :","de":"Stellen über der 60-%-Passungsschwelle:"},
"Wysyłam tylko te oferty.": {"en":"Sending only those jobs.","ru":"Отправляю только эти вакансии.","uk":"Надсилаю лише ці вакансії.","es":"Enviando solo esas ofertas.","fr":"Envoi de ces seules offres.","de":"Nur diese Stellen werden gesendet."},
"Odebrałem wyszukiwanie. Wyszukuję stanowiska podobne do: ": {"en":"Search received. Finding roles similar to: ","ru":"Запрос получен. Ищу должности, похожие на: ","uk":"Запит отримано. Шукаю посади, подібні до: ","es":"Búsqueda recibida. Buscando puestos similares a: ","fr":"Recherche reçue. Recherche de postes similaires à : ","de":"Suche eingegangen. Suche nach ähnlichen Positionen wie: "},
"Przeszukuję wszystkie dostępne strony Pracuj.pl dla ról: ": {"en":"Scanning all available Pracuj.pl pages for roles: ","ru":"Проверяю все доступные страницы Pracuj.pl по должностям: ","uk":"Перевіряю всі доступні сторінки Pracuj.pl за посадами: ","es":"Revisando todas las páginas disponibles de Pracuj.pl para los puestos: ","fr":"Analyse de toutes les pages Pracuj.pl disponibles pour les postes : ","de":"Alle verfügbaren Pracuj.pl-Seiten für folgende Positionen werden durchsucht: "},
"Dopasowuję podobne nazwy stanowisk do profilu.": {"en":"Finding related job titles based on your profile.","ru":"Подбираю похожие названия должностей по профилю.","uk":"Добираю схожі назви посад за профілем.","es":"Buscando títulos de puestos relacionados según tu perfil.","fr":"Recherche de titres de postes similaires à partir du profil.","de":"Ähnliche Berufsbezeichnungen werden anhand deines Profils ermittelt."},
"Przeszukuję kolejne strony Pracuj.pl dla stanowisk z profilu.": {"en":"Scanning additional Pracuj.pl pages for roles from your profile.","ru":"Проверяю следующие страницы Pracuj.pl по должностям из профиля.","uk":"Перевіряю наступні сторінки Pracuj.pl за посадами з профілю.","es":"Revisando más páginas de Pracuj.pl para los puestos del perfil.","fr":"Analyse des pages Pracuj.pl suivantes pour les postes du profil.","de":"Weitere Pracuj.pl-Seiten für Positionen aus deinem Profil werden durchsucht."},
"Sprawdzam każdą względem profilu…": {"en":"Checking each against your profile…","ru":"Сверяю каждую вакансию с профилем…","uk":"Зіставляю кожну вакансію з профілем…","es":"Comparando cada oferta con tu perfil…","fr":"Comparaison de chaque offre avec votre profil…","de":"Jede Stelle wird mit deinem Profil abgeglichen…"},
"Gotowe: sprawdzono ": {"en":"Done: reviewed ","ru":"Готово: проверено ","uk":"Готово: перевірено ","es":"Listo: revisadas ","fr":"Terminé : ","de":"Fertig: geprüft "},
" ofert; ": {"en":" jobs; ","ru":" вакансий; ","uk":" вакансій; ","es":" ofertas; ","fr":" offres ; ","de":" Stellen; "},
" spełnia próg realnego dopasowania (60%). Wysyłam tylko te wyniki…": {"en":" meet the 60% real-fit threshold. Sending only those results…","ru":" прошли порог реального соответствия 60%. Отправляю только их…","uk":" пройшли поріг реальної відповідності 60%. Надсилаю лише їх…","es":" cumplen el umbral de compatibilidad real del 60%. Enviando solo esas ofertas…","fr":" atteignent le seuil de compatibilité réelle de 60 %. Envoi de ces seules offres…","de":" erfüllen die Schwelle von 60 % tatsächlicher Passung. Nur diese Ergebnisse werden gesendet…"},
"zebrano ": {"en":"collected ","ru":"собрано ","uk":"зібрано ","es":"recopiladas ","fr":"collectées ","de":"gesammelt "},
" unikalnych ofert ze wszystkich dostępnych stron (": {"en":" unique jobs from all available pages (","ru":" уникальных вакансий со всех доступных страниц (","uk":" унікальних вакансій з усіх доступних сторінок (","es":" ofertas únicas de todas las páginas disponibles (","fr":" offres uniques de toutes les pages disponibles (","de":" eindeutige Stellen von allen verfügbaren Seiten ("},
"). Sprawdzam każdą względem profilu…": {"en":"). Checking each against your profile…","ru":"). Сверяю каждую с профилем…","uk":"). Зіставляю кожну з профілем…","es":"). Comparando cada una con tu perfil…","fr":"). Comparaison avec votre profil…","de":"). Abgleich mit deinem Profil…"},
"Sprawdzono oferty z Pracuj.pl, ale żadna nie osiągnęła progu realnego dopasowania 60%. Zmień kryteria lub uzupełnij profil.": {"en":"Pracuj.pl jobs were reviewed, but none met the 60% real-fit threshold. Change the criteria or complete your profile.","ru":"Вакансии Pracuj.pl проверены, но ни одна не достигла порога реального соответствия 60%. Измените критерии или дополните профиль.","uk":"Вакансії Pracuj.pl перевірено, але жодна не досягла порога реальної відповідності 60%. Змініть критерії або доповніть профіль.","es":"Se revisaron las ofertas de Pracuj.pl, pero ninguna alcanzó el umbral de compatibilidad real del 60%. Cambia los criterios o completa tu perfil.","fr":"Les offres Pracuj.pl ont été vérifiées, mais aucune n’a atteint le seuil de compatibilité réelle de 60 %. Modifiez les critères ou complétez votre profil.","de":"Die Pracuj.pl-Stellen wurden geprüft, aber keine erreichte die Schwelle von 60 % tatsächlicher Passung. Ändere die Kriterien oder ergänze dein Profil."},
"Nie udało się znaleźć ofert na Pracuj.pl albo portal zablokował automatyczny odczyt. Spróbuj ponownie później.": {"en":"No Pracuj.pl jobs were found, or the portal blocked automatic access. Try again later.","ru":"Вакансии Pracuj.pl не найдены или портал заблокировал автоматическое чтение. Попробуйте позже.","uk":"Вакансії Pracuj.pl не знайдено або портал заблокував автоматичне читання. Спробуйте пізніше.","es":"No se encontraron ofertas en Pracuj.pl o el portal bloqueó el acceso automático. Inténtalo más tarde.","fr":"Aucune offre Pracuj.pl trouvée ou le portail a bloqué l’accès automatique. Réessayez plus tard.","de":"Keine Pracuj.pl-Stellen gefunden oder das Portal hat den automatischen Zugriff blockiert. Versuche es später erneut."},
"Nie mogę ustalić docelowych stanowisk z profilu. Uzupełnij nagłówek zawodowy lub doświadczenie albo podaj kryteria: /jobs stanowisko | lokalizacja.": {"en":"I can't determine target roles from your profile. Complete the professional headline or work history, or provide criteria: /jobs role | location.","ru":"Не удалось определить целевые должности по профилю. Заполните профессиональный заголовок или опыт работы либо укажите критерии: /jobs должность | город.","uk":"Не вдалося визначити цільові посади з профілю. Заповніть професійний заголовок або досвід роботи чи вкажіть критерії: /jobs посада | місто.","es":"No puedo determinar los puestos objetivo del perfil. Completa el titular profesional o la experiencia, o indica criterios: /jobs puesto | ubicación.","fr":"Impossible de déterminer les postes visés depuis le profil. Complétez le titre professionnel ou l’expérience, ou indiquez des critères : /jobs poste | lieu.","de":"Zielpositionen lassen sich aus dem Profil nicht bestimmen. Ergänze die Berufsbezeichnung oder Berufserfahrung oder gib Kriterien an: /jobs Rolle | Ort."},
"Dlaczego oferta pasuje: ": {"en":"Why this job fits: ","ru":"Почему вакансия подходит: ","uk":"Чому вакансія підходить: ","es":"Por qué encaja esta oferta: ","fr":"Pourquoi cette offre correspond : ","de":"Warum diese Stelle passt: "},
" ofert spełniających próg dopasowania.": {"en":" jobs meeting the fit threshold.","ru":" вакансий, прошедших порог соответствия.","uk":" вакансій, що пройшли поріг відповідності.","es":" ofertas que cumplen el umbral de compatibilidad.","fr":" offres répondant au seuil de correspondance.","de":" Stellen, die die Passungsschwelle erfüllen."},
"Gotowe: sprawdzono ": {"en":"Done: reviewed ","ru":"Готово: проверено ","uk":"Готово: перевірено ","es":"Listo: revisadas ","fr":"Terminé : ","de":"Fertig: geprüft "},
" ofert; ": {"en":" jobs; ","ru":" вакансий; ","uk":" вакансій; ","es":" ofertas; ","fr":" offres ; ","de":" Stellen; "},
" spełnia próg realnego dopasowania (60%). Wysyłam tylko te wyniki…": {"en":" meet the 60% real-fit threshold. Sending only those results…","ru":" прошли порог реального соответствия 60%. Отправляю только их…","uk":" пройшли поріг реальної відповідності 60%. Надсилаю лише їх…","es":" cumplen el umbral de compatibilidad real del 60%. Enviando solo esas ofertas…","fr":" atteignent le seuil de compatibilité réelle de 60 %. Envoi de ces seules offres…","de":" erfüllen die Schwelle von 60 % tatsächlicher Passung. Nur diese Ergebnisse werden gesendet…"},
"Zebrano ": {"en":"Collected ","ru":"Собрано ","uk":"Зібрано ","es":"Recopiladas ","fr":"Offres collectées : ","de":"Gesammelt: "},
" unikalnych ofert ze wszystkich dostępnych stron (": {"en":" unique jobs from all available pages (","ru":" уникальных вакансий со всех доступных страниц (","uk":" унікальних вакансій з усіх доступних сторінок (","es":" ofertas únicas de todas las páginas disponibles (","fr":" offres uniques sur toutes les pages disponibles (","de":" eindeutige Stellen von allen verfügbaren Seiten ("},
"). Sprawdzam każdą względem profilu…": {"en":"). Checking each against your profile…","ru":"). Сверяю каждую с профилем…","uk":"). Зіставляю кожну з профілем…","es":"). Comparando cada una con tu perfil…","fr":"). Comparaison avec votre profil…","de":"). Abgleich mit deinem Profil…"},
})

UI_PHRASES.update({
"Sprawdzono oferty z Pracuj.pl, ale żadna nie osiągnęła progu realnego dopasowania 60%. Zmień kryteria lub uzupełnij profil.": {"en":"Pracuj.pl jobs were reviewed, but none met the 60% real-fit threshold. Change the criteria or complete your profile.","ru":"Вакансии Pracuj.pl проверены, но ни одна не достигла порога реального соответствия 60%. Измените критерии или дополните профиль.","uk":"Вакансії Pracuj.pl перевірено, але жодна не досягла порога реальної відповідності 60%. Змініть критерії або доповніть профіль.","es":"Se revisaron las ofertas de Pracuj.pl, pero ninguna alcanzó el umbral de compatibilidad real del 60%. Cambia los criterios o completa tu perfil.","fr":"Les offres Pracuj.pl ont été vérifiées, mais aucune n’a atteint le seuil de compatibilité réelle de 60 %. Modifiez les critères ou complétez votre profil.","de":"Die Pracuj.pl-Stellen wurden geprüft, aber keine erreichte die Schwelle von 60 % tatsächlicher Passung. Ändere die Kriterien oder ergänze dein Profil."},
"Nie udało się znaleźć ofert na Pracuj.pl albo portal zablokował automatyczny odczyt. Spróbuj ponownie później.": {"en":"No Pracuj.pl jobs were found, or the portal blocked automatic access. Try again later.","ru":"Вакансии Pracuj.pl не найдены или портал заблокировал автоматическое чтение. Попробуйте позже.","uk":"Вакансії Pracuj.pl не знайдено або портал заблокував автоматичне читання. Спробуйте пізніше.","es":"No se encontraron ofertas en Pracuj.pl o el portal bloqueó el acceso automático. Inténtalo más tarde.","fr":"Aucune offre Pracuj.pl trouvée ou le portail a bloqué l’accès automatique. Réessayez plus tard.","de":"Keine Pracuj.pl-Stellen gefunden oder das Portal hat den automatischen Zugriff blockiert. Versuche es später erneut."},
"Nie mogę ustalić docelowych stanowisk z profilu. Uzupełnij nagłówek zawodowy lub doświadczenie albo podaj kryteria: /jobs stanowisko | lokalizacja.": {"en":"I can't determine target roles from your profile. Complete the professional headline or work history, or provide criteria: /jobs role | location.","ru":"Не удалось определить целевые должности по профилю. Заполните профессиональный заголовок или опыт работы либо укажите критерии: /jobs должность | город.","uk":"Не вдалося визначити цільові посади з профілю. Заповніть професійний заголовок або досвід роботи чи вкажіть критерії: /jobs посада | місто.","es":"No puedo determinar los puestos objetivo del perfil. Completa el titular profesional o la experiencia, o indica criterios: /jobs puesto | ubicación.","fr":"Impossible de déterminer les postes visés depuis le profil. Complétez le titre professionnel ou l’expérience, ou indiquez des critères : /jobs poste | lieu.","de":"Zielpositionen lassen sich aus dem Profil nicht bestimmen. Ergänze die Berufsbezeichnung oder Berufserfahrung oder gib Kriterien an: /jobs Rolle | Ort."},
"Znaleziono oferty, ale żadna nie przekroczyła progu dopasowania": {"en":"Jobs were found, but none met the fit threshold","ru":"Вакансии найдены, но ни одна не прошла порог соответствия","uk":"Вакансії знайдено, але жодна не пройшла поріг відповідності","es":"Se encontraron ofertas, pero ninguna superó el umbral de compatibilidad","fr":"Des offres ont été trouvées, mais aucune n’a atteint le seuil de correspondance","de":"Stellen gefunden, aber keine hat die Passungsschwelle erreicht"},
"Dlaczego oferta pasuje: ": {"en":"Why this job fits: ","ru":"Почему вакансия подходит: ","uk":"Чому вакансія підходить: ","es":"Por qué encaja esta oferta: ","fr":"Pourquoi cette offre correspond : ","de":"Warum diese Stelle passt: "},
" ofert spełniających próg dopasowania.": {"en":" jobs meeting the fit threshold.","ru":" вакансий, прошедших порог соответствия.","uk":" вакансій, що пройшли поріг відповідності.","es":" ofertas que cumplen el umbral de compatibilidad.","fr":" offres répondant au seuil de correspondance.","de":" Stellen, die die Passungsschwelle erfüllen."},
" sprawdzono ofert; ": {"en":" jobs reviewed; ","ru":" вакансий проверено; ","uk":" вакансій перевірено; ","es":" ofertas revisadas; ","fr":" offres vérifiées ; ","de":" Stellen geprüft; "},
" spełnia próg realnego dopasowania (60%). Wysyłam tylko te wyniki…": {"en":" meet the 60% real-fit threshold. Sending only those results…","ru":" прошли порог реального соответствия 60%. Отправляю только их…","uk":" пройшли поріг реальної відповідності 60%. Надсилаю лише їх…","es":" cumplen el umbral de compatibilidad real del 60%. Enviando solo esas ofertas…","fr":" atteignent le seuil de compatibilité réelle de 60 %. Envoi de ces seules offres…","de":" erfüllen die Schwelle von 60 % tatsächlicher Passung. Nur diese Ergebnisse werden gesendet…"},
})


# Complete translations for interface copy discovered during the UI audit.
UI_PHRASES.update({
    "Profil jest przechowywany i wyświetlany wyłącznie w oryginalnym języku CV.": {
        "en":"The profile is stored and displayed only in the original language of the CV.", "ru":"Профиль хранится и отображается только на исходном языке CV.", "uk":"Профіль зберігається та відображається лише мовою оригіналу CV.", "es":"El perfil se guarda y se muestra únicamente en el idioma original del CV.", "fr":"Le profil est enregistré et affiché uniquement dans la langue d’origine du CV.", "de":"Das Profil wird nur in der Originalsprache des Lebenslaufs gespeichert und angezeigt."},
    "Dopisano i zapisano informacje lokalnie w oryginalnym języku CV.": {
        "en":"The information was added and saved locally in the original language of the CV.", "ru":"Информация добавлена и сохранена локально на исходном языке CV.", "uk":"Інформацію додано й збережено локально мовою оригіналу CV.", "es":"La información se añadió y se guardó localmente en el idioma original del CV.", "fr":"Les informations ont été ajoutées et enregistrées localement dans la langue d’origine du CV.", "de":"Die Angaben wurden in der Originalsprache des Lebenslaufs ergänzt und lokal gespeichert."},
    "Wrócono do menu głównego.": {
        "en":"Returned to the main menu.", "ru":"Вы вернулись в главное меню.", "uk":"Повернулися до головного меню.", "es":"Has vuelto al menú principal.", "fr":"Retour au menu principal.", "de":"Zurück zum Hauptmenü."},
    "Profil jest przechowywany i wyświetlany w oryginalnym języku CV.": {
        "en":"The profile is stored and displayed in the original language of the CV.", "ru":"Профиль хранится и отображается на исходном языке CV.", "uk":"Профіль зберігається та відображається мовою оригіналу CV.", "es":"El perfil se guarda y se muestra en el idioma original del CV.", "fr":"Le profil est enregistré et affiché dans la langue d’origine du CV.", "de":"Das Profil wird in der Originalsprache des Lebenslaufs gespeichert und angezeigt."},
    "CV jest zapisane lokalnie. Po Twojej zgodzie prześlę jego treść do OpenAI i przygotuję roboczy profil.": {
        "en":"The CV is saved locally. With your consent, I’ll send its contents to OpenAI and prepare a draft profile.", "ru":"CV сохранено локально. С вашего согласия я отправлю его содержимое в OpenAI и подготовлю черновик профиля.", "uk":"CV збережено локально. За вашою згодою я надішлю його вміст до OpenAI та підготую чернетку профілю.", "es":"El CV está guardado localmente. Con tu consentimiento, enviaré su contenido a OpenAI y prepararé un borrador del perfil.", "fr":"Le CV est enregistré localement. Avec votre accord, j’enverrai son contenu à OpenAI et préparerai un brouillon du profil.", "de":"Der Lebenslauf ist lokal gespeichert. Mit deiner Zustimmung sende ich den Inhalt an OpenAI und erstelle einen Profilentwurf."},
    "Odrzucono profil. Nie zapisano go jako profilu kandydata.": {
        "en":"The profile was rejected and was not saved as a candidate profile.", "ru":"Профиль отклонён и не сохранён как профиль кандидата.", "uk":"Профіль відхилено й не збережено як профіль кандидата.", "es":"Se rechazó el perfil y no se guardó como perfil de candidato.", "fr":"Le profil a été refusé et n’a pas été enregistré comme profil candidat.", "de":"Das Profil wurde abgelehnt und nicht als Kandidatenprofil gespeichert."},
    "Profil zapisany lokalnie wyłącznie w oryginalnym języku CV.": {
        "en":"The profile was saved locally only in the original language of the CV.", "ru":"Профиль сохранён локально только на исходном языке CV.", "uk":"Профіль збережено локально лише мовою оригіналу CV.", "es":"El perfil se guardó localmente únicamente en el idioma original del CV.", "fr":"Le profil a été enregistré localement uniquement dans la langue d’origine du CV.", "de":"Das Profil wurde lokal nur in der Originalsprache des Lebenslaufs gespeichert."},
    "Zapisane CV. Wybierz profil do aktywacji lub CV do analizy.": {
        "en":"Saved CVs. Choose a profile to activate or a CV to analyze.", "ru":"Сохранённые CV. Выберите профиль для активации или CV для анализа.", "uk":"Збережені CV. Виберіть профіль для активації або CV для аналізу.", "es":"CV guardados. Elige un perfil para activar o un CV para analizar.", "fr":"CV enregistrés. Choisissez un profil à activer ou un CV à analyser.", "de":"Gespeicherte Lebensläufe. Wähle ein Profil zur Aktivierung oder einen Lebenslauf zur Analyse."},
    "Nie ma lokalnych CV. Wyślij plik PDF, DOCX lub TXT, aby dodać CV.": {
        "en":"There are no local CVs. Send a PDF, DOCX or TXT file to add one.", "ru":"Локальных CV нет. Отправьте файл PDF, DOCX или TXT, чтобы добавить CV.", "uk":"Локальних CV немає. Надішліть файл PDF, DOCX або TXT, щоб додати CV.", "es":"No hay CV locales. Envía un archivo PDF, DOCX o TXT para añadir uno.", "fr":"Aucun CV local. Envoyez un fichier PDF, DOCX ou TXT pour en ajouter un.", "de":"Keine lokalen Lebensläufe vorhanden. Sende eine PDF-, DOCX- oder TXT-Datei, um einen hinzuzufügen."},
    "Zapisane profile. Wybierz profil, który ma być aktywny.": {
        "en":"Saved profiles. Choose the profile to activate.", "ru":"Сохранённые профили. Выберите профиль для активации.", "uk":"Збережені профілі. Виберіть профіль для активації.", "es":"Perfiles guardados. Elige el perfil que quieres activar.", "fr":"Profils enregistrés. Choisissez le profil à activer.", "de":"Gespeicherte Profile. Wähle das Profil aus, das aktiviert werden soll."},
    "Nie ma zapisanego profilu. Możesz zarządzać zapisanymi CV lub wysłać nowe CV.": {
        "en":"No profile is saved. You can manage saved CVs or send a new one.", "ru":"Сохранённого профиля нет. Можно управлять сохранёнными CV или отправить новое.", "uk":"Збереженого профілю немає. Можна керувати збереженими CV або надіслати нове.", "es":"No hay un perfil guardado. Puedes gestionar los CV guardados o enviar uno nuevo.", "fr":"Aucun profil n’est enregistré. Vous pouvez gérer les CV enregistrés ou en envoyer un nouveau.", "de":"Es ist kein Profil gespeichert. Du kannst gespeicherte Lebensläufe verwalten oder einen neuen senden."},
    "Wybierz zapisane CV lub profil z listy:": {
        "en":"Choose a saved CV or profile from the list:", "ru":"Выберите сохранённое CV или профиль из списка:", "uk":"Виберіть збережене CV або профіль зі списку:", "es":"Elige un CV o perfil guardado de la lista:", "fr":"Choisissez un CV ou un profil enregistré dans la liste :", "de":"Wähle einen gespeicherten Lebenslauf oder ein Profil aus der Liste:"},
})


# Final audit additions: every launcher UI template has an explicit translation.
_UI_AUDIT_ADDITIONS = {
    "Nie można ustalić użytkownika Telegrama.": ["Could not identify the Telegram user.", "Не удалось определить пользователя Telegram.", "Не вдалося визначити користувача Telegram.", "No se pudo identificar al usuario de Telegram.", "Impossible d’identifier l’utilisateur Telegram.", "Der Telegram-Nutzer konnte nicht ermittelt werden."],
    "Nie udało się przeanalizować pól. Spróbuj ponownie.": ["The fields could not be analyzed. Please try again.", "Не удалось проанализировать поля. Попробуйте ещё раз.", "Не вдалося проаналізувати поля. Спробуйте ще раз.", "No se pudieron analizar los campos. Inténtalo de nuevo.", "Impossible d’analyser les champs. Réessayez.", "Die Felder konnten nicht analysiert werden. Bitte versuche es erneut."],
    "Nie widzę nazw pól. Wklej pytania z formularza, po jednym w wierszu, albo /cancel.": ["I can't see any field names. Paste the form questions, one per line, or use /cancel.", "Не вижу названий полей. Вставьте вопросы формы, по одному в строке, или используйте /cancel.", "Не бачу назв полів. Вставте запитання форми, по одному в рядку, або скористайтеся /cancel.", "No veo nombres de campos. Pega las preguntas, una por línea, o usa /cancel.", "Aucun nom de champ visible. Collez les questions, une par ligne, ou utilisez /cancel.", "Ich sehe keine Feldnamen. Füge die Fragen einzeln pro Zeile ein oder nutze /cancel."],
    "Nie wybrano ofert. Najpierw wybierz pasujące oferty w wynikach wyszukiwania.": ["No jobs selected. First select matching jobs from the search results.", "Вакансии не выбраны. Сначала выберите подходящие вакансии в результатах поиска.", "Вакансії не вибрано. Спочатку виберіть відповідні вакансії в результатах пошуку.", "No hay ofertas seleccionadas. Primero elige ofertas adecuadas en los resultados.", "Aucune offre sélectionnée. Choisissez d’abord les offres adaptées dans les résultats.", "Keine Stellen ausgewählt. Wähle zuerst passende Stellen aus den Suchergebnissen aus."],
    "Nie znaleziono aktywnego profilu lub wybranej oferty. Zacznij ponownie przez /selected.": ["The active profile or selected job wasn't found. Start again with /selected.", "Активный профиль или выбранная вакансия не найдены. Начните заново с /selected.", "Активний профіль або вибрану вакансію не знайдено. Почніть знову через /selected.", "No se encontró el perfil activo o la oferta elegida. Vuelve a empezar con /selected.", "Profil actif ou offre sélectionnée introuvable. Recommencez avec /selected.", "Aktives Profil oder ausgewählte Stelle nicht gefunden. Starte mit /selected erneut."],
    "Ta oferta nie jest na liście wybranych. Użyj /selected, aby sprawdzić wybór.": ["This job isn't selected. Use /selected to review your choices.", "Этой вакансии нет в выбранных. Проверьте список с помощью /selected.", "Цієї вакансії немає серед обраних. Перевірте вибір через /selected.", "Esta oferta no está seleccionada. Revisa la lista con /selected.", "Cette offre n’est pas sélectionnée. Vérifiez avec /selected.", "Diese Stelle ist nicht ausgewählt. Prüfe die Auswahl mit /selected."],
    "CV zapisane lokalnie. Jeśli klikniesz „Tak”, wyodrębnię tekst i przekażę go do OpenAI API, aby przygotować roboczy profil. Profil pokażę Ci do sprawdzenia; zapiszę go jako profil kandydata dopiero po Twoim zatwierdzeniu. Nie klikaj zgody, jeśli nie chcesz wysyłać treści CV do OpenAI.": ["CV saved locally. If you choose “Yes”, I will extract its text and send it to the OpenAI API to prepare a draft profile. You can review it; it will be saved as your candidate profile only after approval. Do not consent if you do not want the CV text sent to OpenAI.", "CV сохранено локально. Если выбрать «Да», я извлеку текст и отправлю его в OpenAI API для подготовки черновика профиля. Вы сможете проверить его; профиль сохранится только после подтверждения. Не соглашайтесь, если не хотите отправлять текст CV в OpenAI.", "CV збережено локально. Якщо вибрати «Так», я витягну текст і надішлю його до OpenAI API для підготовки чернетки профілю. Ви зможете перевірити її; профіль буде збережено лише після підтвердження. Не погоджуйтеся, якщо не хочете надсилати текст CV до OpenAI.", "CV guardado localmente. Si eliges «Sí», extraeré el texto y lo enviaré a la API de OpenAI para preparar un perfil provisional. Podrás revisarlo; solo se guardará tras tu aprobación. No des tu consentimiento si no quieres enviar el texto del CV a OpenAI.", "CV enregistré localement. Si vous choisissez « Oui », j’extrairai le texte et l’enverrai à l’API OpenAI pour préparer un profil provisoire. Vous pourrez le vérifier ; il ne sera enregistré qu’après votre accord. Ne consentez pas si vous ne souhaitez pas envoyer le CV à OpenAI.", "Der Lebenslauf wurde lokal gespeichert. Wenn du „Ja“ wählst, extrahiere ich den Text und sende ihn an die OpenAI-API, um einen Profilentwurf zu erstellen. Du kannst ihn prüfen; gespeichert wird das Profil erst nach deiner Bestätigung. Stimme nicht zu, wenn der CV-Text nicht an OpenAI gesendet werden soll."],
    "Aktywny język profilu: ": ["Active profile language: ", "Активный язык профиля: ", "Активна мова профілю: ", "Idioma del perfil activo: ", "Langue actuelle du profil : ", "Aktive Profilsprache: "],
    "Aktywny profil zmieniono na ": ["Active profile changed to ", "Активный профиль изменён на ", "Активний профіль змінено на ", "Perfil activo cambiado a ", "Profil actif changé : ", "Aktives Profil geändert zu "],
    "Profil przetłumaczony i zapisany lokalnie. Aktywny język: ": ["Profile translated and saved locally. Active language: ", "Профиль переведён и сохранён локально. Активный язык: ", "Профіль перекладено й збережено локально. Активна мова: ", "Perfil traducido y guardado localmente. Idioma activo: ", "Profil traduit et enregistré localement. Langue active : ", "Profil übersetzt und lokal gespeichert. Aktive Sprache: "],
    "Tłumaczę profil na język ": ["Translating the profile into ", "Перевожу профиль на язык ", "Перекладаю профіль мовою ", "Traduciendo el perfil al idioma ", "Traduction du profil en ", "Profil wird ins Deutsche übersetzt: "],
    "Tłumaczę profil na ": ["Translating the profile into ", "Перевожу профиль на ", "Перекладаю профіль ", "Traduciendo el perfil al ", "Traduction du profil en ", "Profil wird übersetzt nach "],
    "Użyj /translate en, /translate ru, /translate uk lub /translate pl.": ["Use /translate en, /translate ru, /translate uk or /translate pl.", "Используйте /translate en, /translate ru, /translate uk или /translate pl.", "Скористайтеся /translate en, /translate ru, /translate uk або /translate pl.", "Usa /translate en, /translate ru, /translate uk o /translate pl.", "Utilisez /translate en, /translate ru, /translate uk ou /translate pl.", "Nutze /translate en, /translate ru, /translate uk oder /translate pl."],
    "Porównuję pola formularza z aktywnym profilem…": ["Comparing the form fields with the active profile…", "Сопоставляю поля формы с активным профилем…", "Порівнюю поля форми з активним профілем…", "Comparando los campos con el perfil activo…", "Comparaison des champs avec le profil actif…", "Formularfelder werden mit dem aktiven Profil verglichen…"],
    "Zgoda otrzymana. Odczytuję CV i przygotowuję profil. To może chwilę potrwać.": ["Consent received. Reading the CV and preparing the profile; this may take a moment.", "Согласие получено. Читаю CV и готовлю профиль. Это может занять некоторое время.", "Згоду отримано. Читаю CV та готую профіль. Це може тривати кілька хвилин.", "Consentimiento recibido. Estoy leyendo el CV y preparando el perfil; puede tardar un momento.", "Consentement reçu. Lecture du CV et préparation du profil en cours ; cela peut prendre un moment.", "Zustimmung erhalten. Lebenslauf wird gelesen und das Profil vorbereitet; dies kann einen Moment dauern."],
    "Pokazano ": ["Showing ", "Показано ", "Показано ", "Mostradas ", "Affichage de ", "Angezeigt: "],
}
for _source, _values in _UI_AUDIT_ADDITIONS.items():
    UI_PHRASES[_source] = dict(zip(("en", "ru", "uk", "es", "fr", "de"), _values))


_UI_FINAL = {
"Nie ma zapisanych CV ani profili. Wyślij CV w tym czacie, aby je dodać.": ["No CVs or profiles are saved. Send a CV here to add one.","Нет сохранённых CV или профилей. Отправьте CV сюда, чтобы добавить его.","Немає збережених CV або профілів. Надішліть CV сюди, щоб додати його.","No hay CV ni perfiles guardados. Envía uno aquí para añadirlo.","Aucun CV ni profil enregistré. Envoyez-en un ici pour en ajouter un.","Keine Lebensläufe oder Profile gespeichert. Sende hier einen Lebenslauf, um ihn hinzuzufügen."],
"Zarządzanie profilami i zapisanymi CV:": ["Manage profiles and saved CVs:","Управление профилями и сохранёнными CV:","Керування профілями та збереженими CV:","Gestionar perfiles y CV guardados:","Gérer les profils et CV enregistrés :","Profile und gespeicherte Lebensläufe verwalten:"],
"Nie znaleziono tego lokalnego CV.": ["That local CV was not found.","Этот локальный CV не найден.","Цей локальний CV не знайдено.","No se encontró ese CV local.","Ce CV local est introuvable.","Dieser lokale Lebenslauf wurde nicht gefunden."],
"Otwieram profil użytkownika.": ["Opening your profile.","Открываю профиль пользователя.","Відкриваю профіль користувача.","Abriendo tu perfil.","Ouverture de votre profil.","Dein Profil wird geöffnet."],
"Aktywny profil zmieniono na ": ["Active profile changed to ","Активный профиль изменён на ","Активний профіль змінено на ","Perfil activo cambiado a ","Profil actif changé : ","Aktives Profil geändert zu "],
"Rozpoczynam wyszukiwanie ofert na Pracuj.pl. Sprawdzę kolejne strony i zbliżone nazwy stanowisk.": ["Starting the Pracuj.pl search. I’ll check multiple pages and related job titles.","Начинаю поиск на Pracuj.pl. Проверю несколько страниц и близкие названия должностей.","Починаю пошук на Pracuj.pl. Перевірю кілька сторінок і споріднені назви посад.","Inicio la búsqueda en Pracuj.pl. Revisaré varias páginas y puestos relacionados.","Recherche sur Pracuj.pl en cours. Je vérifierai plusieurs pages et des intitulés proches.","Suche auf Pracuj.pl gestartet. Ich prüfe mehrere Seiten und verwandte Berufsbezeichnungen."],
"Wyszukiwanie trwa: sprawdzono ": ["Search in progress: checked ","Поиск продолжается: проверено ","Пошук триває: перевірено ","Búsqueda en curso: revisadas ","Recherche en cours : ","Suche läuft: geprüft "],
" stronę/strony Pracuj.pl i znaleziono ": [" Pracuj.pl pages; found "," страниц Pracuj.pl; найдено "," сторінок Pracuj.pl; знайдено "," páginas de Pracuj.pl; encontradas "," pages Pracuj.pl ; "," Pracuj.pl-Seiten; gefunden "],
" unikalnych ofert…": [" unique jobs…"," уникальных вакансий…"," унікальних вакансій…"," ofertas únicas…"," offres uniques…"," eindeutige Stellen…"],
"Pobrano ": ["Retrieved ","Загружено ","Завантажено ","Obtenidas ","Récupération de ","Abgerufen: "],
" ofert z ": [" jobs from "," вакансий с "," вакансій із "," ofertas de "," offres sur "," Stellen von "],
" stron. Oceniam dopasowanie — partia ": [" pages. Assessing matches — batch "," страниц. Оцениваю соответствие — партия "," сторінок. Оцінюю відповідність — пакет "," páginas. Evaluando coincidencias — lote "," pages. Évaluation des correspondances — lot "," Seiten. Bewertung der Passung — Stapel "],
"Zakończono wyszukiwanie. Sprawdzono ": ["Search complete. Checked ","Поиск завершён. Проверено ","Пошук завершено. Перевірено ","Búsqueda finalizada. Revisadas ","Recherche terminée. ","Suche abgeschlossen. Geprüft "],
" stron i oceniono ": [" pages and assessed "," страниц и оценено "," сторінок і оцінено "," páginas y evaluadas "," pages et évalué "," Seiten und bewertet "],
" ofert; ": [" jobs; "," вакансий; "," вакансій; "," ofertas; "," offres ; "," Stellen; "],
" spełnia próg dopasowania 60%.": [" meet the 60% match threshold."," соответствуют порогу 60 %."," відповідають порогу 60 %."," alcanzan el umbral del 60 %."," atteignent le seuil de 60 %."," erfüllen den Schwellenwert von 60 % Übereinstimmung."],
" pasujących ofert.": [" matching jobs."," подходящих вакансий."," відповідних вакансій."," ofertas adecuadas."," offres pertinentes."," passende Stellen."],
" pasujących ofert. Użyj przycisku, aby zobaczyć dalsze wyniki.": [" matching jobs. Use the button to see more results."," подходящих вакансий. Нажмите кнопку, чтобы увидеть следующие результаты."," відповідних вакансій. Натисніть кнопку, щоб переглянути наступні результати."," ofertas adecuadas. Usa el botón para ver más resultados."," offres pertinentes. Utilisez le bouton pour afficher la suite."," passende Stellen. Mit der Schaltfläche werden weitere Ergebnisse angezeigt."],
"Nie znaleziono ofert spełniających próg dopasowania 60% albo portal zablokował odczyt. Spróbuj później lub zmień kryteria.": ["No jobs met the 60% match threshold, or the portal blocked access. Try later or change the criteria.","Нет вакансий с соответствием от 60 %, либо портал заблокировал чтение. Попробуйте позже или измените критерии.","Не знайдено вакансій із відповідністю від 60 %, або портал заблокував читання. Спробуйте пізніше чи змініть критерії.","Ninguna oferta alcanzó el 60 % de coincidencia o el portal bloqueó el acceso. Inténtalo más tarde o cambia los criterios.","Aucune offre n’atteint le seuil de 60 % ou le portail a bloqué l’accès. Réessayez plus tard ou modifiez les critères.","Keine Stelle erreicht 60 % Übereinstimmung oder das Portal blockiert den Zugriff. Versuche es später erneut oder ändere die Kriterien."],
"Nie udało się pobrać ofert z Pracuj.pl. Portal może blokować automatyczny odczyt albo nie ma wyników dla tych stanowisk.": ["Could not retrieve jobs from Pracuj.pl. The portal may block automated access, or there may be no results for these roles.","Не удалось загрузить вакансии с Pracuj.pl. Портал может блокировать автоматическое чтение или вакансий по этим должностям нет.","Не вдалося отримати вакансії з Pracuj.pl. Портал може блокувати автоматичне читання або вакансій за цими посадами немає.","No se pudieron obtener ofertas de Pracuj.pl. El portal puede bloquear el acceso automático o no hay resultados para estos puestos.","Impossible de récupérer les offres de Pracuj.pl. Le portail peut bloquer l’accès automatisé ou aucun résultat ne correspond à ces postes.","Stellen konnten nicht von Pracuj.pl abgerufen werden. Das Portal blockiert möglicherweise den automatischen Zugriff oder es gibt keine Ergebnisse für diese Berufe."],
"Nie udało się pobrać lub ocenić ofert. Sprawdź połączenie i spróbuj ponownie.": ["Could not retrieve or assess jobs. Check the connection and try again.","Не удалось загрузить или оценить вакансии. Проверьте подключение и попробуйте ещё раз.","Не вдалося завантажити або оцінити вакансії. Перевірте з’єднання та спробуйте ще раз.","No se pudieron obtener o evaluar las ofertas. Comprueba la conexión e inténtalo de nuevo.","Impossible de récupérer ou d’évaluer les offres. Vérifiez la connexion et réessayez.","Stellen konnten nicht abgerufen oder bewertet werden. Prüfe die Verbindung und versuche es erneut."],
"Nie udało się dokończyć tej operacji. Bot odebrał polecenie, ale wystąpił błąd; spróbuj ponownie.": ["The operation could not be completed. The bot received your request but encountered an error; try again.","Не удалось завершить операцию. Бот получил команду, но произошла ошибка; попробуйте ещё раз.","Не вдалося завершити операцію. Бот отримав команду, але сталася помилка; спробуйте ще раз.","No se pudo completar la operación. El bot recibió la solicitud, pero ocurrió un error; inténtalo de nuevo.","L’opération n’a pas abouti. Le bot a reçu votre demande, mais une erreur est survenue ; réessayez.","Der Vorgang konnte nicht abgeschlossen werden. Der Bot hat deine Anfrage erhalten, aber es trat ein Fehler auf. Bitte erneut versuchen."],
"PROFILE": ["PROFILE","ПРОФИЛЬ","ПРОФІЛЬ","PERFIL","PROFIL","PROFIL"],
"EDUKACJA": ["EDUCATION","ОБРАЗОВАНИЕ","ОСВІТА","EDUCACIÓN","FORMATION","AUSBILDUNG"],
"ROBOCZY PROFIL DO SPRAWDZENIA": ["DRAFT PROFILE FOR REVIEW","ЧЕРНОВИК ПРОФИЛЯ ДЛЯ ПРОВЕРКИ","ЧЕРНЕТКА ПРОФІЛЮ ДЛЯ ПЕРЕВІРКИ","BORRADOR DEL PERFIL PARA REVISAR","BROUILLON DU PROFIL À VÉRIFIER","PROFILENTWURF ZUR PRÜFUNG"],
"DOŚWIADCZENIE I CZYNNOŚCI WPROST WSKAZANE W CV": ["EXPERIENCE AND DUTIES EXPLICITLY STATED IN THE CV","ОПЫТ И ОБЯЗАННОСТИ, ПРЯМО УКАЗАННЫЕ В CV","ДОСВІД І ОБОВ’ЯЗКИ, ПРЯМО ВКАЗАНІ В CV","EXPERIENCIA Y FUNCIONES INDICADAS EXPRESAMENTE EN EL CV","EXPÉRIENCE ET TÂCHES EXPLICITEMENT MENTIONNÉES DANS LE CV","ERFAHRUNG UND IM LEBENSLAUF AUSDRÜCKLICH GENANNTE TÄTIGKEITEN"],
"Osoba: ": ["Person: ","Кандидат: ","Кандидат: ","Persona: ","Personne : ","Person: "],
"Kontakt: ": ["Contact: ","Контакт: ","Контакт: ","Contacto: ","Contact : ","Kontakt: "],
"Lokalizacja: ": ["Location: ","Местоположение: ","Місце перебування: ","Ubicación: ","Lieu : ","Standort: "],
"Nagłówek: ": ["Headline: ","Заголовок: ","Заголовок: ","Titular: ","Titre : ","Überschrift: "],
"Doświadczenie: ": ["Experience: ","Опыт: ","Досвід: ","Experiencia: ","Expérience : ","Erfahrung: "],
"Kompetencje: ": ["Skills: ","Навыки: ","Навички: ","Competencias: ","Compétences : ","Kompetenzen: "],
"Branże: ": ["Industries: ","Отрасли: ","Галузі: ","Sectores: ","Secteurs : ","Branchen: "],
"Języki: ": ["Languages: ","Языки: ","Мови: ","Idiomas: ","Langues : ","Sprachen: "],
"Certyfikaty: ": ["Certifications: ","Сертификаты: ","Сертифікати: ","Certificaciones: ","Certifications : ","Zertifikate: "],
"Najważniejsze projekty: ": ["Key projects: ","Ключевые проекты: ","Ключові проєкти: ","Proyectos destacados: ","Projets clés : ","Wichtige Projekte: "],
"Preferencje: ": ["Preferences: ","Предпочтения: ","Побажання: ","Preferencias: ","Préférences : ","Präferenzen: "],
"Informacje uzupełnione przez Ciebie: ": ["Information you added: ","Добавленные вами сведения: ","Додані вами відомості: ","Información añadida por ti: ","Informations que vous avez ajoutées : ","Von dir ergänzte Angaben: "],
"Do potwierdzenia: ": ["To confirm: ","Требует подтверждения: ","Потребує підтвердження: ","Por confirmar: ","À confirmer : ","Zu bestätigen: "],
"EDUKACJA": ["EDUCATION","ОБРАЗОВАНИЕ","ОСВІТА","EDUCACIÓN","FORMATION","AUSBILDUNG"],
"Sprawdź dane. Zapis nastąpi dopiero po wybraniu „Zatwierdź i zapisz”.": ["Review the details. They will be saved only after you choose “Approve and save”.","Проверьте данные. Они будут сохранены только после нажатия «Подтвердить и сохранить».","Перевірте дані. Їх буде збережено лише після вибору «Підтвердити й зберегти».","Revisa los datos. Solo se guardarán al elegir «Aprobar y guardar».","Vérifiez les informations. Elles ne seront enregistrées qu’après avoir choisi « Valider et enregistrer ».","Prüfe die Angaben. Sie werden erst nach „Bestätigen und speichern“ gespeichert."],
"Pola formularza sprawdzone dla wybranej oferty:": ["Form fields checked for the selected job:","Поля формы проверены для выбранной вакансии:","Поля форми перевірено для вибраної вакансії:","Campos comprobados para la oferta seleccionada:","Champs vérifiés pour l’offre sélectionnée :","Formularfelder für die ausgewählte Stelle geprüft:"],
"Odpowiedzi do skopiowania": ["Answers to copy","Ответы для копирования","Відповіді для копіювання","Respuestas para copiar","Réponses à copier","Antworten zum Kopieren"],
"Odpowiedź do skopiowania: ": ["Answer to copy: ","Ответ для копирования: ","Відповідь для копіювання: ","Respuesta para copiar: ","Réponse à copier : ","Antwort zum Kopieren: "],
"Brak danych: ": ["Information missing: ","Не хватает данных: ","Бракує даних: ","Faltan datos: ","Information manquante : ","Fehlende Angaben: "],
"Sprawdź propozycje, skopiuj odpowiedzi i samodzielnie wyślij aplikację. Bot nie loguje się ani nie wysyła formularza.": ["Review and copy the suggested answers, then submit the application yourself. The bot does not sign in or submit forms.","Проверьте и скопируйте предложенные ответы, затем отправьте заявку самостоятельно. Бот не входит в аккаунт и не отправляет формы.","Перевірте й скопіюйте запропоновані відповіді, а заявку надішліть самостійно. Бот не входить в обліковий запис і не надсилає форми.","Revisa y copia las respuestas sugeridas y envía tú la solicitud. El bot no inicia sesión ni envía formularios.","Vérifiez et copiez les réponses proposées, puis envoyez vous-même la candidature. Le bot ne se connecte pas et ne soumet aucun formulaire.","Prüfe und kopiere die Vorschläge und sende die Bewerbung selbst ab. Der Bot meldet sich nicht an und übermittelt keine Formulare."],
}
for _source, _values in _UI_FINAL.items():
    UI_PHRASES[_source] = dict(zip(("en", "ru", "uk", "es", "fr", "de"), _values))


UI_FORMATS = {
 "telegram_id": {
  "pl":"Twój Telegram ID: {id}","en":"Your Telegram ID: {id}","ru":"Ваш Telegram ID: {id}","uk":"Ваш Telegram ID: {id}","es":"Tu ID de Telegram: {id}","fr":"Votre identifiant Telegram : {id}","de":"Deine Telegram-ID: {id}"},
 "active_profile_changed": {
  "pl":"Aktywny profil zmieniono na {id}. Użyj /profile, aby go wyświetlić.","en":"Active profile changed to {id}. Use /profile to view it.","ru":"Активный профиль изменён на {id}. Используйте /profile, чтобы посмотреть его.","uk":"Активний профіль змінено на {id}. Скористайтеся /profile, щоб переглянути його.","es":"El perfil activo cambió a {id}. Usa /profile para verlo.","fr":"Le profil actif est maintenant {id}. Utilisez /profile pour l’afficher.","de":"Aktives Profil auf {id} geändert. Mit /profile anzeigen."},
 "search_batch": {
  "pl":"Pobrano {count} ofert z {pages} stron. Oceniam dopasowanie — partia {index}/{total}…","en":"Retrieved {count} jobs from {pages} pages. Assessing matches — batch {index}/{total}…","ru":"Загружено {count} вакансий с {pages} страниц. Оцениваю соответствие — пакет {index}/{total}…","uk":"Завантажено {count} вакансій із {pages} сторінок. Оцінюю відповідність — пакет {index}/{total}…","es":"Obtenidas {count} ofertas de {pages} páginas. Evaluando coincidencias — lote {index}/{total}…","fr":"{count} offres récupérées sur {pages} pages. Évaluation des correspondances — lot {index}/{total}…","de":"{count} Stellen von {pages} Seiten abgerufen. Bewertung der Passung — Stapel {index}/{total}…"},
 "search_page_progress": {
  "pl":"Wyszukiwanie trwa: sprawdzono {pages} stronę/strony Pracuj.pl i znaleziono {count} unikalnych ofert…","en":"Search in progress: checked {pages} Pracuj.pl pages and found {count} unique jobs…","ru":"Поиск продолжается: проверено страниц Pracuj.pl: {pages}; найдено уникальных вакансий: {count}…","uk":"Пошук триває: перевірено сторінок Pracuj.pl: {pages}; знайдено унікальних вакансій: {count}…","es":"Búsqueda en curso: revisadas {pages} páginas de Pracuj.pl; encontradas {count} ofertas únicas…","fr":"Recherche en cours : {pages} pages Pracuj.pl vérifiées, {count} offres uniques trouvées…","de":"Suche läuft: {pages} Pracuj.pl-Seiten geprüft, {count} eindeutige Stellen gefunden…"},
 "search_finished": {
  "pl":"Zakończono wyszukiwanie w {seconds:.1f} s. Sprawdzono {pages} stron i oceniono {count} ofert; {qualified} spełnia próg dopasowania 60%.","en":"Search completed in {seconds:.1f} s. Checked {pages} pages and assessed {count} jobs; {qualified} meet the 60% match threshold.","ru":"Поиск завершён за {seconds:.1f} с. Проверено страниц: {pages}; оценено вакансий: {count}; порог 60% прошли: {qualified}.","uk":"Пошук завершено за {seconds:.1f} с. Перевірено сторінок: {pages}; оцінено вакансій: {count}; поріг 60% пройшли: {qualified}.","es":"Búsqueda finalizada en {seconds:.1f} s. Revisadas {pages} páginas y evaluadas {count} ofertas; {qualified} alcanzan el 60 %.","fr":"Recherche terminée en {seconds:.1f} s. {pages} pages et {count} offres évaluées ; {qualified} atteignent 60 %.","de":"Suche in {seconds:.1f} s abgeschlossen. {pages} Seiten und {count} Stellen geprüft; {qualified} erreichen mindestens 60 % Übereinstimmung."},
 "search_results_more": {
  "pl":"Pokazano {start}–{end} z {total} pasujących ofert. Użyj przycisku, aby zobaczyć dalsze wyniki.","en":"Showing {start}–{end} of {total} matching jobs. Use the button to see more results.","ru":"Показано {start}–{end} из {total} подходящих вакансий. Нажмите кнопку, чтобы увидеть следующие результаты.","uk":"Показано {start}–{end} з {total} відповідних вакансій. Натисніть кнопку, щоб переглянути наступні результати.","es":"Mostrando {start}–{end} de {total} ofertas adecuadas. Usa el botón para ver más resultados.","fr":"Affichage de {start}–{end} sur {total} offres pertinentes. Utilisez le bouton pour afficher la suite.","de":"{start}–{end} von {total} passenden Stellen angezeigt. Mit der Schaltfläche werden weitere Ergebnisse angezeigt."},
 "search_results_end": {
  "pl":"Pokazano {start}–{end} z {total} pasujących ofert.","en":"Showing {start}–{end} of {total} matching jobs.","ru":"Показано {start}–{end} из {total} подходящих вакансий.","uk":"Показано {start}–{end} з {total} відповідних вакансій.","es":"Mostrando {start}–{end} de {total} ofertas adecuadas.","fr":"Affichage de {start}–{end} sur {total} offres pertinentes.","de":"{start}–{end} von {total} passenden Stellen angezeigt."},
 "delete_cv_confirm": {
  "pl":"Usunąć lokalny plik CV „{filename}”? Usunięty zostanie tylko ten plik.","en":"Delete the local CV file “{filename}”? Only this file will be removed.","ru":"Удалить локальный файл CV «{filename}»? Будет удалён только этот файл.","uk":"Видалити локальний файл CV «{filename}»? Буде видалено лише цей файл.","es":"¿Eliminar el archivo CV local «{filename}»? Solo se eliminará este archivo.","fr":"Supprimer le fichier CV local « {filename} » ? Seul ce fichier sera supprimé.","de":"Die lokale Lebenslaufdatei „{filename}“ löschen? Nur diese Datei wird entfernt."},
}

UI_FORMATS.update({
 "deleted_cv_plain": {
  "pl":"Usunięto plik CV „{filename}”.","en":"Deleted CV file “{filename}”.","ru":"Файл CV «{filename}» удалён.","uk":"Файл CV «{filename}» видалено.","es":"Se eliminó el archivo CV «{filename}».","fr":"Fichier CV « {filename} » supprimé.","de":"Lebenslaufdatei „{filename}“ gelöscht."},
 "deleted_cv_linked": {
  "pl":"Usunięto plik CV „{filename}”. Powiązany profil pozostał zapisany; źródłowego CV nie można już ponownie odczytać.","en":"Deleted CV file “{filename}”. The linked profile remains saved, but its source CV can no longer be read again.","ru":"Файл CV «{filename}» удалён. Связанный профиль сохранён, но исходное CV больше нельзя прочитать повторно.","uk":"Файл CV «{filename}» видалено. Пов’язаний профіль залишився, але вихідне CV більше не можна перечитати.","es":"Se eliminó el archivo CV «{filename}». El perfil vinculado sigue guardado, pero ya no se puede volver a leer el CV original.","fr":"Fichier CV « {filename} » supprimé. Le profil associé reste enregistré, mais le CV source ne peut plus être relu.","de":"Lebenslaufdatei „{filename}“ gelöscht. Das verknüpfte Profil bleibt gespeichert, aber die Quelldatei kann nicht erneut gelesen werden."},
 "deleted_profile_with_replacement": {
  "pl":"Usunięto profil. Plik CV pozostał lokalnie. Aktywny jest teraz profil {id}.","en":"Profile deleted. The CV file remains stored locally. Profile {id} is now active.","ru":"Профиль удалён. Файл CV остался локально. Теперь активен профиль {id}.","uk":"Профіль видалено. Файл CV залишився локально. Тепер активний профіль {id}.","es":"Perfil eliminado. El archivo CV sigue guardado localmente. El perfil {id} ahora está activo.","fr":"Profil supprimé. Le fichier CV reste enregistré localement. Le profil {id} est maintenant actif.","de":"Profil gelöscht. Die Lebenslaufdatei bleibt lokal gespeichert. Profil {id} ist jetzt aktiv."},
 "deleted_profile_no_replacement": {
  "pl":"Usunięto profil. Plik CV pozostał lokalnie. Wyślij nowe CV, aby utworzyć kolejny profil.","en":"Profile deleted. The CV file remains stored locally. Send a new CV to create another profile.","ru":"Профиль удалён. Файл CV остался локально. Отправьте новое CV, чтобы создать профиль.","uk":"Профіль видалено. Файл CV залишився локально. Надішліть нове CV, щоб створити профіль.","es":"Perfil eliminado. El archivo CV sigue guardado localmente. Envía otro CV para crear un perfil.","fr":"Profil supprimé. Le fichier CV reste enregistré localement. Envoyez un nouveau CV pour créer un autre profil.","de":"Profil gelöscht. Die Lebenslaufdatei bleibt lokal gespeichert. Sende einen neuen Lebenslauf, um ein weiteres Profil zu erstellen."},
})

def format_ui(key: str, language: str, **values: object) -> str:
    language = normalize_language(language)
    return UI_FORMATS[key][language].format(**values)


for _source, _values in {
 "Lokalne pliki CV — wybierz, aby usunąć:": ["Local CV files — select one to delete:","Локальные файлы CV — выберите для удаления:","Локальні файли CV — виберіть для видалення:","Archivos CV locales: selecciona uno para eliminarlo:","Fichiers CV locaux — sélectionnez-en un à supprimer :","Lokale Lebensläufe — zum Löschen auswählen:"],
 "Profile zapisane z CV:": ["Profiles created from CVs:","Профили, созданные из CV:","Профілі, створені з CV:","Perfiles creados desde CV:","Profils créés à partir des CV :","Aus Lebensläufen erstellte Profile:"],
 "Usuń wybrane CV": ["Delete selected CV","Удалить выбранное CV","Видалити вибране CV","Eliminar el CV seleccionado","Supprimer le CV sélectionné","Ausgewählten Lebenslauf löschen"],
 "Zapisz uzupełnienie": ["Save profile update","Сохранить дополнение","Зберегти доповнення","Guardar actualización","Enregistrer le complément","Ergänzung speichern"],
 "🔙 Wróć do profilu": ["🔙 Back to profile","🔙 Назад к профилю","🔙 Назад до профілю","🔙 Volver al perfil","🔙 Retour au profil","🔙 Zurück zum Profil"],
}.items():
    UI_PHRASES[_source] = dict(zip(("en", "ru", "uk", "es", "fr", "de"), _values))


UI_FORMATS["analyze_cv_button"] = {
 "pl":"Analizuj: {filename}","en":"Analyze: {filename}","ru":"Анализировать: {filename}","uk":"Проаналізувати: {filename}","es":"Analizar: {filename}","fr":"Analyser : {filename}","de":"Analysieren: {filename}"}


UI_PHRASES["Pracodawca: "] = dict(zip(("en","ru","uk","es","fr","de"), ["Employer: ","Работодатель: ","Роботодавець: ","Empresa: ","Employeur : ","Arbeitgeber: "]))
UI_PHRASES["Aby przygotować profil, wyodrębnię tekst z wybranego lokalnego CV i przekażę go do OpenAI API. Profil pokażę Ci do sprawdzenia, a zapiszę dopiero po zatwierdzeniu. Czy wyrażasz zgodę na wysłanie tekstu tego CV do OpenAI?"] = dict(zip(("en","ru","uk","es","fr","de"), [
"To prepare a profile, I’ll extract text from the selected local CV and send it to the OpenAI API. I’ll show you the profile and save it only after approval. Do you consent to sending this CV text to OpenAI?",
"Чтобы подготовить профиль, я извлеку текст из выбранного локального CV и отправлю его в OpenAI API. Сначала покажу профиль и сохраню только после подтверждения. Вы согласны отправить текст этого CV в OpenAI?",
"Щоб підготувати профіль, я витягну текст із вибраного локального CV і надішлю його до OpenAI API. Спочатку покажу профіль і збережу лише після підтвердження. Ви погоджуєтеся на надсилання тексту цього CV до OpenAI?",
"Para preparar el perfil, extraeré el texto del CV local seleccionado y lo enviaré a la API de OpenAI. Te mostraré el perfil y solo lo guardaré tras tu aprobación. ¿Aceptas enviar este CV a OpenAI?",
"Pour préparer le profil, j’extrairai le texte du CV local sélectionné et l’enverrai à l’API OpenAI. Je vous montrerai le profil et ne l’enregistrerai qu’après validation. Acceptez-vous l’envoi de ce CV à OpenAI ?",
"Zum Erstellen des Profils extrahiere ich den Text aus dem ausgewählten lokalen Lebenslauf und sende ihn an die OpenAI-API. Ich zeige dir das Profil und speichere es erst nach Freigabe. Bist du mit dem Senden dieses Lebenslaufs an OpenAI einverstanden?" ]))


UI_PHRASES["Analizuję udokumentowane obowiązki i kompetencje, aby dobrać zbliżone nazwy stanowisk…"] = dict(zip(("en","ru","uk","es","fr","de"), [
"Reviewing documented duties and skills to find related job titles…",
"Анализирую подтверждённые обязанности и навыки, чтобы подобрать близкие названия должностей…",
"Аналізую підтверджені обов’язки й навички, щоб підібрати споріднені назви посад…",
"Analizando las funciones y competencias documentadas para encontrar puestos relacionados…",
"Analyse des tâches et compétences documentées pour trouver des intitulés proches…",
"Dokumentierte Tätigkeiten und Kompetenzen werden geprüft, um verwandte Jobtitel zu finden…" ]))


for _source, _values in {
 "brak w CV": ["not stated in CV","не указано в CV","не вказано в CV","no indicado en el CV","non indiqué dans le CV","im Lebenslauf nicht angegeben"],
 "brak": ["not provided","не указано","не вказано","no indicado","non indiqué","nicht angegeben"],
 "Brak podsumowania w CV": ["No summary in the CV","В CV нет краткого описания","У CV немає короткого опису","No hay resumen en el CV","Aucun résumé dans le CV","Keine Zusammenfassung im Lebenslauf"],
 "Uzupełnij tę informację ręcznie.": ["Add this information manually.","Укажите эту информацию вручную.","Додайте цю інформацію вручну.","Completa esta información manualmente.","Complétez cette information manuellement.","Ergänze diese Angabe manuell."],
 "Pole": ["Field","Поле","Поле","Campo","Champ","Feld"],
 "Oferta": ["Job","Вакансия","Вакансія","Oferta","Offre","Stelle"],
 "Firma niepodana": ["Company not specified","Компания не указана","Компанію не вказано","Empresa no especificada","Entreprise non précisée","Unternehmen nicht angegeben"],
 "Lokalizacja niepodana": ["Location not specified","Местоположение не указано","Місце розташування не вказано","Ubicación no especificada","Lieu non précisé","Standort nicht angegeben"],
}.items():
    UI_PHRASES[_source] = dict(zip(("en","ru","uk","es","fr","de"), _values))
UI_FORMATS["candidate_position"] = {
 "pl":"Stanowisko {number}","en":"Position {number}","ru":"Должность {number}","uk":"Посада {number}","es":"Puesto {number}","fr":"Poste {number}","de":"Position {number}"}


UI_FORMATS["cv_text_limit"] = {
 "pl":"CV przekracza limit {limit} znaków i nie zostało obcięte ani zapisane jako profil. Podziel plik lub wyślij krótszą wersję.",
 "en":"The CV exceeds the {limit}-character processing limit. It was not truncated or saved as a profile. Split the file or send a shorter version.",
 "ru":"CV превышает лимит обработки в {limit} символов. Текст не обрезан, профиль не сохранён. Разделите файл или отправьте более короткую версию.",
 "uk":"CV перевищує ліміт обробки у {limit} символів. Текст не обрізано, профіль не збережено. Розділіть файл або надішліть коротшу версію.",
 "es":"El CV supera el límite de procesamiento de {limit} caracteres. No se recortó ni se guardó como perfil. Divide el archivo o envía una versión más breve.",
 "fr":"Le CV dépasse la limite de traitement de {limit} caractères. Il n’a pas été tronqué ni enregistré comme profil. Scindez le fichier ou envoyez une version plus courte.",
 "de":"Der Lebenslauf überschreitet das Verarbeitungslimit von {limit} Zeichen. Er wurde nicht gekürzt oder als Profil gespeichert. Teile die Datei oder sende eine kürzere Version."}

# UI strings added after the initial language catalog audit. Keep every user-facing
# phrase here complete across all supported languages; candidate/source text stays as written.
_UI_COVERAGE_PATCH = {
    "Nie ma jeszcze zapisanego profilu. Możesz zarządzać zapisanymi CV lub wysłać nowe CV.": [
        "There is no saved profile yet. You can manage saved CVs or send a new CV.",
        "Пока нет сохранённого профиля. Можно управлять сохранёнными CV или отправить новое CV.",
        "Ще немає збереженого профілю. Ви можете керувати збереженими CV або надіслати нове CV.",
        "Aún no hay un perfil guardado. Puedes gestionar los CV guardados o enviar uno nuevo.",
        "Aucun profil n’est encore enregistré. Vous pouvez gérer les CV enregistrés ou en envoyer un nouveau.",
        "Es ist noch kein Profil gespeichert. Du kannst gespeicherte Lebensläufe verwalten oder einen neuen senden.",
    ],
    "Nie ma zapisanych CV ani profili. Wyślij CV w tym czacie, aby je dodać.": [
        "There are no saved CVs or profiles. Send a CV here to add one.",
        "Сохранённых CV и профилей нет. Отправьте CV в этот чат, чтобы добавить его.",
        "Збережених CV і профілів немає. Надішліть CV у цей чат, щоб додати його.",
        "No hay CV ni perfiles guardados. Envía un CV aquí para añadirlo.",
        "Aucun CV ni profil enregistré. Envoyez un CV ici pour l’ajouter.",
        "Es sind keine Lebensläufe oder Profile gespeichert. Sende hier einen Lebenslauf, um ihn hinzuzufügen.",
    ],
    "Sprawdzam publiczny formularz wybranej oferty…": [
        "Checking the public application form for the selected job…",
        "Проверяю общедоступную форму выбранной вакансии…",
        "Перевіряю загальнодоступну форму обраної вакансії…",
        "Revisando el formulario público de la oferta seleccionada…",
        "Vérification du formulaire public de l’offre sélectionnée…",
        "Das öffentliche Bewerbungsformular der ausgewählten Stelle wird geprüft…",
    ],
    "Odczytałem pola formularza. Przygotowuję odpowiedzi na podstawie profilu…": [
        "I read the form fields. Preparing answers based on your profile…",
        "Поля формы прочитаны. Готовлю ответы на основе профиля…",
        "Поля форми прочитано. Готую відповіді на основі профілю…",
        "He leído los campos del formulario. Preparando respuestas según tu perfil…",
        "Les champs du formulaire ont été lus. Préparation des réponses selon votre profil…",
        "Die Formularfelder wurden gelesen. Antworten auf Grundlage deines Profils werden vorbereitet…",
    ],
    "Anulowano. Zapisany profil nie został zmieniony.": [
        "Cancelled. The saved profile was not changed.",
        "Отменено. Сохранённый профиль не изменён.",
        "Скасовано. Збережений профіль не змінено.",
        "Cancelado. El perfil guardado no se modificó.",
        "Annulé. Le profil enregistré n’a pas été modifié.",
        "Abgebrochen. Das gespeicherte Profil wurde nicht geändert.",
    ],
    "Uzupełniony profil zapisano lokalnie w języku oryginalnego CV.": [
        "The updated profile was saved locally in the original CV language.",
        "Дополненный профиль сохранён локально на языке исходного CV.",
        "Доповнений профіль збережено локально мовою оригінального CV.",
        "El perfil actualizado se guardó localmente en el idioma del CV original.",
        "Le profil complété a été enregistré localement dans la langue du CV d’origine.",
        "Das ergänzte Profil wurde lokal in der Sprache des ursprünglichen Lebenslaufs gespeichert.",
    ],
    "Bot nie poprosi Cię o ręczne wklejanie pytań; otwórz formularz samodzielnie:": [
        "The bot won't ask you to paste the questions manually; open the form yourself:",
        "Бот не попросит вручную вставлять вопросы; откройте форму самостоятельно:",
        "Бот не просит вручну вставляти запитання; відкрийте форму самостійно:",
        "El bot no te pedirá que pegues las preguntas; abre el formulario por tu cuenta:",
        "Le bot ne vous demandera pas de copier les questions ; ouvrez le formulaire vous-même :",
        "Der Bot fordert dich nicht auf, die Fragen einzufügen; öffne das Formular selbst:",
    ],
    "Nie udało się zapisać uzupełnienia. Profil mógł zostać usunięty.": [
        "Couldn't save the profile update. The profile may have been deleted.",
        "Не удалось сохранить дополнение. Возможно, профиль был удалён.",
        "Не вдалося зберегти доповнення. Можливо, профіль було видалено.",
        "No se pudo guardar la actualización. Es posible que se haya eliminado el perfil.",
        "Impossible d’enregistrer le complément. Le profil a peut-être été supprimé.",
        "Die Profilerweiterung konnte nicht gespeichert werden. Möglicherweise wurde das Profil gelöscht.",
    ],
    "Pola odczytano, ale przygotowanie odpowiedzi nie powiodło się. Spróbuj ponownie później.": [
        "The fields were read, but the answers couldn't be prepared. Please try again later.",
        "Поля прочитаны, но подготовить ответы не удалось. Попробуйте позже.",
        "Поля прочитано, але підготувати відповіді не вдалося. Спробуйте пізніше.",
        "Se leyeron los campos, pero no se pudieron preparar las respuestas. Inténtalo más tarde.",
        "Les champs ont été lus, mais les réponses n’ont pas pu être préparées. Réessayez plus tard.",
        "Die Felder wurden gelesen, aber die Antworten konnten nicht vorbereitet werden. Bitte versuche es später erneut.",
    ],
    "Nie udało się usunąć pliku CV. Sprawdź uprawnienia do folderu data/cv.": [
        "Couldn't delete the CV file. Check permissions for the data/cv folder.",
        "Не удалось удалить файл CV. Проверьте разрешения для папки data/cv.",
        "Не вдалося видалити файл CV. Перевірте дозволи для папки data/cv.",
        "No se pudo eliminar el archivo CV. Comprueba los permisos de la carpeta data/cv.",
        "Impossible de supprimer le fichier CV. Vérifiez les droits du dossier data/cv.",
        "Die CV-Datei konnte nicht gelöscht werden. Prüfe die Berechtigungen des Ordners data/cv.",
    ],
    "Anulowano usuwanie CV. Plik pozostał zapisany.": [
        "CV deletion cancelled. The file remains saved.",
        "Удаление CV отменено. Файл остался сохранён.",
        "Видалення CV скасовано. Файл залишився збереженим.",
        "Se canceló la eliminación del CV. El archivo sigue guardado.",
        "Suppression du CV annulée. Le fichier reste enregistré.",
        "Das Löschen des Lebenslaufs wurde abgebrochen. Die Datei bleibt gespeichert.",
    ],
    "ROBOCZY PROFIL DO SPRAWDZENIA": [
        "DRAFT PROFILE FOR REVIEW", "ЧЕРНОВИК ПРОФИЛЯ ДЛЯ ПРОВЕРКИ", "ЧЕРНЕТКА ПРОФІЛЮ ДЛЯ ПЕРЕВІРКИ",
        "BORRADOR DEL PERFIL PARA REVISAR", "BROUILLON DU PROFIL À VÉRIFIER", "PROFILENTWURF ZUR ÜBERPRÜFUNG",
    ],
    "Osoba: ": ["Person: ", "Кандидат: ", "Кандидат: ", "Persona: ", "Personne : ", "Person: "],
    "Kontakt: ": ["Contact: ", "Контакты: ", "Контакти: ", "Contacto: ", "Contact : ", "Kontakt: "],
    "Lokalizacja: ": ["Location: ", "Местоположение: ", "Місце розташування: ", "Ubicación: ", "Lieu : ", "Standort: "],
    "Nagłówek: ": ["Headline: ", "Заголовок: ", "Заголовок: ", "Titular: ", "Intitulé : ", "Überschrift: "],
    "Doświadczenie: ": ["Experience: ", "Опыт: ", "Досвід: ", "Experiencia: ", "Expérience : ", "Erfahrung: "],
    "Kompetencje: ": ["Skills: ", "Навыки: ", "Навички: ", "Competencias: ", "Compétences : ", "Kompetenzen: "],
    "DOŚWIADCZENIE I CZYNNOŚCI WPROST WSKAZANE W CV": [
        "EXPERIENCE AND DUTIES EXPLICITLY STATED IN THE CV", "ОПЫТ И ОБЯЗАННОСТИ, ПРЯМО УКАЗАННЫЕ В CV",
        "ДОСВІД І ОБОВ’ЯЗКИ, БЕЗПОСЕРЕДНЬО ВКАЗАНІ В CV", "EXPERIENCIA Y TAREAS INDICADAS EXPRESAMENTE EN EL CV",
        "EXPÉRIENCE ET TÂCHES EXPLICITEMENT MENTIONNÉES DANS LE CV", "IM LEBENSLAUF AUSDRÜCKLICH GENANNTE ERFAHRUNG UND AUFGABEN",
    ],
    "Fragment źródłowy: ": ["Source excerpt: ", "Фрагмент источника: ", "Фрагмент джерела: ", "Fragmento de origen: ", "Extrait source : ", "Quellenauszug: "],
    "Brak czynności potwierdzonych dosłownym fragmentem CV.": [
        "No duties supported by a verbatim CV excerpt.", "Нет обязанностей, подтверждённых дословным фрагментом CV.",
        "Немає обов’язків, підтверджених дослівним фрагментом CV.", "No hay tareas respaldadas por una cita literal del CV.",
        "Aucune tâche confirmée par un extrait exact du CV.", "Keine Aufgaben durch einen wörtlichen Lebenslaufauszug belegt.",
    ],
    "EDUKACJA": ["EDUCATION", "ОБРАЗОВАНИЕ", "ОСВІТА", "EDUCACIÓN", "FORMATION", "AUSBILDUNG"],
    "Branże: ": ["Industries: ", "Отрасли: ", "Галузі: ", "Sectores: ", "Secteurs : ", "Branchen: "],
    "Języki: ": ["Languages: ", "Языки: ", "Мови: ", "Idiomas: ", "Langues : ", "Sprachen: "],
    "Certyfikaty: ": ["Certifications: ", "Сертификаты: ", "Сертифікати: ", "Certificaciones: ", "Certifications : ", "Zertifikate: "],
    "Najważniejsze projekty: ": ["Key projects: ", "Ключевые проекты: ", "Ключові проєкти: ", "Proyectos clave: ", "Projets clés : ", "Wichtige Projekte: "],
    "Preferencje: ": ["Preferences: ", "Предпочтения: ", "Побажання: ", "Preferencias: ", "Préférences : ", "Präferenzen: "],
    "Informacje uzupełnione przez Ciebie: ": ["Information you added: ", "Добавленные вами сведения: ", "Додана вами інформація: ", "Información que añadiste: ", "Informations que vous avez ajoutées : ", "Von dir ergänzte Angaben: "],
    "Do potwierdzenia: ": ["To confirm: ", "Требует подтверждения: ", "Потрібно підтвердити: ", "Pendiente de confirmar: ", "À confirmer : ", "Zu bestätigen: "],
    "Sprawdź dane. Zapis nastąpi dopiero po wybraniu „Zatwierdź i zapisz”.": [
        "Review the details. They will be saved only after you select “Approve and save”.",
        "Проверьте данные. Они будут сохранены только после нажатия «Подтвердить и сохранить».",
        "Перевірте дані. Їх буде збережено лише після натискання «Підтвердити й зберегти».",
        "Revisa los datos. Solo se guardarán cuando selecciones «Aprobar y guardar».",
        "Vérifiez les informations. Elles ne seront enregistrées qu’après avoir choisi « Valider et enregistrer ».",
        "Prüfe die Angaben. Sie werden erst gespeichert, wenn du „Bestätigen und speichern“ auswählst.",
    ],
}
for _source, _values in _UI_COVERAGE_PATCH.items():
    UI_PHRASES[_source] = dict(zip(("en", "ru", "uk", "es", "fr", "de"), _values))

# Menus for choosing a local CV or a saved candidate profile.
_PROFILE_MANAGER_LABELS = {
    "pl": "🧑‍💼 Zarządzanie profilem kandydata",
    "en": "🧑‍💼 Manage candidate profiles",
    "ru": "🧑‍💼 Управление профилями кандидата",
    "uk": "🧑‍💼 Керування профілями кандидата",
    "es": "🧑‍💼 Gestionar perfiles de candidato",
    "fr": "🧑‍💼 Gérer les profils candidat",
    "de": "🧑‍💼 Kandidatenprofile verwalten",
}
for _language, _label in _PROFILE_MANAGER_LABELS.items():
    PROFILE_ACTION_LABELS[_language]["profile_manager"] = _label

_PROFILE_MANAGER_PHRASES = {
    "Twoje lokalne CV. Wybierz plik:": [
        "Your local CVs. Select a file:", "Ваши локальные CV. Выберите файл:", "Ваші локальні CV. Виберіть файл:",
        "Tus CV locales. Selecciona un archivo:", "Vos CV locaux. Sélectionnez un fichier :", "Deine lokalen Lebensläufe. Wähle eine Datei:",
    ],
    "Nie ma lokalnie zapisanych plików CV. Wyślij CV w tym czacie, aby je dodać.": [
        "There are no CV files saved locally. Send a CV in this chat to add one.",
        "Локально сохранённых файлов CV нет. Отправьте CV в этот чат, чтобы добавить его.",
        "Локально збережених файлів CV немає. Надішліть CV у цей чат, щоб додати його.",
        "No hay archivos CV guardados localmente. Envía uno en este chat para añadirlo.",
        "Aucun fichier CV n’est enregistré localement. Envoyez-en un dans ce chat pour l’ajouter.",
        "Es sind keine Lebensläufe lokal gespeichert. Sende hier einen, um ihn hinzuzufügen.",
    ],
    "Nie ma jeszcze zapisanych profili kandydata.": [
        "There are no saved candidate profiles yet.", "Пока нет сохранённых профилей кандидата.", "Збережених профілів кандидата ще немає.",
        "Aún no hay perfiles de candidato guardados.", "Aucun profil candidat n’est encore enregistré.", "Es sind noch keine Kandidatenprofile gespeichert.",
    ],
    "Profile kandydatów. Wybierz profil do zarządzania:": [
        "Candidate profiles. Select a profile to manage:", "Профили кандидата. Выберите профиль для управления:", "Профілі кандидата. Виберіть профіль для керування:",
        "Perfiles de candidato. Selecciona uno para gestionarlo:", "Profils candidat. Sélectionnez un profil à gérer :", "Kandidatenprofile. Wähle ein Profil zur Verwaltung:",
    ],
    "Używaj do wyszukiwania ofert": [
        "Use for job searches", "Использовать для поиска вакансий", "Використовувати для пошуку вакансій",
        "Usar para buscar ofertas", "Utiliser pour rechercher des offres", "Für die Stellensuche verwenden",
    ],
    "🔙 Lista CV": ["🔙 CV list", "🔙 Список CV", "🔙 Список CV", "🔙 Lista de CV", "🔙 Liste des CV", "🔙 CV-Liste"],
    "🔙 Lista profili": ["🔙 Profile list", "🔙 Список профилей", "🔙 Список профілів", "🔙 Lista de perfiles", "🔙 Liste des profils", "🔙 Profilliste"],
    "Usuń CV": ["Delete CV", "Удалить CV", "Видалити CV", "Eliminar CV", "Supprimer le CV", "Lebenslauf löschen"],
    "Stwórz profil z CV jeszcze raz": [
        "Create a profile from this CV again", "Повторно создать профиль по этому CV", "Створити профіль із цього CV ще раз",
        "Crear un perfil de nuevo a partir de este CV", "Recréer un profil à partir de ce CV", "Aus diesem Lebenslauf erneut ein Profil erstellen",
    ],
    "Potwierdź usunięcie CV": ["Confirm CV deletion", "Подтвердить удаление CV", "Підтвердити видалення CV", "Confirmar eliminación del CV", "Confirmer la suppression du CV", "Löschen des Lebenslaufs bestätigen"],
    "Potwierdź usunięcie profilu": ["Confirm profile deletion", "Подтвердить удаление профиля", "Підтвердити видалення профілю", "Confirmar eliminación del perfil", "Confirmer la suppression du profil", "Löschen des Profils bestätigen"],
    "Usunąć wybrany profil kandydata? Oryginalny plik CV pozostanie lokalnie.": [
        "Delete the selected candidate profile? The original CV file will remain stored locally.",
        "Удалить выбранный профиль кандидата? Исходный файл CV останется локально.",
        "Видалити вибраний профіль кандидата? Оригінальний файл CV залишиться локально.",
        "¿Eliminar el perfil seleccionado? El archivo CV original seguirá guardado localmente.",
        "Supprimer le profil sélectionné ? Le fichier CV d’origine restera enregistré localement.",
        "Das ausgewählte Kandidatenprofil löschen? Die ursprüngliche CV-Datei bleibt lokal gespeichert.",
    ],
    "Profil kandydata został usunięty.": ["Candidate profile deleted.", "Профиль кандидата удалён.", "Профіль кандидата видалено.", "Perfil de candidato eliminado.", "Profil candidat supprimé.", "Kandidatenprofil gelöscht."],
    "Nie udało się usunąć profilu.": ["Couldn't delete the profile.", "Не удалось удалить профиль.", "Не вдалося видалити профіль.", "No se pudo eliminar el perfil.", "Impossible de supprimer le profil.", "Das Profil konnte nicht gelöscht werden."],
}
for _source, _translations in _PROFILE_MANAGER_PHRASES.items():
    UI_PHRASES[_source] = dict(zip(("en", "ru", "uk", "es", "fr", "de"), _translations))

UI_FORMATS["selected_cv"] = {
    "pl": "Wybrane CV: {filename}", "en": "Selected CV: {filename}", "ru": "Выбрано CV: {filename}",
    "uk": "Вибране CV: {filename}", "es": "CV seleccionado: {filename}", "fr": "CV sélectionné : {filename}",
    "de": "Ausgewählter Lebenslauf: {filename}",
}
UI_FORMATS["selected_profile"] = {
    "pl": "Wybrany profil kandydata: {name}", "en": "Selected candidate profile: {name}",
    "ru": "Выбранный профиль кандидата: {name}", "uk": "Вибраний профіль кандидата: {name}",
    "es": "Perfil de candidato seleccionado: {name}", "fr": "Profil candidat sélectionné : {name}",
    "de": "Ausgewähltes Kandidatenprofil: {name}",
}

_SEARCH_PROFILE_LABELS = {
    "Dopasowuję nazwy stanowisk i miast do zapisu używanego przez Pracuj.pl…": [
        "Matching job titles and city names to the format used by Pracuj.pl…", "Подбираю названия должностей и городов в формате Pracuj.pl…", "Добираю назви посад і міст до формату Pracuj.pl…", "Adaptando los puestos y las ciudades al formato de Pracuj.pl…", "Adaptation des intitulés de poste et des villes au format de Pracuj.pl…", "Ich gleiche Berufs- und Städtenamen an das Format von Pracuj.pl an…"],
    "Dane kontaktowe": ["Contact details", "Контактные данные", "Контактні дані", "Datos de contacto", "Coordonnées", "Kontaktdaten"],
    "Doświadczenie zawodowe": ["Work experience", "Опыт работы", "Досвід роботи", "Experiencia laboral", "Expérience professionnelle", "Berufserfahrung"],
    "Kompetencje i branże": ["Skills and industries", "Навыки и отрасли", "Навички та галузі", "Competencias y sectores", "Compétences et secteurs", "Kompetenzen und Branchen"],
    "Edukacja i certyfikaty": ["Education and certifications", "Образование и сертификаты", "Освіта та сертифікати", "Educación y certificaciones", "Formation et certifications", "Ausbildung und Zertifikate"],
    "Języki": ["Languages", "Языки", "Мови", "Idiomas", "Langues", "Sprachen"],
    "Preferencje wyszukiwania": ["Search preferences", "Предпочтения поиска", "Налаштування пошуку", "Preferencias de búsqueda", "Préférences de recherche", "Suchpräferenzen"],
    "Kategorie profilu": ["Profile categories", "Категории профиля", "Категорії профілю", "Categorías del perfil", "Catégories du profil", "Profilkategorien"],
    "Do uzupełnienia": ["To be completed", "Нужно заполнить", "Потрібно заповнити", "Pendiente de completar", "À compléter", "Noch auszufüllen"],
    "Preferowany tryb pracy": ["Preferred work mode", "Предпочтительный формат работы", "Бажаний формат роботи", "Modalidad de trabajo preferida", "Mode de travail préféré", "Bevorzugtes Arbeitsmodell"],
    "Preferowane miasta": ["Preferred cities", "Предпочитаемые города", "Бажані міста", "Ciudades preferidas", "Villes préférées", "Bevorzugte Städte"],
    "Preferowane typy umowy": ["Preferred contract types", "Предпочитаемые типы договора", "Бажані типи договору", "Tipos de contrato preferidos", "Types de contrat préférés", "Bevorzugte Vertragsarten"],
    "Oczekiwania finansowe": ["Salary expectations", "Финансовые ожидания", "Фінансові очікування", "Expectativas salariales", "Prétentions salariales", "Gehaltsvorstellungen"],
    "Forma zatrudnienia": ["Contract type", "Тип договора", "Тип договору", "Tipo de contrato", "Type de contrat", "Vertragsart"],
    "Wynagrodzenie": ["Salary", "Зарплата", "Зарплата", "Salario", "Salaire", "Gehalt"],
    "Tryb pracy": ["Work mode", "Формат работы", "Формат роботи", "Modalidad", "Mode de travail", "Arbeitsmodell"],
    "Jaki tryb pracy preferujesz: zdalny, hybrydowy czy stacjonarny? Możesz odpowiedzieć „dowolny”.": [
        "Which work mode do you prefer: remote, hybrid, or on-site? You can answer “any”.", "Какой формат работы вы предпочитаете: удалённый, гибридный или офисный? Можно ответить «любой».", "Який формат роботи ви обираєте: віддалений, гібридний чи офісний? Можна відповісти «будь-який».", "¿Qué modalidad prefieres: remota, híbrida o presencial? Puedes responder «cualquiera».", "Quel mode préférez-vous : à distance, hybride ou sur site ? Vous pouvez répondre « indifférent ».", "Welches Arbeitsmodell bevorzugst du: remote, hybrid oder vor Ort? Du kannst „egal“ antworten."],
    "W jakich miastach chcesz pracować stacjonarnie lub hybrydowo? Wpisz miasta oddzielone przecinkami albo „pomiń”.": [
        "In which cities would you work on-site or hybrid? Separate cities with commas, or answer “skip”.", "В каких городах вы готовы работать в офисе или в гибридном формате? Перечислите через запятую или ответьте «пропустить».", "У яких містах ви готові працювати в офісі або гібридно? Перелічіть через кому або напишіть «пропустити».", "¿En qué ciudades trabajarías presencialmente o en modalidad híbrida? Sepáralas con comas o responde «omitir».", "Dans quelles villes accepteriez-vous un travail sur site ou hybride ? Séparez-les par des virgules ou répondez « ignorer ».", "In welchen Städten würdest du vor Ort oder hybrid arbeiten? Städte durch Kommas trennen oder „überspringen“ schreiben."],
    "Jakie typy umowy preferujesz? Wpisz odpowiedź albo „pomiń”.": [
        "Which contract types do you prefer? Enter your answer or “skip”.", "Какие типы договора вы предпочитаете? Напишите ответ или «пропустить».", "Які типи договору ви обираєте? Напишіть відповідь або «пропустити».", "¿Qué tipos de contrato prefieres? Escribe tu respuesta o «omitir».", "Quels types de contrat préférez-vous ? Répondez ou écrivez « ignorer ».", "Welche Vertragsarten bevorzugst du? Antworte oder schreibe „überspringen“."],
    "Jakie są Twoje oczekiwania finansowe? Wpisz kwotę i walutę albo „pomiń”.": [
        "What are your salary expectations? Enter an amount and currency or “skip”.", "Каковы ваши финансовые ожидания? Укажите сумму и валюту или «пропустить».", "Які ваші фінансові очікування? Вкажіть суму й валюту або «пропустити».", "¿Cuáles son tus expectativas salariales? Indica importe y moneda u «omitir».", "Quelles sont vos prétentions salariales ? Indiquez le montant et la devise ou « ignorer ».", "Wie sind deine Gehaltsvorstellungen? Betrag und Währung angeben oder „überspringen“."],
    "Jakie dodatkowe informacje mam dopisać do profilu? Możesz też wpisać „pomiń”.": [
        "What additional information should I add to your profile? You can also answer “skip”.", "Какие дополнительные сведения добавить в профиль? Можно ответить «пропустить».", "Яку додаткову інформацію додати до профілю? Можна відповісти «пропустити».", "¿Qué información adicional debo añadir al perfil? También puedes responder «omitir».", "Quelles informations complémentaires dois-je ajouter au profil ? Vous pouvez répondre « ignorer ».", "Welche zusätzlichen Angaben soll ich zum Profil hinzufügen? Du kannst auch „überspringen“ antworten."],
    "Odpowiadaj po kolei. Wpisz „pomiń”, aby pominąć pytanie, albo /cancel, aby anulować.": [
        "Answer one question at a time. Type “skip” to skip a question, or /cancel to cancel.", "Отвечайте по очереди. Напишите «пропустить», чтобы пропустить вопрос, или /cancel для отмены.", "Відповідайте по черзі. Напишіть «пропустити», щоб пропустити запитання, або /cancel для скасування.", "Responde una pregunta a la vez. Escribe «omitir» para saltarla o /cancel para cancelar.", "Répondez aux questions une par une. Écrivez « ignorer » pour passer ou /cancel pour annuler.", "Beantworte die Fragen der Reihe nach. Schreibe „überspringen“ oder /cancel zum Abbrechen."],
    "Wyślij odpowiedź tekstową albo /cancel.": ["Send a text answer or /cancel.", "Отправьте текстовый ответ или /cancel.", "Надішліть текстову відповідь або /cancel.", "Envía una respuesta de texto o /cancel.", "Envoyez une réponse textuelle ou /cancel.", "Sende eine Textantwort oder /cancel."],
    "Zapisz uzupełnienie": ["Save profile updates", "Сохранить дополнения", "Зберегти доповнення", "Guardar cambios del perfil", "Enregistrer les compléments", "Ergänzungen speichern"],
    "Nie udało się pobrać ofert z Pracuj.pl. Portal może blokować automatyczny odczyt albo nie ma wyników dla tych stanowisk.": [
        "Couldn't retrieve offers from Pracuj.pl. The portal may be blocking automated access, or there are no results for these roles.", "Не удалось получить вакансии с Pracuj.pl. Портал может блокировать автоматический доступ либо вакансий по этим должностям нет.", "Не вдалося отримати вакансії з Pracuj.pl. Портал може блокувати автоматичний доступ або вакансій за цими посадами немає.", "No se pudieron obtener ofertas de Pracuj.pl. El portal puede bloquear el acceso automático o no hay resultados para esos puestos.", "Impossible de récupérer les offres de Pracuj.pl. Le portail bloque peut-être l’accès automatisé ou aucun résultat ne correspond.", "Angebote von Pracuj.pl konnten nicht abgerufen werden. Das Portal blockiert möglicherweise automatisierte Zugriffe oder es gibt keine Treffer."],
    "Nie udało się pobrać lub ocenić ofert. Sprawdź połączenie i spróbuj ponownie.": [
        "Couldn't retrieve or assess the offers. Check the connection and try again.", "Не удалось получить или оценить вакансии. Проверьте соединение и повторите попытку.", "Не вдалося отримати або оцінити вакансії. Перевірте з’єднання та спробуйте ще раз.", "No se pudieron obtener o evaluar las ofertas. Comprueba la conexión e inténtalo de nuevo.", "Impossible de récupérer ou d’évaluer les offres. Vérifiez la connexion et réessayez.", "Angebote konnten nicht abgerufen oder bewertet werden. Prüfe die Verbindung und versuche es erneut."],
    "Pracuj.pl ograniczył liczbę żądań. Poczekaj chwilę przed kolejnym wyszukiwaniem.": [
        "Pracuj.pl has limited the number of requests. Wait a little before searching again.", "Pracuj.pl ограничил количество запросов. Подождите немного перед следующим поиском.", "Pracuj.pl обмежив кількість запитів. Зачекайте трохи перед наступним пошуком.", "Pracuj.pl ha limitado el número de solicitudes. Espera un poco antes de volver a buscar.", "Pracuj.pl a limité le nombre de requêtes. Attendez un peu avant de relancer la recherche.", "Pracuj.pl hat die Anzahl der Anfragen begrenzt. Warte kurz, bevor du erneut suchst."],
    "Pracuj.pl ograniczył liczbę żądań. Pokazuję dotychczas zebrane oferty; spróbuj ponownie później.": [
        "Pracuj.pl has limited the number of requests. Showing the offers collected so far; try again later.", "Pracuj.pl ограничил количество запросов. Показываю уже найденные вакансии; попробуйте позже.", "Pracuj.pl обмежив кількість запитів. Показую вже зібрані вакансії; спробуйте пізніше.", "Pracuj.pl ha limitado el número de solicitudes. Se muestran las ofertas reunidas; inténtalo más tarde.", "Pracuj.pl a limité le nombre de requêtes. Voici les offres déjà recueillies ; réessayez plus tard.", "Pracuj.pl hat die Anzahl der Anfragen begrenzt. Bisher gefundene Stellen werden angezeigt; versuche es später erneut."],
}
for _source, _values in _SEARCH_PROFILE_LABELS.items():
    UI_PHRASES[_source] = dict(zip(("en", "ru", "uk", "es", "fr", "de"), _values))

UI_PHRASES.update({
    "Wyszukiwanie i ocena dopasowań zostały zatrzymane.": {
        "en": "Job search and match assessment have been stopped.",
        "ru": "Поиск вакансий и оценка соответствия остановлены.",
        "uk": "Пошук вакансій та оцінювання відповідності зупинено.",
        "es": "Se detuvieron la búsqueda de ofertas y la evaluación de compatibilidad.",
        "fr": "La recherche d’offres et l’évaluation de la correspondance ont été arrêtées.",
        "de": "Die Stellensuche und die Bewertung der Passgenauigkeit wurden gestoppt.",
    },
    "Wyszukiwanie już trwa. Zatrzymaj je przed uruchomieniem kolejnego.": {
        "en": "A search is already running. Stop it before starting another one.",
        "ru": "Поиск уже выполняется. Остановите его, прежде чем запускать новый.",
        "uk": "Пошук уже триває. Зупиніть його, перш ніж запускати новий.",
        "es": "Ya hay una búsqueda en curso. Deténla antes de iniciar otra.",
        "fr": "Une recherche est déjà en cours. Arrêtez-la avant d’en lancer une autre.",
        "de": "Eine Suche läuft bereits. Stoppe sie, bevor du eine neue startest.",
    },
    "Firma niepodana": {
        "en": "Company not provided", "ru": "Компания не указана", "uk": "Компанію не вказано",
        "es": "Empresa no indicada", "fr": "Entreprise non indiquée", "de": "Unternehmen nicht angegeben",
    },
    "Lokalizacja niepodana": {
        "en": "Location not provided", "ru": "Местоположение не указано", "uk": "Місце розташування не вказано",
        "es": "Ubicación no indicada", "fr": "Lieu non indiqué", "de": "Standort nicht angegeben",
    },
    "Data publikacji": {
        "en": "Posted", "ru": "Опубликовано", "uk": "Опубліковано",
        "es": "Publicado", "fr": "Publié le", "de": "Veröffentlicht",
    },
    "Aby przejść do pól formularza dla wybranej oferty, użyj /apply ID_OFERTY. Aplikację wysyłasz samodzielnie.": {
        "en": "To review the application fields for a selected job, use /apply JOB_ID. You submit the application yourself.",
        "ru": "Чтобы посмотреть поля формы выбранной вакансии, используйте /apply ID_ВАКАНСИИ. Заявку вы отправляете самостоятельно.",
        "uk": "Щоб переглянути поля форми обраної вакансії, скористайтеся /apply ID_ВАКАНСІЇ. Заявку ви надсилаєте самостійно.",
        "es": "Para revisar los campos del formulario de una oferta seleccionada, usa /apply ID_OFERTA. Tú envías la solicitud.",
        "fr": "Pour consulter les champs du formulaire d’une offre sélectionnée, utilisez /apply ID_OFFRE. Vous envoyez vous-même la candidature.",
        "de": "Um die Formularfelder einer ausgewählten Stelle zu prüfen, verwende /apply JOB_ID. Du sendest die Bewerbung selbst ab.",
    },
    "Profil powiązany pozostanie zapisany, ale nie będzie można ponownie odczytać jego źródłowego CV.": {
        "en": "The linked profile will remain saved, but its source CV can no longer be read again.",
        "ru": "Связанный профиль останется сохранённым, но исходное CV больше нельзя будет прочитать повторно.",
        "uk": "Пов’язаний профіль залишиться збереженим, але вихідне CV більше не можна буде прочитати повторно.",
        "es": "El perfil vinculado seguirá guardado, pero ya no se podrá volver a leer su CV de origen.",
        "fr": "Le profil associé restera enregistré, mais son CV source ne pourra plus être lu à nouveau.",
        "de": "Das verknüpfte Profil bleibt gespeichert, aber der ursprüngliche Lebenslauf kann nicht erneut eingelesen werden.",
    },
    "Oferta prowadzi do zewnętrznego systemu rekrutacyjnego.": {
        "en": "This job opens an external recruitment system.",
        "ru": "Вакансия ведёт во внешнюю систему подбора персонала.",
        "uk": "Вакансія веде до зовнішньої системи рекрутингу.",
        "es": "Esta oferta abre un sistema de selección externo.",
        "fr": "Cette offre mène à un système de recrutement externe.",
        "de": "Diese Stelle führt zu einem externen Bewerbungssystem.",
    },
    "Formularz wymaga logowania albo portal odmówił dostępu.": {
        "en": "The form requires sign-in, or the portal denied access.",
        "ru": "Форма требует входа в систему, либо портал отказал в доступе.",
        "uk": "Форма потребує входу або портал відмовив у доступі.",
        "es": "El formulario requiere iniciar sesión o el portal denegó el acceso.",
        "fr": "Le formulaire nécessite une connexion ou le portail a refusé l’accès.",
        "de": "Das Formular erfordert eine Anmeldung oder das Portal hat den Zugriff verweigert.",
    },
    "Formularz jest ładowany dynamicznie albo wymaga logowania.": {
        "en": "The form loads dynamically or requires sign-in.",
        "ru": "Форма загружается динамически или требует входа в систему.",
        "uk": "Форма завантажується динамічно або потребує входу.",
        "es": "El formulario se carga dinámicamente o requiere iniciar sesión.",
        "fr": "Le formulaire se charge de façon dynamique ou nécessite une connexion.",
        "de": "Das Formular wird dynamisch geladen oder erfordert eine Anmeldung.",
    },
    "Strona formularza przekracza limit odczytu.": {
        "en": "The application form page exceeds the reading limit.",
        "ru": "Страница формы превышает допустимый объём чтения.",
        "uk": "Сторінка форми перевищує обмеження на обсяг зчитування.",
        "es": "La página del formulario supera el límite de lectura.",
        "fr": "La page du formulaire dépasse la limite de lecture.",
        "de": "Die Formularseite überschreitet das Leselimit.",
    },
    "Nie udało się odczytać publicznego formularza.": {
        "en": "Couldn't read the public application form.",
        "ru": "Не удалось прочитать открытую форму заявки.",
        "uk": "Не вдалося прочитати відкриту форму заявки.",
        "es": "No se pudo leer el formulario público de solicitud.",
        "fr": "Impossible de lire le formulaire public de candidature.",
        "de": "Das öffentliche Bewerbungsformular konnte nicht gelesen werden.",
    },
})
