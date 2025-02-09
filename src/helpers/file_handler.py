# src/helpers/file_handler.py
from ..parsers import code_parser, comment_extractor, metadata_parser


class FileHandler:
    """
    Hanterar inläsning och parsing av filer baserat på filtyp.
    För Python-filer används CodeParser, CommentExtractor och MetadataParser.
    För andra filtyper returneras rå text.
    """

    def __init__(self):
        self.code_parser = code_parser.CodeParser()
        self.comment_extractor = comment_extractor.CommentExtractor()
        self.metadata_parser = metadata_parser.MetadataParser()

    def process_file(self, file_path):
        result = {"file_path": file_path}
        if file_path.endswith(".py"):
            parsed = self.code_parser.parse(file_path)
            comments = self.comment_extractor.extract_comments(file_path)
            metadata = self.metadata_parser.parse_metadata(file_path)
            result.update(
                {
                    "ast": parsed.get("ast"),
                    "raw": parsed.get("raw"),
                    "comments": comments,
                    "metadata": metadata,
                }
            )
        else:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    result["raw"] = f.read()
            except Exception as e:
                result["error"] = str(e)
        return result


if __name__ == "__main__":
    handler = FileHandler()
    print(handler.process_file(__file__))
