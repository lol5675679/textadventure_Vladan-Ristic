import json
import os

SAVE_DIR = "saves"

# Stelle sicher, dass der Ordner beim Start existiert
os.makedirs(SAVE_DIR, exist_ok=True)

def save_game(data: dict, filename: str):
    """Speichert das Spiel als JSON im saves-Ordner."""
    if not filename.endswith(".json"):
        filename += ".json"
    path = os.path.join(SAVE_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_game(filename: str) -> dict:
    """Lädt einen Spielstand aus dem saves-Ordner."""
    path = os.path.join(SAVE_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[Fehler beim Laden von {filename}]: {e}")
        return {}

def get_all_savefiles() -> list:
    """Gibt alle Spielstände im saves-Ordner zurück (Dateinamen)."""
    return [f for f in os.listdir(SAVE_DIR) if f.endswith(".json")]
