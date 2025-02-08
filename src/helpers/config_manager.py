# src/helpers/config_manager.py
import os
import yaml
from ..helpers.logger import Logger

class ConfigManager:
    """
    Hanterar inläsning av konfiguration från config.yaml.
    Om filen inte finns används defaultvärden.
    """
    DEFAULT_CONFIG = {
        "default_llm": "lmstudio",
        "llm": {
            "lmstudio": {
                "context_tokens": 60000,
                "temperature": 0.7,
                "base_url": "http://localhost:1234/v1"
            },
            "openai": {
                "context_tokens": 4000,
                "temperature": 0.8,
                "base_url": "https://api.openai.com/v1"
            }
        },
        "default_path": "./Workspace/",
        "ignore_paths": ["node_modules", ".git", "venv"],
        "prompt_templates": {
            "developer": {
                "full": "Developer-Full-Prompt-Template",
                "sum": "Developer-Summary-Prompt-Template",
                "short": "Developer-Short-Prompt-Template"
            },
            "user": {
                "full": "User-Full-Prompt-Template",
                "sum": "User-Summary-Prompt-Template",
                "short": "User-Short-Prompt-Template"
            },
            "ai": {
                "full": "AI-Full-Prompt-Template",
                "sum": "AI-Summary-Prompt-Template",
                "short": "AI-Short-Prompt-Template"
            }
        }
    }

    def __init__(self, config_path="config.yaml"):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    config = yaml.safe_load(f)
                Logger.log("Konfiguration inläst från config.yaml.", "SUCCESS")
                return config
            except Exception as e:
                Logger.log(f"Fel vid inläsning av config.yaml: {e}", "ERROR")
        Logger.log("config.yaml hittades inte. Använder default-inställningar.", "WARNING")
        return self.DEFAULT_CONFIG

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == "__main__":
    cm = ConfigManager()
    print(cm.config)
