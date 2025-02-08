import os


class WorkspaceScanner:
    """
    Skannar den angivna workspace-sökvägen och identifierar alla mappar och filer.
    Kan konfigureras med ignorerade sökvägar (t.ex. "node_modules", ".git", "venv") via konstruktorn.
    """

    def __init__(self, ignore_paths=None):
        self.ignore_paths = ignore_paths if ignore_paths is not None else []

    def scan(self, base_path):
        """
        Rekursivt skannar base_path och returnerar en lista med filvägar.
        """
        file_paths = []
        for root, dirs, files in os.walk(base_path):
            # Filtrera bort ignorerade mappar
            dirs[:] = [d for d in dirs if not self._is_ignored(os.path.join(root, d))]
            for file in files:
                full_path = os.path.join(root, file)
                if not self._is_ignored(full_path):
                    file_paths.append(full_path)
        return file_paths

    def _is_ignored(self, path):
        """Returnerar True om någon ignorerad sträng finns i path."""
        for pattern in self.ignore_paths:
            if pattern in path:
                return True
        return False


if __name__ == "__main__":
    # Exempelanvändning
    scanner = WorkspaceScanner(ignore_paths=["node_modules", ".git", "venv"])
    files = scanner.scan(".")
    print("Skannade filer:")
    for f in files:
        print(f)
