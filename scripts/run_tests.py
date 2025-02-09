#!/usr/bin/env python3
"""
run_tests.py - Kör enhetstester för AutoDocX.
"""
import argparse
import subprocess
import sys


def run_command(command, error_message="Ett fel uppstod"):
    """Kör ett kommando och hantera eventuella fel."""
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        if e.returncode == 5:  # pytest returnerar 5 när inga tester hittas
            print("VARNING: Inga tester hittades")
            return
        print(f"ERROR: {error_message}")
        print(f"Kommando som misslyckades: {' '.join(command)}")
        print(f"Returkod: {e.returncode}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Kör tester för AutoDocX")
    parser.add_argument("--coverage", action="store_true", help="Kör med kodtäckning")
    parser.add_argument("--lint", action="store_true", help="Kör linting")
    args = parser.parse_args()

    if args.lint:
        print("Kör linting...")
        run_command(
            ["flake8", "--config=.flake8"],
            "Linting misslyckades"
        )
        run_command(
            ["black", "--check", "."],
            "Black formattering misslyckades"
        )
        run_command(
            ["isort", "--check", "."],
            "Import sortering misslyckades"
        )

    print("Kör tester...")
    test_command = ["pytest", "--maxfail=1"]
    
    if not args.coverage:
        test_command.extend(["--disable-warnings", "-q"])
    else:
        test_command.extend([
            "--cov=src",
            "--cov-report=term-missing",
            "--cov-report=html"
        ])
    
    run_command(test_command, "Tester misslyckades")

    if args.coverage:
        print("\nKodtäckningsrapport genererad i htmlcov/index.html")


if __name__ == "__main__":
    main()