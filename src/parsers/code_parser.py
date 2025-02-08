import ast


class CodeParser:
    """
    Läser och tolkar kodfiler.

    Om filen är en Python-fil används ast för att skapa ett abstrakt syntaxträd (AST).
    För andra filtyper kan man implementera andra metoder eller returnera rå text.
    """

    def parse(self, file_path):
        """
        Parsar en given fil och returnerar en struktur med tolkade data.

        Returnerar ett dictionary med:
            - "ast": AST-träd för Python-filer, annars None.
            - "raw": Rå textinnehåll om filen inte är Python.
        """
        result = {"ast": None, "raw": None}
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            if file_path.endswith(".py"):
                try:
                    tree = ast.parse(content)
                    result["ast"] = tree
                except Exception as e:
                    result["ast"] = None
                    result["error"] = f"AST-parsing misslyckades: {e}"
            else:
                result["raw"] = content
        except Exception as e:
            result["error"] = f"Fel vid läsning: {e}"
        return result


if __name__ == "__main__":
    parser = CodeParser()
    sample_file = __file__  # Testa med detta script (detta är en Python-fil)
    parsed = parser.parse(sample_file)
    print("Parsed resultat:", parsed)
