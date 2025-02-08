# src/helpers/config_manager.py
import os
from dotenv import load_dotenv
from ..helpers.logger import Logger

class ConfigManager:
    """
    Hanterar inläsning av konfiguration från miljövariabler (.env).
    Standardvärden används om miljövariabler saknas.
    """

    def __init__(self):
        # Ladda miljövariabler från .env
        load_dotenv()

        self.config = {
            "default_llm": os.getenv("DEFAULT_MODEL", "lmstudio"),
            "default_path": os.getenv("DEFAULT_PATH", "./Workspace/"),
            "ignore_paths": os.getenv("IGNORE_PATHS", "node_modules,.git,venv").split(","),
            "prompt_templates": {
                "developer": {
                    "full": os.getenv("PROMPT_DEV_FULL", "Developer-Full-Prompt-Template"),
                    "sum": os.getenv("PROMPT_DEV_SUM", "Developer-Summary-Prompt-Template"),
                    "short": os.getenv("PROMPT_DEV_SHORT", "Developer-Short-Prompt-Template")
                },
                "user": {
                    "full": os.getenv("PROMPT_USER_FULL", "User-Full-Prompt-Template"),
                    "sum": os.getenv("PROMPT_USER_SUM", "User-Summary-Prompt-Template"),
                    "short": os.getenv("PROMPT_USER_SHORT", "User-Short-Prompt-Template")
                },
                "ai": {
                    "full": os.getenv("PROMPT_AI_FULL", "AI-Full-Prompt-Template"),
                    "sum": os.getenv("PROMPT_AI_SUM", "AI-Summary-Prompt-Template"),
                    "short": os.getenv("PROMPT_AI_SHORT", "AI-Short-Prompt-Template")
                }
            },
            "llm": {
                "lmstudio": {
                    "context_tokens": int(os.getenv("MAX_TOKENS", "60000")),
                    "temperature": float(os.getenv("TEMPERATURE", "0.7")),
                    "top_p": float(os.getenv("TOP_P", "0.9")),
                    "base_url": os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234/v1"),
                    "model": os.getenv("LM_STUDIO_MODEL", "model-identifier")
                },
                "anthropic": {
                    "context_tokens": int(os.getenv("MAX_TOKENS", "60000")),
                    "temperature": float(os.getenv("TEMPERATURE", "0.7")),
                    "top_p": float(os.getenv("TOP_P", "0.9")),
                    "api_key": os.getenv("ANTHROPIC_API_KEY"),
                    "model_opus": os.getenv("CLAUDE_OPUS_MODEL", "claude-3-opus-20240229"),
                    "model_sonnet": os.getenv("CLAUDE_SONNET_MODEL", "claude-3-sonnet-20240229"),
                    "model_haiku": os.getenv("CLAUDE_HAIKU_MODEL", "claude-3-haiku-20240307")
                },
                "openai": {
                    "context_tokens": int(os.getenv("MAX_TOKENS", "60000")),
                    "temperature": float(os.getenv("TEMPERATURE", "0.7")),
                    "top_p": float(os.getenv("TOP_P", "0.9")),
                    "api_key": os.getenv("OPENAI_API_KEY"),
                    "gpt4_model": os.getenv("GPT4_MODEL", "gpt-4"),
                    "gpt35_model": os.getenv("GPT35_MODEL", "gpt-3.5-turbo")
                },
                "azure": {
                    "context_tokens": int(os.getenv("MAX_TOKENS", "60000")),
                    "temperature": float(os.getenv("TEMPERATURE", "0.7")),
                    "top_p": float(os.getenv("TOP_P", "0.9")),
                    "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
                    "base_url": os.getenv("AZURE_BASE_URL", "https://your-resource.openai.azure.com"),
                    "api_version": os.getenv("AZURE_API_VERSION", "2024-02-15-preview"),
                    "gpt4_model": os.getenv("AZURE_GPT4_MODEL", "gpt-4"),
                    "gpt35_model": os.getenv("AZURE_GPT35_MODEL", "gpt-3.5-turbo")
                },
                "groq": {
                    "context_tokens": int(os.getenv("MAX_TOKENS", "60000")),
                    "temperature": float(os.getenv("TEMPERATURE", "0.7")),
                    "top_p": float(os.getenv("TOP_P", "0.9")),
                    "api_key": os.getenv("GROQ_API_KEY"),
                    "model_mixtral": os.getenv("GROQ_MODEL", "mixtral-8x7b-32768")
                }
            }
        }

        Logger.log("Konfiguration laddad från miljövariabler.", "SUCCESS")

    def get(self, key, default=None):
        """
        Hämtar en konfigurationsparameter.
        """
        return self.config.get(key, default)

if __name__ == "__main__":
    cm = ConfigManager()
    print(cm.config)
