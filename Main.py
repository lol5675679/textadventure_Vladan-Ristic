from utils import Utils  # Importiert Utils aus utils.py
from Character import Character  # Importiert Character aus Character.py
from spielgui import SpielGUI
def main():
    """Hauptfunktion, die das Spiel startet."""
    try:
        Utils.print_slow("Willkommen zu meinem Textadventure!\n")
        Utils.print_slow("In diesem Spiel wirst du deinen eigenen Charakter erstellen und dich auf ein düsteres Abenteuer begeben.\n")
        Utils.print_slow("Als erstes erstellen wir deinen Charakter.\n")
        
        # Charakter erstellen
        player = Character()
        player.create_character()
        
    except Exception as e:
        print(f"Es ist ein Fehler aufgetreten: {e}")
        Utils.print_slow("Das Spiel wurde beendet. Bitte versuche es erneut.\n")

if __name__ == "__main__":
    app = SpielGUI()
    app.mainloop()
