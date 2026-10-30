# WOW Job Assistant

Telegramowy asystent rekrutacyjny: zapisuje CV lokalnie, przygotowuje profil po zgodzie użytkownika, pomaga wyszukiwać i oceniać oferty Pracuj.pl oraz przygotowuje szkice odpowiedzi do aplikacji.

## Konfiguracja

Dodaj lokalnie do pliku `.env` wartości `OPENAI_API_KEY`, `TELEGRAM_BOT_TOKEN` i `TELEGRAM_OWNER_ID`. Plik jest ignorowany przez Git. Nie umieszczaj kluczy w kodzie.

Windows PowerShell:
1. `python -m venv .venv`
2. `.\.venv\Scripts\Activate.ps1`
3. `python -m pip install -r requirements.txt`
4. `python bot.py`

Bot przyjmuje CV PDF, DOCX i TXT (do 15 MB). Oryginały i profile są przechowywane lokalnie w `data/`. Wysyłka tekstu CV do OpenAI rozpoczyna się dopiero po osobnej zgodzie w Telegramie. Bot nie wysyła aplikacji za użytkownika.

Nie uruchamiaj drugiej instancji bota z tym samym tokenem równolegle.
