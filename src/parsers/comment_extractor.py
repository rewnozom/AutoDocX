# src/parsers/comment_extractor.py
import ast

class CommentExtractor:
    """
    Extraherar kommentarer och docstrings från Python-kod.
    """

    def extract_comments(self, file_path):
        comments = []
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            # Extrahera radrubriker (vanliga kommentarer)
            for line in content.splitlines():
                stripped = line.strip()
                if stripped.startswith("#"):
                    comments.append(stripped)
            # Extrahera docstrings via AST
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
                    doc = ast.get_docstring(node)
                    if doc:
                        comments.append(doc)
        except Exception as e:
            comments.append(f"[ERROR] Kunde inte läsa filen: {e}")
        return comments

if __name__ == "__main__":
    extractor = CommentExtractor()
    sample_file = __file__
    comments = extractor.extract_comments(sample_file)
    print("Extraherade kommentarer:")
    for comment in comments:
        print(comment)
