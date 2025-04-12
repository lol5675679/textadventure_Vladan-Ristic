import customtkinter as ctk
from speicherlogik import get_all_savefiles, load_game

FARBE_HINTERGRUND = "#2E3437"
FARBE_PRIMÄR = "#B02E48"
FARBE_AKZENT = "#0C4C70"
FARBE_TEXT = "#FFFFFF"

class LadeFenster(ctk.CTkFrame):
    def __init__(self, master, charakter_ref, start_game_callback, fehler_callback):
        super().__init__(master, fg_color=FARBE_HINTERGRUND)
        self.pack(fill="both", expand=True)

        self.charakter = charakter_ref
        self.start_game_callback = start_game_callback
        self.fehler_callback = fehler_callback

        self.build_ui()

    def build_ui(self):
        ctk.CTkLabel(self, text="💾 Spielstand wählen:", font=("Orbitron", 20, "bold"), text_color=FARBE_PRIMÄR).pack(pady=10)

        savefiles = get_all_savefiles()
        if not savefiles:
            ctk.CTkLabel(self, text="Keine Spielstände gefunden.", text_color="red", font=("Orbitron", 14)).pack(pady=10)
            ctk.CTkButton(self, text="Zurück", font=("Orbitron", 14), fg_color="#444", hover_color="#666", command=self.fehler_callback).pack(pady=20)
            return

        for file in savefiles:
            ctk.CTkButton(
                self,
                text=file,
                font=("Orbitron", 14),
                fg_color=FARBE_AKZENT,
                hover_color=FARBE_PRIMÄR,
                command=lambda f=file: self.lade_und_starte(f)
            ).pack(pady=5, fill="x", padx=40)

        ctk.CTkButton(self, text="Zurück", font=("Orbitron", 14), fg_color="#444", hover_color="#666", command=self.fehler_callback).pack(pady=20)

    def lade_und_starte(self, filename):
        try:
            data = load_game(filename)
            self.charakter.name = data.get("name", "")
            self.charakter.age = data.get("age", 0)
            self.charakter.gender = data.get("gender", "")
            self.charakter.appearance = data.get("appearance", {})
            self.charakter.skills = data.get("skills", {})
            raum = data.get("room", "verfallener_gang_obergeschoss")
            self.start_game_callback(raum)
        except Exception as e:
            self.destroy()
            error_label = ctk.CTkLabel(self.master, text=f"Fehler beim Laden: {e}", text_color="red")
            error_label.pack(pady=10)
            ctk.CTkButton(self.master, text="Zurück", font=("Orbitron", 14), fg_color="#444", hover_color="#666", command=self.fehler_callback).pack(pady=10)
