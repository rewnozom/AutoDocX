import sys
import time

class Logger:
    """
    Logger för AutoDocX som skriver ut processloggar med tidsstämpel.
    Ger visuell feedback med färgkodade utskrifter i terminalen.
    """
    COLORS = {
        "INFO": "[94m",    # Blå
        "SUCCESS": "[92m", # Grön
        "WARNING": "[93m", # Gul
        "ERROR": "[91m",   # Röd
        "ENDC": "[0m"      # Återställ färg
    }
    
    @staticmethod
    def log(message, level="INFO"):
        color = Logger.COLORS.get(level, "")
        endc = Logger.COLORS["ENDC"]
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sys.stdout.write(f"{color}[{timestamp}] [{level}] {message}{endc}
")
        sys.stdout.flush()

if __name__ == "__main__":
    Logger.log("Detta är en informationslogg.", "INFO")
    Logger.log("Detta är en varningslogg.", "WARNING")
    Logger.log("Detta är en fel-logg.", "ERROR")
    Logger.log("Detta är en succélogg.", "SUCCESS")
