# src/validators/doc_consistency.py
def check_consistency(code_path, doc_path):
    """
    Säkerställer att dokumentationen överensstämmer med koden.

    Placeholder-implementation:
      - Jämför exempelvis antalet rader i kod och dokumentation.
      - Om dokumentationen har färre än hälften av antalet rader i koden, flagga som inkonsekvent.

    Returnerar:
      (bool, str): Status (True om dokumentationen är konsistent, annars False) och ett meddelande.
    """
    try:
        with open(code_path, "r", encoding="utf-8") as f:
            code_lines = f.readlines()
        with open(doc_path, "r", encoding="utf-8") as f:
            doc_lines = f.readlines()

        if len(doc_lines) < len(code_lines) / 2:
            return False, "Dokumentationen verkar vara ofullständig."
        return True, "Dokumentationen överensstämmer med koden."
    except Exception as e:
        return False, f"Fel vid jämförelse: {e}"


if __name__ == "__main__":
    code_file = "src/sample.py"  # Justera sökväg vid behov
    doc_file = "docs/Developer-Docs/sample.md"  # Justera sökväg vid behov
    status, message = check_consistency(code_file, doc_file)
    print(f"Consistency check: {status} - {message}")
