import re


class CommentExtractor:
    """
    Extraherar kommentarer från kod.

    För Python-filer letar denna implementation efter rader som börjar med '#'.
    Kan utvidgas med stöd för andra språk och kommentarformat.
    """

    def extract_comments(self, file_path):
        """
        Läser filen och returnerar en lista med kommentarer.
        """
        comments = []
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    stripped = line.strip()
                    if stripped.startswith("#"):
                        comments.append(stripped)
        except Exception as e:
            comments.append(f"[ERROR] Kunde inte läsa filen: {e}")
        return comments


if __name__ == "__main__":
    extractor = CommentExtractor()
    sample_file = __file__  # Testa med detta script
    comments = extractor.extract_comments(sample_file)
    print("Extraherade kommentarer:")
    for comment in comments:
        print(comment)
