#!/usr/bin/env python3
"""
deploy.py - Script för att distribuera AutoDocX.
Exempel:
    python scripts/deploy.py
"""
import os
import subprocess
import sys


def run_command(command, error_message="Ett fel uppstod"):
    """Kör ett kommando och hantera eventuella fel."""
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {error_message}")
        print(f"Kommando som misslyckades: {' '.join(command)}")
        print(f"Returkod: {e.returncode}")
        sys.exit(1)


def main():
    print("Distribuerar AutoDocX...")
    
    # Rensa gamla builds
    if os.path.exists("dist"):
        print("Rensar gamla distributioner...")
        for file in os.listdir("dist"):
            os.remove(os.path.join("dist", file))
    
    # Bygg både source distribution och wheel
    print("Bygger distributionspaket...")
    run_command(
        ["python", "-m", "build"],
        "Kunde inte bygga distributionspaket"
    )
    
    print("Distribution skapad i ./dist/")
    print("\nFör att publicera till PyPI, kör:")
    print("python -m twine upload dist/*")


if __name__ == "__main__":
    main()