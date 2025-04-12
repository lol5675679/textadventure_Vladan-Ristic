import time

class Utils:
    """
    Eine Sammlung von Hilfsfunktionen, einschließlich einer intelligenten Eingabeaufforderung
    und einer Funktion zum langsamen Drucken von Text.
    """

    @staticmethod
    def print_slow(text: str, delay: float = 0):
        """
        Gibt Text Zeichen für Zeichen langsam aus.
        :param text: Der Text, der ausgegeben werden soll.
        :param delay: Die Verzögerung zwischen den Zeichen in Sekunden (Standard ist 0,05 Sekunden).
        """
        for letter in text:
            print(letter, end='', flush=True)
            time.sleep(delay)  # Verzögerung zwischen den Zeichen
        print()

    @staticmethod
    def intelligent_input(prompt: str, valid_inputs: list = None) -> str:
        """
        Fragt den Benutzer nach einer Eingabe und validiert sie gegen eine Liste gültiger Eingaben.
        :param prompt: Die Eingabeaufforderung, die dem Benutzer angezeigt wird.
        :param valid_inputs: Eine Liste gültiger Eingaben (optional).
        :return: Die gültige Eingabe des Benutzers.
        """
        while True:
            user_input = input(prompt).strip().lower()  # Eingabe standardisieren
            if valid_inputs is None or user_input in [x.lower() for x in valid_inputs]:  # Validierung
                return user_input
            print("Ungültige Eingabe. Bitte versuche es erneut.")
