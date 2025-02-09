import os
from ..helpers.logger import Logger
from ..helpers.config_manager import ConfigManager

def initialize_system():
    """
    Initierar systemet genom att ladda konfiguration från miljövariabler och verifiera att nödvändiga resurser finns.
    """
    Logger.log("Initierar systemet...", "INFO")
    
    # Initiera ConfigManager för att ladda konfiguration från .env
    try:
        config_manager = ConfigManager()
        Logger.log("Konfiguration laddad från .env.", "SUCCESS")
        
        # Skapa nödvändiga mappar baserat på konfigurationen
        default_path = config_manager.get("default_path", "./Workspace/")
        if not os.path.exists(default_path):
            os.makedirs(default_path)
            Logger.log(f"Skapade standardmapp: {default_path}", "SUCCESS")
            
        # Skapa docs-mappar om de inte finns
        docs_dirs = ["docs/User-Docs", "docs/Developer-Docs", "docs/AI-Docs"]
        for dir_path in docs_dirs:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                Logger.log(f"Skapade dokumentationsmapp: {dir_path}", "SUCCESS")
                
    except Exception as e:
        Logger.log(f"Fel vid initiering av konfiguration: {str(e)}", "ERROR")
        
    if not os.path.exists(".env"):
        Logger.log(".env fil saknas. Skapa en baserad på .env.example", "WARNING")

    Logger.log("Systeminitiering klar.", "SUCCESS")

if __name__ == "__main__":
    initialize_system()