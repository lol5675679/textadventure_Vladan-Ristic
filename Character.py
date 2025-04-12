from utils import Utils
from intro import Intro  # Importiere die Intro-Klasse hier

class Character:
    """
    Klasse zur Erstellung und Verwaltung des Spielercharakters.
    """

    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.appearance = {}
        self.skills = {
            "Mut": 0,
            "Intelligenz": 0,
            "Geschicklichkeit": 0,
            "Charisma": 0
        }
        self.inventory = []  


    def create_character(self):
        """
        Erlaubt dem Spieler, seinen Charakter zu gestalten.
        """
        Utils.print_slow("Es ist Zeit, deinen Charakter zu gestalten.\n")

        # Name eingeben
        self.name = input("Wie heißt du? ").strip()
        Utils.print_slow(f"Willkommen, {self.name}!\n")

        # Alter eingeben
        while True:
            try:
                self.age = int(input("Wie alt bist du? ").strip())
                if self.age > 0:
                    break
                else:
                    print("Bitte gib ein gültiges Alter ein.")
            except ValueError:
                print("Das Alter muss eine Zahl sein.")

        # Geschlecht auswählen
        self.gender = Utils.intelligent_input(
            "Bist du männlich, weiblich oder divers? (m/w/d): ", ["m", "w", "d"]
        )
        self.gender = {"m": "männlich", "w": "weiblich", "d": "divers"}[self.gender]

        # Erscheinungsbild gestalten
        Utils.print_slow("Beschreibe dein Erscheinungsbild.\n")
        hair_color = input("Welche Haarfarbe hast du? ").strip()
        eye_color = input("Welche Augenfarbe hast du? ").strip()
        self.appearance = {"Haarfarbe": hair_color, "Augenfarbe": eye_color}

        # Fähigkeiten zuweisen
        Utils.print_slow("Jetzt verteile 10 Punkte auf deine Fähigkeiten: Mut, Intelligenz, Geschicklichkeit und Charisma.\n")
        remaining_points = 10

        for skill in self.skills:
            while True:
                try:
                    Utils.print_slow(f"Verfügbare Punkte: {remaining_points}\n")
                    points = int(input(f"Wie viele Punkte möchtest du für {skill} vergeben? ").strip())
                    if 0 <= points <= remaining_points:
                        self.skills[skill] = points
                        remaining_points -= points
                        break
                    else:
                        print(f"Bitte gib eine Zahl zwischen 0 und {remaining_points} ein.")
                except ValueError:
                    print("Das muss eine Zahl sein.")

        Utils.print_slow("Hier ist dein Charakter:\n")
        Utils.print_slow(f"Name: {self.name}\nAlter: {self.age}\nGeschlecht: {self.gender}\n")
        Utils.print_slow(f"Haarfarbe: {self.appearance['Haarfarbe']}\nAugenfarbe: {self.appearance['Augenfarbe']}\n")
        Utils.print_slow("Fähigkeiten:\n")
        for skill, value in self.skills.items():
            Utils.print_slow(f"  {skill}: {value}\n")

        Utils.print_slow("Dein Charakter ist bereit. Weiter zur Einführung...\n")
        
        # Intro wird jetzt hier aufgerufen
        Intro.display_intro(self.get_character_summary())  # Intro wird direkt nach der Erstellung des Charakters aufgerufen

    def get_character_summary(self):
        """
        Gibt eine Zusammenfassung des Charakters zurück.
        """
        return {
            "Name": self.name,  # Nur der Name wird übergeben
        }
