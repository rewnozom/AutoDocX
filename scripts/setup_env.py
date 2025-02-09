#!/usr/bin/env python3
"""
setup_env.py - Script för att sätta upp utvecklingsmiljön för AutoDocX.
Exempel:
    python scripts/setup_env.py
"""
import argparse
import os
import subprocess
import sys
from typing import List


def run_command(command: List[str], error_message: str = "Ett fel uppstod") -> None:
    """Kör ett kommando och hantera eventuella fel."""
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {error_message}")
        print(f"Kommando som misslyckades: {' '.join(command)}")
        print(f"Returkod: {e.returncode}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Sätt upp utvecklingsmiljön för AutoDocX"
    )
    parser.add_argument(
        "--dev",
        action="store_true",
        help="Installera utvecklingsverktyg",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Rensa befintlig installation först",
    )
    args = parser.parse_args()

    print("Sätter upp utvecklingsmiljön för AutoDocX...")

    # Uppgradera pip
    run_command(
        ["python", "-m", "pip", "install", "--upgrade", "pip"],
        "Kunde inte uppgradera pip"
    )

    if args.clean:
        print("Rensar befintlig installation...")
        run_command(
            ["pip", "uninstall", "-y", "AutoDocX"],
            "Kunde inte avinstallera AutoDocX"
        )

    # Installera beroenden
    if args.dev:
        print("Installerar med utvecklingsverktyg...")
        run_command(
            ["pip", "install", "-e", ".[dev]"],
            "Kunde inte installera utvecklingsberoenden"
        )
    else:
        print("Installerar baskrav...")
        run_command(
            ["pip", "install", "-e", "."],
            "Kunde inte installera beroenden"
        )

    # Skapa nödvändiga mappar
    directories = ["Workspace", "docs", "logs"]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Skapade mapp: {directory}")

    print("\nUtvecklingsmiljön är nu inställd!")
    print("\nFör att börja använda AutoDocX:")
    print("1. Skapa en .env fil (om den inte redan finns)")
    print("2. Lägg din kod i ./Workspace mappen")
    print("3. Kör: docx ./Workspace -update")


if __name__ == "__main__":
    main()