from utils import Utils
from texts import GameTexts
import time

class Vorgeschichte:
    """
    Klasse zur Verwaltung der Vorgeschichte des Spiels.
    """

    @staticmethod
    def display_vorgeschichte():
        """
        Zeigt die Vorgeschichte der Anstalt und fordert den Spieler zu einer Entscheidung auf.
        """
        for line in GameTexts.VORGESCHICHTE:
            Utils.print_slow(line + "\n")
            time.sleep(2)

        Utils.print_slow("Noch hast du die Möglichkeit, umzukehren. Aber wenn du weitermachen willst, dann entscheide dich jetzt:\n")
        time.sleep(2)
        Utils.print_slow("----\n")
        Utils.print_slow("[1] = Du startest das Spiel und stellst dich der Dunkelheit.\n")
        Utils.print_slow("----\n")
        Utils.print_slow("[2] = Du gibst auf und suchst Sicherheit im Licht.\n")
        Utils.print_slow("----\n")

        antwort = Utils.intelligent_input("Deine Entscheidung: ", ["1", "2"])

        if antwort == "1":
            Utils.print_slow("Mutig! Das Abenteuer beginnt. Die Dunkelheit erwartet dich...\n")
            from gamestart import GameStart
            GameStart.start_game()
        elif antwort == "2":
            Utils.print_slow("Klug, aber feige. Die Anstalt wird auf dich warten...\n")
            # Hier könnte eine Game-Over-Logik eingefügt werden
