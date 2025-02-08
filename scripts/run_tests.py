#!/usr/bin/env python3
"""
run_tests.py - Kör enhetstester för AutoDocX.
"""
import subprocess


def main():
    print("Kör tester med pytest...")
    subprocess.run(["pytest", "--maxfail=1", "--disable-warnings", "-q"])


if __name__ == "__main__":
    main()
