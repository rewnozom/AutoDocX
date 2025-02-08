#!/usr/bin/env python3
"""
deploy.py - Script för att distribuera AutoDocX.
Exempel:
    python scripts/deploy.py
"""
import subprocess

def main():
    print("Distribuerar AutoDocX...")
    # Placeholder: Lägg till distributionslogik här (t.ex. bygga distributionspaket med setup.py)
    subprocess.run(["python", "setup.py", "sdist"])
    print("Distribueringen är klar.")

if __name__ == "__main__":
    main()
