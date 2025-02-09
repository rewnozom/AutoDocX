# src/core/process_controller.py
from ..scanners.workspace_scanner import WorkspaceScanner
from ..helpers.file_handler import FileHandler
from ..helpers.logger import Logger
from ..helpers.config_manager import ConfigManager


class ProcessController:
    def __init__(self):
        config = ConfigManager().config
        ignore_paths = config.get("ignore_paths", ["node_modules", ".git", "venv"])
        self.scanner = WorkspaceScanner(ignore_paths=ignore_paths)
        self.file_handler = FileHandler()

    def scan_codebase(self, base_path):
        Logger.log(f"Skannar kodbasen i: {base_path}", "INFO")
        file_list = self.scanner.scan(base_path)
        Logger.log(f"Skanning klar. {len(file_list)} filer hittades.", "SUCCESS")
        return file_list

    def analyze_file(self, file_path):
        Logger.log(f"Analyserar fil: {file_path}", "INFO")
        result = self.file_handler.process_file(file_path)
        return result
