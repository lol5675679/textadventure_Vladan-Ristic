import customtkinter as ctk
from speicherlogik import save_game

FARBE_HINTERGRUND = "#2E3437"
FARBE_PRIMÄR = "#B02E48"
FARBE_AKZENT = "#0C4C70"
FARBE_TEXT = "#FFFFFF"

class SpeicherFenster(ctk.CTkFrame):
    def __init__(self, master, charakter_ref, raum_name, zurueck_callback):
        super().__init__(master, fg_color=FARBE_HINTERGRUND)
        self.pack(fill="both", expand=True)

        self.master = master
        self.charakter = charakter_ref
        self.raum_name = raum_name
        self.zurueck_callback = zurueck_callback

        self.build_ui()
        self.bind("<Configure>", self.on_resize)

    def build_ui(self):
        ctk.CTkLabel(self, text="📝 Spiel speichern als:", font=("Orbitron", 20, "bold"), text_color=FARBE_PRIMÄR).pack(pady=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="z.B. spielstand1")
        self.entry.pack(pady=10, fill="x", padx=40)

        ctk.CTkButton(self, text="💾 Speichern", font=("Orbitron", 16), fg_color=FARBE_PRIMÄR,
                      hover_color=FARBE_AKZENT, command=self.speichern).pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="", text_color=FARBE_TEXT, font=("Orbitron", 14))
        self.status_label.pack(pady=10)

    def speichern(self):
        filename = self.entry.get().strip()
        if not filename:
            self.show_message("Bitte einen Spielstandnamen eingeben!", "red")
            return

        data = {
            "name": self.charakter.name,
            "age": self.charakter.age,
            "gender": self.charakter.gender,
            "appearance": self.charakter.appearance,
            "skills": self.charakter.skills,
            "room": self.raum_name
        }

        try:
            save_game(data, filename)
            self.show_message("Spielstand erfolgreich gespeichert!", "green")
            self.master.after(2000, self.zurueck_callback)
        except Exception as e:
            self.show_message(f"Fehler beim Speichern: {e}", "red")

    def show_message(self, text, color):
        self.status_label.configure(text=text, text_color=color)

    def on_resize(self, event):
        if event.width > 800:
            self.status_label.configure(font=("Orbitron", 16))
        else:
            self.status_label.configure(font=("Orbitron", 12))
