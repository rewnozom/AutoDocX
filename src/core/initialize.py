import os
from ..helpers.logger import Logger
import yaml

def initialize_system():
    """
    Initierar systemet genom att ladda konfiguration, miljövariabler och verifiera att nödvändiga resurser finns.
    """
    Logger.log("Initierar systemet...", "INFO")
    config_path = "config.yaml"
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        Logger.log("Konfiguration inläst från config.yaml.", "SUCCESS")
    else:
        Logger.log("config.yaml hittades inte. Använder standardinställningar.", "WARNING")
    
    if os.path.exists(".env"):
        Logger.log("Laddar miljövariabler från .env...", "INFO")
        try:
            from dotenv import load_dotenv
            load_dotenv()
            Logger.log(".env inläst.", "SUCCESS")
        except ImportError:
            Logger.log("python-dotenv inte installerat. Hoppar över .env inläsning.", "WARNING")
    else:
        Logger.log(".env fil hittades inte.", "WARNING")
    
    Logger.log("Systeminitiering klar.", "SUCCESS")
