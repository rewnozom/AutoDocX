# src/generators/formatters/json_formatter.py
import json

def format_json(doc_content):
    """
    Formaterar dokumentationen till JSON-format.
    Placeholder: Returnerar en JSON-sträng med dokumentationen.
    """
    return json.dumps({"documentation": doc_content}, indent=2)

if __name__ == "__main__":
    sample = "Exempel på dokumentation."
    print("JSON format:", format_json(sample))
