import customtkinter as ctk

FARBE_HINTERGRUND = "#2E3437"
FARBE_PRIMÄR = "#B02E48"
FARBE_AKZENT = "#0C4C70"
FARBE_TEXT = "#FFFFFF"

class Logbuch(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=250, fg_color=FARBE_HINTERGRUND)
        self.pack(side="right", fill="y", padx=5, pady=10)

        self.visible = True
        self.einträge = []

        ctk.CTkLabel(self, text="📘 Logbuch", font=("Orbitron", 18, "bold"), text_color=FARBE_PRIMÄR).pack(pady=(10, 0))
        self.textbox = ctk.CTkTextbox(self, wrap="word", fg_color="#1c1f21", text_color=FARBE_TEXT)
        self.textbox.pack(expand=True, fill="both", padx=5, pady=10)

        self.toggle_button = ctk.CTkButton(
            self, text="🫣 Verbergen", font=("Orbitron", 14),
            fg_color="#444", hover_color="#666",
            command=self.umschalten
        )
        self.toggle_button.pack(pady=5)

    def umschalten(self):
        if self.visible:
            self.textbox.pack_forget()
            self.toggle_button.configure(text="📘 Anzeigen")
        else:
            self.textbox.pack(expand=True, fill="both", padx=5, pady=10)
            self.toggle_button.configure(text="🫣 Verbergen")
        self.visible = not self.visible

    def eintrag_hinzufügen(self, text: str):
        self.einträge.append(text)
        self.update_textbox()

    def update_textbox(self):
        if self.textbox and self.textbox.winfo_exists():
            self.textbox.delete("1.0", "end")
            for eintrag in self.einträge:
                self.textbox.insert("end", f"• {eintrag}\n\n")