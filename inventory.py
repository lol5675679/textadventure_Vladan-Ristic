class Inventory:
    """
    Klasse zur Verwaltung des Spielerinventars.
    """

    def __init__(self):
        self.items = []

    def add_item(self, item: str):
        """
        Fügt einen Gegenstand zum Inventar hinzu.
        :param item: Der Name des Gegenstands.
        """
        self.items.append(item)
        print(f"'{item}' wurde dem Inventar hinzugefügt.")

    def remove_item(self, item: str):
        """
        Entfernt einen Gegenstand aus dem Inventar.
        :param item: Der Name des Gegenstands.
        """
        if item in self.items:
            self.items.remove(item)
            print(f"'{item}' wurde aus dem Inventar entfernt.")
        else:
            print(f"'{item}' ist nicht im Inventar.")

    def show_inventory(self):
        """
        Zeigt den aktuellen Inhalt des Inventars.
        """
        if self.items:
            print("Dein Inventar enthält folgende Gegenstände:")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item}")
        else:
            print("Dein Inventar ist leer.")

    def has_item(self, item: str) -> bool:
        """
        Überprüft, ob ein bestimmter Gegenstand im Inventar ist.
        :param item: Der Name des Gegenstands.
        :return: True, wenn der Gegenstand im Inventar ist, sonst False.
        """
        return item in self.items
