def check_syntax(file_path):
    """
    Kontrollerar syntaxen i den genererade dokumentationen.
    
    Placeholder-implementation:
      - Verifierar att filen existerar och inte är tom.
      - Här kan man senare integrera med ett Markdown-lintverktyg eller liknande.
      
    Returnerar:
      (bool, str): Status (True om syntaxen är OK, annars False) och ett meddelande.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        if not content.strip():
            return False, "Filen är tom."
        # Placeholder: Ytterligare syntaxkontroll kan läggas till här.
        return True, "Syntax OK."
    except Exception as e:
        return False, f"Fel vid läsning: {e}"

if __name__ == "__main__":
    # Exempel på användning
    test_file = "docs/Developer-Docs/sample.md"  # Justera sökväg vid behov
    status, message = check_syntax(test_file)
    print(f"Syntaxcheck för {{test_file}}: {{status}} - {{message}}")
