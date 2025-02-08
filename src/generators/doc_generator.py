# src/generators/doc_generator.py
import os
from ..helpers.logger import Logger
from ..helpers.file_operations import write_file

class DocGenerator:
    """
    Sammanställer enskilda fil-dokumentationer till en enhetlig dokumentation.
    Integrerar data från parsers, AI-svar och formaterare.
    """

    def __init__(self):
        self.documents = {}

    def add_document(self, file_path, doc_content):
        """
        Lägger till genererad dokumentation för en specifik fil.
        """
        self.documents[file_path] = doc_content
        Logger.log(f"Dokumentation tillagd för: {file_path}", "SUCCESS")

    def generate_aggregate(self, output_path):
        """
        Sammanställer all enskild dokumentation till en aggregerad fil.
        """
        aggregated_content = ""
        for file_path, content in self.documents.items():
            aggregated_content += f"# Dokumentation för {file_path}\n\n{content}\n\n"
        write_file(output_path, aggregated_content)
        return aggregated_content

if __name__ == "__main__":
    generator = DocGenerator()
    generator.add_document("example.py", "Detta är en exempel dokumentation.")
    agg = generator.generate_aggregate("docs/Temp/Developer-Docs/example.md")
    print("Aggregerad dokumentation genererad.")
