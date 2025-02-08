import os
import ast


class FileAnalyzer:
    """
    Analyserar enskilda filer för att extrahera funktioner, klasser, kommentarer
    och annan metadata. Detta är en placeholder-implementation för Python-filer.
    För icke-Python-filer returneras filens råa innehåll.
    """

    def analyze(self, file_path):
        """
        Analyserar filen och returnerar ett dictionary med resultat.
        Om filen är en Python-fil, används ast för att extrahera funktioner och klasser.
        """
        analysis = {
            "file_path": file_path,
            "functions": [],
            "classes": [],
            "comments": [],
        }
        if file_path.endswith(".py"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                # Parsning av Python-kod med ast
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        analysis["functions"].append(node.name)
                    elif isinstance(node, ast.ClassDef):
                        analysis["classes"].append(node.name)
                # En enkel metod för att extrahera kommentarer
                analysis["comments"] = self._extract_comments(content)
            except Exception as e:
                analysis["error"] = str(e)
        else:
            # För icke-Python-filer: läs in rå innehåll
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    analysis["content"] = f.read()
            except Exception as e:
                analysis["error"] = str(e)
        return analysis

    def _extract_comments(self, content):
        """
        En placeholder-metod för att extrahera kommentarer ur Python-kod.
        """
        comments = []
        for line in content.splitlines():
            line = line.strip()
            if line.startswith("#"):
                comments.append(line)
        return comments


if __name__ == "__main__":
    analyzer = FileAnalyzer()
    # Testa med en exempel-fil (ändra sökväg om nödvändigt)
    result = analyzer.analyze("sample.py")
    print("Analysresultat:", result)
