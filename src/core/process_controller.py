from ..scanners.workspace_scanner import WorkspaceScanner
from ..scanners.file_analyzer import FileAnalyzer
from ..helpers.logger import Logger

class ProcessController:
    def __init__(self):
        self.scanner = WorkspaceScanner(ignore_paths=["node_modules", ".git", "venv"])
        self.analyzer = FileAnalyzer()
    
    def scan_codebase(self, base_path):
        Logger.log(f"Skannar kodbasen i: {base_path}", "INFO")
        file_list = self.scanner.scan(base_path)
        Logger.log(f"Skanning klar. {len(file_list)} filer hittades.", "SUCCESS")
        return file_list
    
    def analyze_file(self, file_path):
        Logger.log(f"Analyserar fil: {file_path}", "INFO")
        result = self.analyzer.analyze(file_path)
        return result
