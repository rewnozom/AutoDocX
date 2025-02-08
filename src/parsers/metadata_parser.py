# src/parsers/metadata_parser.py
import os
import time

class MetadataParser:
    """
    Samlar metadata om en given fil.

    Metadata kan inkludera filstorlek, skapelse- och ändringstider med mera.
    """

    def parse_metadata(self, file_path):
        """
        Returnerar ett dictionary med metadata för den angivna filen.
        """
        metadata = {}
        try:
            stats = os.stat(file_path)
            metadata["file_size"] = stats.st_size
            metadata["last_modified"] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime(stats.st_mtime)
            )
            metadata["last_accessed"] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime(stats.st_atime)
            )
            metadata["creation_time"] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime(stats.st_ctime)
            )
        except Exception as e:
            metadata["error"] = f"Fel vid hämtning av metadata: {e}"
        return metadata

if __name__ == "__main__":
    parser = MetadataParser()
    sample_file = __file__  # Testa med detta script
    meta = parser.parse_metadata(sample_file)
    print("Metadata för filen:")
    for key, value in meta.items():
        print(f"{key}: {value}")
