import customtkinter as ctk

FARBE_HINTERGRUND = "#2E3437"
FARBE_PRIMÄR = "#B02E48"
FARBE_AKZENT = "#0C4C70"
FARBE_TEXT = "#FFFFFF"

class CharakterPanel(ctk.CTkFrame):
    def __init__(self, master, character, **kwargs):
        super().__init__(master, fg_color=FARBE_HINTERGRUND, **kwargs)
        self.character = character
        self.visible = False

        self.columnconfigure(0, weight=1)
        self.configure(border_width=2, border_color=FARBE_AKZENT, corner_radius=10)

        self.title = ctk.CTkLabel(self, text="🧍 Dein Charakter", font=("Orbitron", 18, "bold"), text_color=FARBE_PRIMÄR)
        self.title.grid(row=0, column=0, pady=(10, 5), padx=10)

        self.info_label = ctk.CTkLabel(self, text="", justify="left", font=("Orbitron", 14), text_color=FARBE_TEXT)
        self.info_label.grid(row=1, column=0, pady=5, padx=10)

        self.hide_button = ctk.CTkButton(self, text="❌ Schließen", font=("Orbitron", 14), fg_color="#444", hover_color="#666", command=self.hide)
        self.hide_button.grid(row=2, column=0, pady=(10, 10))

        self.update_content()

    def update_content(self):
        text = f"🪪 Name: {self.character.name}\n"
        text += f"🎂 Alter: {self.character.age}\n"
        text += f"⚧ Geschlecht: {self.character.gender}\n"

        if self.character.appearance:
            text += f"💇 Haarfarbe: {self.character.appearance.get('Haarfarbe', '-')}\n"
            text += f"👁️ Augenfarbe: {self.character.appearance.get('Augenfarbe', '-')}\n"

        text += "\n📊 Fähigkeiten:\n"
        for skill, value in self.character.skills.items():
            text += f"  - {skill}: {value}\n"

        self.info_label.configure(text=text)

    def toggle(self):
        if self.visible:
            self.hide()
        else:
            self.show()

    def show(self):
        self.pack(side="right", fill="y", padx=10, pady=10)
        self.visible = True
        self.update_content()

    def hide(self):
        self.pack_forget()
        self.visible = False