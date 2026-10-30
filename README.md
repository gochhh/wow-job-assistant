# WOW Job Assistant

Telegramowy asystent rekrutacyjny: zapisuje CV lokalnie, przygotowuje profil po zgodzie użytkownika, pomaga wyszukiwać i oceniać oferty Pracuj.pl oraz przygotowuje szkice odpowiedzi do aplikacji.

## Konfiguracja

Dodaj lokalnie do pliku `.env` wartości `OPENAI_API_KEY` i `TELEGRAM_BOT_TOKEN`. Plik jest ignorowany przez Git. Nie umieszczaj kluczy w kodzie. `TELEGRAM_OWNER_ID` nie jest wymagany do normalnej pracy; jest używany wyłącznie do przypisania danych z dawnego układu podczas migracji.

Windows PowerShell:
1. `python -m venv .venv`
2. `.\.venv\Scripts\Activate.ps1`
3. `python -m pip install -r requirements.txt`
4. `python bot.py`

Bot przyjmuje CV PDF, DOCX i TXT (do 15 MB). Każdy użytkownik ma własny katalog `data/users/<telegram_user_id>/`, zawierający jego CV, profile, oferty, cache i ustawienia. Wszystkie operacje bota są ograniczone do identyfikatora użytkownika z prywatnego czatu Telegrama; wiadomości z grup nie uruchamiają funkcji. Na systemach POSIX katalog użytkownika otrzymuje uprawnienia `0700`.

CV i profile są trwałymi danymi osobowymi przechowywanymi na serwerze. Uprawnienia folderów izolują użytkowników aplikacji, ale administrator serwera i konto systemowe uruchamiające bota nadal mogą odczytać pliki. Wysyłka tekstu CV do OpenAI rozpoczyna się dopiero po osobnej zgodzie użytkownika w Telegramie. Bot nie wysyła aplikacji za użytkownika.

Przy pierwszym uruchomieniu nowa wersja kopiuje stare dane z `data/cv`, `data/profile`, `data/jobs` i ustawienia do katalogu dotychczasowego właściciela, a następnie weryfikuje kopie. Jeśli w tych lokalizacjach są starsze dane, `TELEGRAM_OWNER_ID` musi wskazywać dotychczasowego właściciela (jego ID można uzyskać poleceniem `/id`). Stare kopie pozostają na miejscu jako zabezpieczenie; po sprawdzeniu migracji i wykonaniu kopii zapasowej można je ręcznie usunąć. Przy konflikcie lub błędzie weryfikacji bot zatrzyma start i zachowa źródła.

Użytkownik może usuwać zapisane CV i profile z menu bota. Pełne usunięcie jego danych z serwera obejmuje katalog `data/users/<telegram_user_id>/` oraz kopie zapasowe; wykonuje je administrator serwera po zatrzymaniu bota. Kopie zapasowe należy przechowywać z ograniczonym dostępem i usuwać zgodnie z tą samą procedurą.

Nie uruchamiaj drugiej instancji bota z tym samym tokenem równolegle.
