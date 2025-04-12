from utils import Utils
from texts import GameTexts
from vorgeschichte import Vorgeschichte
import time

class Intro:
    @staticmethod
    def display_intro(character):
        """
        Zeigt die Einleitung an und verarbeitet die Spielerinteraktion.
        :param character: Ein Dictionary mit Charakterinformationen.
        """
        # Standardwerte für den Charakter setzen
        character_defaults = {"Name": "Unbekannt"}
        character = {**character_defaults, **character}  # Fehlende Werte ergänzen

        # Prüfen, ob GameTexts.INTRO korrekt definiert ist
        if not hasattr(GameTexts, "INTRO") or not isinstance(GameTexts.INTRO, list):
            raise AttributeError("`GameTexts.INTRO` ist nicht definiert oder kein gültiger Text.")

        # Debugging (kann entfernt werden, sobald alles funktioniert)
        print("DEBUG: GameTexts.INTRO =", GameTexts.INTRO)

        # Intro-Texte anzeigen
        for line in GameTexts.INTRO:
            formatted_line = line.replace("{Name}", character["Name"])
            Utils.print_slow(formatted_line + "\n")
            time.sleep(2)

        # Entscheidungsphase
        Utils.print_slow("Doch bevor du weitergehst, beantworte eine entscheidende Frage...\n")
        time.sleep(2)
        Utils.print_slow("Glaubst du wirklich, dass du die Kraft besitzt, das Unaussprechliche zu überleben?\n")
        time.sleep(2)
        Utils.print_slow("Falls ja, wähle mit Bedacht...\n")
        time.sleep(2)

        # Optionen anzeigen
        Utils.print_slow("----\n")
        Utils.print_slow("\t[1]. Weiter in die Dunkelheit schreiten.\n")
        Utils.print_slow("----\n")
        Utils.print_slow("\t[2]. Umkehren und dem Wahnsinn entfliehen.\n")
        Utils.print_slow("----\n")

        # Eingabe des Spielers
        antwort = Utils.intelligent_input("Deine Wahl: ", ["1", "2"])

        # Entscheidungen verarbeiten
        if antwort == "1":
            Utils.print_slow("Mutig! Das Abenteuer beginnt. Die Schatten erwarten dich...\n")
            Vorgeschichte.display_vorgeschichte()
        elif antwort == "2":
            Utils.print_slow("Dein Herz war zu schwach. Die Dunkelheit verschlingt dich...\n")

if __name__ == "__main__":
    # Testfall: Beispiel-Charakter
    test_character = {"Name": "Test"}
    Intro.display_intro(test_character)
