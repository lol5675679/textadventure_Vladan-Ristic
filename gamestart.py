import json
import time
from utils import Utils
from texts import GameTexts

class GameStart:
    """
    Klasse zur Verwaltung des Spielstarts nach der Vorgeschichte.
    """

    @staticmethod
    def start_game():
        """
        Gibt den Text für den Spielstart aus und lädt die Adventure-Daten.
        """
        # Spielstart-Texte anzeigen
        for line in GameTexts.GAMESTART:
            Utils.print_slow(line + "\n")
            time.sleep(2)

        Utils.print_slow("Lade die Abenteuerwelt...\n")
        time.sleep(2)

        # Adventure-Daten aus der JSON-Datei laden
        try:
            with open("adventure.json", "r", encoding="utf-8") as json_file:
                adventure_data = json.load(json_file)
        except FileNotFoundError:
            Utils.print_slow("Fehler: Die Datei 'adventure.json' wurde nicht gefunden.\n")
            return
        except json.JSONDecodeError:
            Utils.print_slow("Fehler: Die Datei 'adventure.json' enthält ungültige Daten.\n")
            return

        Utils.print_slow("Abenteuerwelt erfolgreich geladen. Das Spiel beginnt jetzt!\n")
        time.sleep(2)

        # Übergang ins Hauptspiel basierend auf den JSON-Daten
        GameStart.start_adventure(adventure_data)

    @staticmethod
    def start_adventure(adventure_data):
        """
        Startet das Abenteuer basierend auf den geladenen JSON-Daten.
        :param adventure_data: Ein Dictionary mit den Adventure-Daten.
        """
        current_room = adventure_data["rooms"][0]  # Startraum
        GameStart.explore_room(current_room, adventure_data)

    @staticmethod
    def explore_room(room, adventure_data):
        """
        Lässt den Spieler einen Raum erkunden und Entscheidungen treffen.
        :param room: Der aktuelle Raum, der erkundet wird.
        :param adventure_data: Die gesamte Adventure-Datenstruktur.
        """
        Utils.print_slow(f"Du befindest dich in {room['name']}.\n")
        Utils.print_slow(f"Beschreibung: {room['description']}\n")
        time.sleep(2)

        # Entscheidungen des Spielers
        options = room["options"]
        option_texts = room["option_texts"]

        decision = GameStart.ask_decision(options, option_texts)
        next_room_name = options[str(decision)]  # Hole den nächsten Raum basierend auf der Entscheidung

        # Finde den nächsten Raum in den Adventure-Daten
        next_room = next((r for r in adventure_data["rooms"] if r["name"] == next_room_name), None)
        if next_room:
            GameStart.explore_room(next_room, adventure_data)

    @staticmethod
    def ask_decision(options, option_texts):
        """
        Fragt den Spieler nach einer Entscheidung basierend auf den gegebenen Optionen.
        :param options: Ein Dictionary von Optionen (Schlüsseln: Ziffern als Strings, Werten: Raumnamen).
        :param option_texts: Ein Dictionary von Texten für die Optionen.
        :return: Die vom Spieler getroffene Wahl.
        """
        Utils.print_slow("Was möchtest du tun?\n")
        for idx, text in option_texts.items():
            Utils.print_slow(f"{idx}. {text}\n")

        while True:
            try:
                player_choice = input("Gib die Nummer deiner Wahl ein: ").strip()
                if player_choice in options:
                    return int(player_choice)  # Gibt die Auswahl als Integer zurück
                else:
                    Utils.print_slow("Ungültige Wahl. Bitte versuche es erneut.\n")
            except ValueError:
                Utils.print_slow("Ungültige Eingabe. Bitte gib eine Zahl ein.\n")

if __name__ == "__main__":
    # Testlauf für den Spielstart
    GameStart.start_game()
