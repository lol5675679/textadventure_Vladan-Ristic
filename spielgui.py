import customtkinter as ctk
import json
import os
import sys
from texts import GameTexts
from Character import Character
from charakter_gui import CharakterErstellung
from ladefenster import LadeFenster
from speicherfenster import SpeicherFenster
from logbuch import Logbuch
from charakter_panel import CharakterPanel
from timerleiste import TimerLeiste
from auflösung_auswahl import AufloesungAuswahl
from minimap import MiniMap

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

FARBE_HINTERGRUND = "#2E3437"
FARBE_PRIMÄR = "#B02E48"
FARBE_AKZENT = "#0C4C70"
FARBE_TEXT = "#FFFFFF"

class SpielGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🩸 Textadventure: Die Verlassene Klinik")
        self.geometry("1280x720")
        self.resizable(True, True)
        self.configure(fg_color=FARBE_HINTERGRUND)

        self.character = Character()
        self.current_room = None
        self.adventure_data = {}

        self.logbuch = None
        self.spiel_beendet = False
        self.charakter_panel = None
        self.blut_timer = None
        self.minimap = None

        self.bind("<Configure>", self.on_resize)
        self.font_size = 14

        self.show_start_menu()

    def on_resize(self, event):
        width = event.width
        if width < 1000:
            self.font_size = 12
        elif width < 1400:
            self.font_size = 14
        else:
            self.font_size = 16

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_start_menu(self):
        self.spiel_beendet = False
        self.clear_window()

        frame = ctk.CTkFrame(self, corner_radius=15, fg_color=FARBE_HINTERGRUND)
        frame.pack(padx=40, pady=60, fill="both", expand=True)

        title = ctk.CTkLabel(frame, text="🧟 Willkommen im Horror-Textadventure 🧟", font=("Orbitron", 36, "bold"), text_color=FARBE_PRIMÄR)
        title.pack(pady=30)

        ctk.CTkButton(frame, text="🎮 Neues Spiel starten", font=("Orbitron", 18), height=45,
                      fg_color=FARBE_PRIMÄR, hover_color=FARBE_AKZENT,
                      command=self.neues_spiel_starten).pack(pady=12, fill="x", padx=200)
        ctk.CTkButton(frame, text="💾 Spielstand laden", font=("Orbitron", 18), height=45,
                      fg_color=FARBE_PRIMÄR, hover_color=FARBE_AKZENT,
                      command=self.zeige_ladefenster).pack(pady=12, fill="x", padx=200)
        ctk.CTkButton(frame, text="🚪 Beenden", font=("Orbitron", 18), height=45,
                      fg_color="#444", hover_color="#666", command=self.quit).pack(pady=12, fill="x", padx=200)

        aufl_frame = AufloesungAuswahl(frame, self.set_window_size)
        aufl_frame.pack(pady=10)

    def neues_spiel_starten(self):
        self.clear_window()
        CharakterErstellung(self, self.character, self.show_intro)

    def set_window_size(self, einstellung):
        self.attributes("-fullscreen", False)
        self.geometry(f"{einstellung[0]}x{einstellung[1]}")

    def zeige_ladefenster(self):
        self.clear_window()
        LadeFenster(self, self.character, self.start_game, self.show_start_menu)

    def load_game(self):
        try:
            with open("savegame.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.character.name = data.get("name", "")
                self.character.age = data.get("age", 0)
                self.character.gender = data.get("gender", "")
                self.character.appearance = data.get("appearance", {})
                self.character.skills = data.get("skills", {})
                start_room = data.get("room", "verfallener_gang_obergeschoss")
                self.start_game(start_room)
        except Exception as e:
            self.clear_window()
            ctk.CTkLabel(self, text=f"Fehler beim Laden: {e}", text_color="red").pack(pady=20)
            ctk.CTkButton(self, text="🔙 Zurück", command=self.show_start_menu).pack()

    def show_intro(self):
        self.clear_window()
        self.textbox = ctk.CTkTextbox(self, wrap="word", fg_color="#1c1f21", text_color=FARBE_TEXT)
        self.textbox.pack(fill="both", expand=True, padx=20, pady=20)

        for line in GameTexts.INTRO:
            self.textbox.insert("end", line.replace("{Name}", self.character.name) + "\n\n")

        btn_frame = ctk.CTkFrame(self, fg_color=FARBE_HINTERGRUND)
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="➡️ In die Dunkelheit", font=("Orbitron", 14), fg_color=FARBE_PRIMÄR, hover_color=FARBE_AKZENT, command=self.show_vorgeschichte).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="⬅️ Umkehren", font=("Orbitron", 14), fg_color="#444", hover_color="#666", command=self.quit).pack(side="left", padx=10)

    def show_vorgeschichte(self):
        self.clear_window()
        self.textbox = ctk.CTkTextbox(self, wrap="word", fg_color="#1c1f21", text_color=FARBE_TEXT)
        self.textbox.pack(fill="both", expand=True, padx=20, pady=20)

        for line in GameTexts.VORGESCHICHTE:
            self.textbox.insert("end", line + "\n\n")

        ctk.CTkButton(self, text="☠️ Spiel starten", font=("Orbitron", 16), fg_color=FARBE_PRIMÄR, hover_color=FARBE_AKZENT, command=self.start_game).pack(pady=10)

    def start_game(self, start_room="verfallener_gang_obergeschoss"):
        self.clear_window()

        main_frame = ctk.CTkFrame(self, fg_color=FARBE_HINTERGRUND)
        main_frame.pack(fill="both", expand=True)

        spielbereich = ctk.CTkFrame(main_frame, fg_color=FARBE_HINTERGRUND)
        spielbereich.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.text_frame = ctk.CTkFrame(spielbereich, fg_color="#1c1f21")
        self.text_frame.pack(fill="both", expand=True)

        self.button_frame = ctk.CTkFrame(spielbereich, fg_color=FARBE_HINTERGRUND)
        self.button_frame.pack(fill="x", pady=(0, 10))

        self.textbox = ctk.CTkTextbox(self.text_frame, wrap="word", fg_color="#1c1f21", text_color=FARBE_TEXT, font=("Orbitron", self.font_size))
        self.textbox.pack(fill="both", expand=True)

        self.blut_timer = TimerLeiste(self.button_frame, self.zeit_abgelaufen)
        self.logbuch = Logbuch(main_frame)
        self.charakter_panel = CharakterPanel(main_frame, self.character)

        self.adventure_data = self.load_adventure()
        self.current_room = None
        self.minimap = MiniMap(main_frame, [r["name"] for r in self.adventure_data["rooms"]])
        self.show_room(start_room)

    def load_adventure(self):
        try:
            if getattr(sys, 'frozen', False):
                base_path = sys._MEIPASS
            else:
                base_path = os.path.dirname(os.path.abspath(__file__))

            json_path = os.path.join(base_path, "adventure.json")

            with open(json_path, "r", encoding="utf-8") as file:
                return json.load(file)

        except Exception as e:
            self.textbox.insert("end", f"Fehler beim Laden: {e}\n")
            return {}

    def show_room(self, room_name):
        if self.blut_timer:
            self.blut_timer.abbrechen()

        if self.button_frame and self.button_frame.winfo_children():
            for widget in self.button_frame.winfo_children():
                widget.destroy()

        room = next((r for r in self.adventure_data["rooms"] if r["name"] == room_name), None)
        if not room:
            self.textbox.insert("end", "Raum nicht gefunden.\n")
            return

        self.current_room = room
        self.textbox.delete("1.0", "end")
        self.textbox.insert("end", f"📍 {room['description']}\n\n")
        if self.minimap:
            self.minimap.raum_anzeigen(room_name)

        self.logbuch.eintrag_hinzufügen(f"📌 Raum: {room['name']} – {room['description']}")

        for key, text in room["option_texts"].items():
            ctk.CTkButton(self.button_frame, text=text, font=("Orbitron", 14), fg_color=FARBE_PRIMÄR, hover_color=FARBE_AKZENT,
                          command=lambda k=key: self.choose_option(k)).pack(pady=4, fill="x", padx=40)

        self.blut_timer = TimerLeiste(self.button_frame, self.zeit_abgelaufen)
        self.blut_timer.starten()

        ctk.CTkButton(self.button_frame, text="💾 Speichern", font=("Orbitron", 14), fg_color=FARBE_AKZENT, hover_color=FARBE_PRIMÄR,
                      command=self.zeige_speicherfenster).pack(pady=5)
        ctk.CTkButton(self.button_frame, text="🧍 Charakter anzeigen", font=("Orbitron", 14), fg_color="#444", hover_color="#666",
                      command=self.charakter_panel.toggle).pack(pady=5)

    def choose_option(self, option_key):
        if self.spiel_beendet:
            return
        if self.blut_timer:
            self.blut_timer.abbrechen()

        next_room = self.current_room["options"].get(option_key)
        if next_room:
            self.show_room(next_room)
        else:
            self.textbox.insert("end", "❌ Ungültige Option.\n")

    def zeige_speicherfenster(self):
        self.clear_window()
        SpeicherFenster(self, self.character, self.current_room["name"], lambda: self.after(100, lambda: self.show_room(self.current_room["name"])))

    def zeit_abgelaufen(self):
        self.spiel_beendet = True
        self.textbox.insert("end", "\n⏰ Du hast zu lange gezögert...\n")
        self.textbox.insert("end", "💀 Etwas packt dich aus der Dunkelheit...\n")
        self.textbox.insert("end", "GAME OVER\n")

        for widget in self.button_frame.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.configure(state="disabled")

        restart_frame = ctk.CTkFrame(self, fg_color=FARBE_HINTERGRUND)
        restart_frame.pack(pady=20)

        ctk.CTkButton(
            restart_frame,
            text="🔁 Zurück zum Hauptmenü",
            font=("Orbitron", 16, "bold"),
            fg_color=FARBE_PRIMÄR,
            hover_color=FARBE_AKZENT,
            command=self.show_start_menu
        ).pack(pady=10, padx=40, fill="x")
