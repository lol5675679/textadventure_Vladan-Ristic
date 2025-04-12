import json
from utils import Utils


class Room:
    """
    Repräsentiert einen Raum im Spiel.
    """
    def __init__(self, name: str, description: str, choices: list, outcomes: list):
        self.name = name
        self.description = description
        self.choices = choices
        self.outcomes = outcomes

    def display_room(self):
        """
        Zeigt die Raumbeschreibung und Optionen an.
        """
        Utils.print_slow(self.description + "\n")
        for i, choice in enumerate(self.choices, 1):
            Utils.print_slow(f"[{i}] {choice}\n")

    def resolve_choice(self, choice_index: int, character):
        """
        Verarbeitet die Wahl des Spielers und deren Ergebnis.
        :param choice_index: Index der Spielerwahl.
        :param character: Der Spielercharakter.
        """
        if 0 <= choice_index < len(self.outcomes):
            outcome, detail = self.outcomes[choice_index]
            if outcome == "next":
                Utils.print_slow("Du gehst in den nächsten Raum.\n")
                return detail
            elif outcome == "stay":
                Utils.print_slow(detail + "\n")
            elif outcome == "inventory":
                character.add_to_inventory(detail)
            elif outcome == "death":
                character.health = 0
                Utils.print_slow("Game Over! Du bist gestorben.\n")
            elif outcome == "win":
                Utils.print_slow("Glückwunsch! Du hast das Spiel gewonnen!\n")
        else:
            Utils.print_slow("Ungültige Wahl.\n")

class RoomManager:
    """
    Verwalterklasse für Räume.
    """
    rooms = {}

    @staticmethod
    def load_rooms_from_file(file_path):
        """
        Lädt Räume aus einer JSON-Datei.
        :param file_path: Pfad zur JSON-Datei.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            RoomManager.load_rooms(json_data["rooms"] if "rooms" in json_data else json_data)

    @staticmethod
    def load_rooms(json_data):
        """
        Lädt Räume aus JSON-Daten (Liste von Räumen).
        :param json_data: JSON-Daten der Räume.
        """
        for room_data in json_data:
            room_name = room_data.get("name", "unbekannt")
            RoomManager.rooms[room_name] = Room(
                name=room_name,
                description=room_data.get("description", ""),
                choices=list(room_data.get("option_texts", {}).values()),
                outcomes=[("next", room_data.get("options", {}).get(str(i))) for i in range(1, len(room_data.get("options", {})) + 1)]
            )

    @staticmethod
    def get_room(name):
        """
        Gibt einen Raum anhand seines Namens zurück.
        :param name: Name des Raums.
        :return: Instanz der Klasse Room.
        """
        return RoomManager.rooms.get(name)

# --- Test-Code (deaktivieren für GUI!) ---
# RoomManager.load_rooms_from_file('adventure.json')
# current_room = RoomManager.get_room("verfallener_gang_obergeschoss")
# if current_room:
#     current_room.display_room()
#     choice = Utils.intelligent_input("Wähle eine Option: ", [str(i) for i in range(1, len(current_room.choices) + 1)])
#     next_room_name = current_room.resolve_choice(int(choice) - 1, character=None)
#     if next_room_name:
#         next_room = RoomManager.get_room(next_room_name)
#         if next_room:
#             next_room.display_room()
