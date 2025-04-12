import customtkinter as ctk

FARBE_HINTERGRUND = "#2E3437"
FARBE_PRIMÄR = "#B02E48"
FARBE_AKZENT = "#0C4C70"
FARBE_TEXT = "#FFFFFF"

class MiniMap(ctk.CTkFrame):
    def __init__(self, parent, raum_liste: list[str]):
        super().__init__(parent, width=250, fg_color=FARBE_HINTERGRUND)
        self.pack(side="right", fill="y", padx=5, pady=10)

        self.raum_liste = raum_liste
        self.current = None
        self.labels = {}

        ctk.CTkLabel(self, text="🗺️ Minimap", font=("Orbitron", 18, "bold"), text_color=FARBE_PRIMÄR).pack(pady=(10, 0))

        for raum in self.raum_liste:
            label = ctk.CTkLabel(self, text=f"• {raum}", anchor="w", font=("Orbitron", 14), text_color=FARBE_TEXT)
            label.pack(fill="x", padx=10, pady=2)
            self.labels[raum] = label

    def raum_anzeigen(self, raum_name: str):
        self.current = raum_name
        for name, label in self.labels.items():
            if name == raum_name:
                label.configure(text_color=FARBE_PRIMÄR)
            else:
                label.configure(text_color=FARBE_TEXT)
