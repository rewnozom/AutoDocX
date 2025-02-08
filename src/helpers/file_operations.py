import os

def read_file(file_path):
    """
    Läser innehållet i en fil och returnerar det som en sträng.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"[ERROR] Kunde inte läsa filen {file_path}: {e}")
        return None

def write_file(file_path, content):
    """
    Skriver innehållet till en fil. Skapar mappstruktur om det behövs.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[WRITE] Filen {file_path} skrevs.")
    except Exception as e:
        print(f"[ERROR] Kunde inte skriva filen {file_path}: {e}")

def append_to_file(file_path, content):
    """
    Appenderar innehåll till en existerande fil.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(content)
        print(f"[APPEND] Innehåll har lagts till i {file_path}.")
    except Exception as e:
        print(f"[ERROR] Kunde inte appenda till filen {file_path}: {e}")

if __name__ == "__main__":
    # Testa funktionerna
    test_path = "temp/test_file.txt"
    write_file(test_path, "Detta är en testtext.")
    print("Läser fil:", read_file(test_path))
    
    # 🛠 FIXAD RAD: Stängd sträng korrekt
    append_to_file(test_path, "\nLägger till mer text.")
    
    print("Läser fil igen:", read_file(test_path))
