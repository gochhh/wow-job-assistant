import argparse
import asyncio
import os
import sys
from pathlib import Path

from agents import Agent, Runner

for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8", errors="replace")


def load_api_key_from_env_file() -> None:
    env_file = Path(__file__).with_name(".env")
    if not env_file.exists():
        return
    for raw_line in env_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        name, separator, value = line.partition("=")
        if separator and name.strip() == "OPENAI_API_KEY":
            value = value.strip().strip('"').strip("'")
            if value:
                os.environ.setdefault("OPENAI_API_KEY", value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analizuje treść ogłoszenia o pracę zapisaną w pliku tekstowym."
    )
    parser.add_argument(
        "plik",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("job_offer.txt"),
        help="ścieżka do pliku z treścią ogłoszenia",
    )
    return parser.parse_args()


async def analyze_offer(offer_text: str) -> str:
    agent = Agent(
        name="WOW Job Assistant — analizator ogłoszeń",
        instructions=(
            "Analizujesz ogłoszenia o pracę dla kandydata. Odpowiadaj po polsku. "
            "Korzystaj wyłącznie z informacji zawartych w ogłoszeniu; nie dopowiadaj "
            "brakujących warunków ani nie oceniaj dopasowania kandydata, bo nie podano CV. "
            "Ułóż wynik pod nagłówkami: Stanowisko i warunki; Główne zadania; "
            "Wymagania konieczne; Mile widziane; Niepodane lub niejasne informacje. "
            "Zachowaj rozróżnienie między wymaganiami koniecznymi a dodatkowymi."
        ),
        model="gpt-4.1-mini",
    )
    result = await Runner.run(agent, f"Przeanalizuj to ogłoszenie:\n\n{offer_text}")
    return result.final_output


def main() -> int:
    load_api_key_from_env_file()
    if not os.environ.get("OPENAI_API_KEY"):
        print("Brak OPENAI_API_KEY. Uzupełnij lokalny plik .env.")
        return 1

    args = parse_args()
    if not args.plik.is_file():
        print(
            f"Nie znaleziono pliku: {args.plik}\n"
            "Zapisz treść ogłoszenia w job_offer.txt albo podaj ścieżkę jako argument."
        )
        return 2

    offer_text = args.plik.read_text(encoding="utf-8").strip()
    if not offer_text:
        print(f"Plik {args.plik} jest pusty.")
        return 2

    print(asyncio.run(analyze_offer(offer_text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
