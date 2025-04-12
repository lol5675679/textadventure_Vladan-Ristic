import customtkinter as ctk

class TimerLeiste(ctk.CTkFrame):
    def __init__(self, master, callback_bei_ablauf, dauer=15):
        super().__init__(master, corner_radius=10, fg_color="transparent")
        self.callback_bei_ablauf = callback_bei_ablauf
        self.timer_seconds = dauer
        self.time_left = 100
        self.timer_id = None
        self.pulse_state = True

        self.pack(fill="x", padx=20, pady=(5, 10))

        self.label = ctk.CTkLabel(self, text="🩸 Zeit läuft...", font=("Arial", 14, "bold"), text_color="#8B0000")
        self.label.pack(pady=(5, 0))

        self.balken = ctk.CTkProgressBar(self, height=16, corner_radius=8, border_width=1, progress_color="#8B0000")
        self.balken.pack(fill="x", padx=20, pady=(3, 2))
        self.balken.set(1.0)

        self.prozent_label = ctk.CTkLabel(self, text="100%", font=("Arial", 12, "bold"), text_color="#8B0000")
        self.prozent_label.pack()

    def starten(self):
        self.time_left = 100
        self._aktualisieren()

    def _aktualisieren(self):
        prozent = int(self.time_left)
        self.prozent_label.configure(text=f"{prozent}%")
        self.balken.set(prozent / 100)

        if self.time_left < 50:
            self._pulse()

        if self.time_left <= 0:
            self.prozent_label.configure(text="0%")
            self.callback_bei_ablauf()
        else:
            self.time_left -= 2
            self.timer_id = self.after(int(self.timer_seconds * 10), self._aktualisieren)

    def _pulse(self):
        farbe1 = "#8B0000"
        farbe2 = "#B22222"
        neue_farbe = farbe2 if self.pulse_state else farbe1
        self.balken.configure(progress_color=neue_farbe)
        self.prozent_label.configure(text_color=neue_farbe)
        self.label.configure(text_color=neue_farbe)
        self.pulse_state = not self.pulse_state

    def abbrechen(self):
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        try:
            self.prozent_label.configure(text="⏹️ Abgebrochen", text_color="gray")
            self.balken.set(0)
            self.label.configure(text="Timer gestoppt", text_color="gray")
        except:
            pass
