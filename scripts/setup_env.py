#!/usr/bin/env python3
"""
setup_env.py - Script för att sätta upp utvecklingsmiljön för AutoDocX.
Exempel:
    python scripts/setup_env.py
"""
import os
import subprocess

def main():
    print("Sätter upp utvecklingsmiljön för AutoDocX...")
    # Exempel: Installera beroenden
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    print("Utvecklingsmiljön är nu inställd.")

if __name__ == "__main__":
    main()
