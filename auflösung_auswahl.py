import customtkinter as ctk

# Farbpalette
FARBE_HINTERGRUND = "#2E3437"      # Asphalt
FARBE_PRIMÄR = "#B02E48"           # Rot
FARBE_AKZENT = "#0C4C70"           # Tiefblau
FARBE_TEXT = "#FFFFFF"

class AufloesungAuswahl(ctk.CTkFrame):
    def __init__(self, master, apply_callback):
        super().__init__(master, fg_color=FARBE_HINTERGRUND)
        self.apply_callback = apply_callback

        ctk.CTkLabel(
            self,
            text="🖥️ Bildschirmauflösung",
            font=("Orbitron", 24, "bold"),
            text_color=FARBE_PRIMÄR
        ).pack(pady=(20, 10))

        self.aufloesungen = [
            ("1280 x 720 (HD) 💡", (1280, 720)),
            ("1920 x 1080 (Full HD) 🖥️", (1920, 1080)),
            ("2560 x 1440 (QHD) 🚀", (2560, 1440))
        ]

        self.selected = ctk.StringVar(value=self.aufloesungen[0][0])

        # Stylisches Frame für Auswahlbereich
        rahmen = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=12)
        rahmen.pack(padx=20, pady=10, fill="x")

        for text, _ in self.aufloesungen:
            btn = ctk.CTkRadioButton(
                rahmen,
                text=text,
                font=("Orbitron", 16),
                text_color=FARBE_TEXT,
                variable=self.selected,
                value=text,
                border_color=FARBE_PRIMÄR,
                radiobutton_width=30,
                radiobutton_height=30,
                hover_color=FARBE_AKZENT,
                fg_color=FARBE_PRIMÄR
            )
            btn.pack(anchor="w", pady=7, padx=20)

        # Apply-Button
        ctk.CTkButton(
            self,
            text="🎯 Auflösung anwenden",
            font=("Orbitron", 18, "bold"),
            height=45,
            fg_color=FARBE_PRIMÄR,
            hover_color=FARBE_AKZENT,
            corner_radius=12,
            command=self.anwenden
        ).pack(pady=20, padx=30, fill="x")

    def anwenden(self):
        auswahl = self.selected.get()
        einstellung = next((aufl for text, aufl in self.aufloesungen if text == auswahl), (1280, 720))
        self.apply_callback(einstellung)
