# src/validators/validator_manager.py
from .syntax_checker import check_syntax
from .doc_consistency import check_consistency

class ValidatorManager:
    """
    Hanterar körning av olika validatorer på genererad dokumentation.
    """
    def __init__(self):
        pass

    def run_validators(self, code_path, doc_path):
        syntax_status, syntax_msg = check_syntax(doc_path)
        consistency_status, consistency_msg = check_consistency(code_path, doc_path)
        return {
            "syntax": {"status": syntax_status, "message": syntax_msg},
            "consistency": {"status": consistency_status, "message": consistency_msg}
        }

if __name__ == "__main__":
    vm = ValidatorManager()
    results = vm.run_validators("src/sample.py", "docs/Developer-Docs/sample.md")
    print("Validator resultat:", results)
