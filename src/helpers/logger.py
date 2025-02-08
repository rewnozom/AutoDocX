import sys
import time

class Logger:
    """
    Logger för AutoDocX som skriver ut processloggar med tidsstämpel.
    Ger visuell feedback med färgkodade utskrifter i terminalen.
    """
    COLORS = {
        "INFO": "\033[94m",    # Blå
        "SUCCESS": "\033[92m", # Grön
        "WARNING": "\033[93m", # Gul
        "ERROR": "\033[91m",   # Röd
        "ENDC": "\033[0m"      # Återställ färg
    }

    @staticmethod
    def log(message, level="INFO"):
        color = Logger.COLORS.get(level, "")
        endc = Logger.COLORS["ENDC"]
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 🛠️ FIXAD RAD: Stänger f-string korrekt
        sys.stdout.write(f"{color}[{timestamp}] [{level}] {message}{endc}\n")
        sys.stdout.flush()

if __name__ == "__main__":
    Logger.log("Detta är en informationslogg.", "INFO")
    Logger.log("Detta är en varningslogg.", "WARNING")
    Logger.log("Detta är en fel-logg.", "ERROR")
    Logger.log("Detta är en succélogg.", "SUCCESS")
