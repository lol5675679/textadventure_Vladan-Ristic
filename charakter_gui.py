import customtkinter as ctk
import random
import os
import sys
import platform
from PIL import Image
from customtkinter import CTkImage

# Für PyInstaller-kompatiblen Pfad
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FARBE_HINTERGRUND = "#2E3437"
FARBE_PRIMÄR = "#B02E48"
FARBE_AKZENT = "#0C4C70"
FARBE_TEXT = "#FFFFFF"

KI_NAMEN = ["Dr. Vex", "Sera Kael", "Nulla-77", "Ionis", "Zeta Varn", "Cora-X"]

if platform.system() == "Windows":
    import winsound
else:
    from playsound import playsound

def spiele_sound(dateiname="click.wav"):
    path = os.path.join(BASE_DIR, "assets", dateiname)
    if os.path.exists(path):
        if platform.system() == "Windows":
            winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
        else:
            playsound(path, block=False)

def generiere_name():
    return random.choice(KI_NAMEN)

class CharakterErstellung(ctk.CTkFrame):
    def __init__(self, master, character, callback):
        super().__init__(master, fg_color=FARBE_HINTERGRUND)
        self.master = master
        self.character = character
        self.callback = callback
        self.remaining_points = 10
        self.sliders = {}
        self.slider_labels = {}
        self.scan_animation = None
        self.pack(fill="both", expand=True)

        self.step1()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def step1(self):
        self.clear_window()

        haupt_frame = ctk.CTkFrame(self, fg_color=FARBE_HINTERGRUND)
        haupt_frame.pack(fill="both", expand=True, padx=40, pady=30)

        eingabe_frame = ctk.CTkFrame(haupt_frame, fg_color=FARBE_HINTERGRUND)
        eingabe_frame.pack(side="left", fill="both", expand=True, padx=(0, 20))

        profil_frame = ctk.CTkFrame(haupt_frame, width=300, fg_color="#1c1f21")
        profil_frame.pack(side="right", fill="y", padx=10, pady=10)

        ctk.CTkLabel(eingabe_frame, text="🧬 Charakter erstellen (Schritt 1/2)", font=("Orbitron", 20, "bold"), text_color=FARBE_PRIMÄR).pack(pady=(0, 20))

        self.name_var = ctk.StringVar()
        ctk.CTkLabel(eingabe_frame, text="🪪 Name:", font=("Orbitron", 16), text_color=FARBE_TEXT).pack(anchor="w")
        name_frame = ctk.CTkFrame(eingabe_frame, fg_color=FARBE_HINTERGRUND)
        name_frame.pack(fill="x", pady=5)
        self.name_entry = ctk.CTkEntry(name_frame, textvariable=self.name_var)
        self.name_entry.pack(side="left", fill="x", expand=True)
        ctk.CTkButton(name_frame, text="🔀", width=40, command=lambda: [spiele_sound("blip.wav"), self.name_random()]).pack(side="left", padx=5)

        self.age_var = ctk.StringVar()
        ctk.CTkLabel(eingabe_frame, text="🎂 Alter:", font=("Orbitron", 16), text_color=FARBE_TEXT).pack(anchor="w", pady=(10, 0))
        self.age_entry = ctk.CTkEntry(eingabe_frame, textvariable=self.age_var)
        self.age_entry.pack(fill="x")

        self.gender_var = ctk.StringVar()
        ctk.CTkLabel(eingabe_frame, text="⚧ Geschlecht (m/w/d):", font=("Orbitron", 16), text_color=FARBE_TEXT).pack(anchor="w", pady=(10, 0))
        self.gender_entry = ctk.CTkEntry(eingabe_frame, textvariable=self.gender_var)
        self.gender_entry.pack(fill="x")

        ctk.CTkButton(eingabe_frame, text="🔓 Weiter zu Fähigkeiten", font=("Orbitron", 16), fg_color=FARBE_PRIMÄR,
                      hover_color=FARBE_AKZENT, command=lambda: [spiele_sound("confirm.wav"), self.step2()]).pack(pady=30)

        self.profil_label = ctk.CTkLabel(profil_frame, text="", justify="left", font=("Orbitron", 14), text_color=FARBE_TEXT)
        self.profil_label.pack(pady=20, padx=10)

        self.avatar = ctk.CTkLabel(profil_frame, text="")
        self.avatar.pack(pady=20)
        self.update_avatar_bild()

        self.scan = ctk.CTkProgressBar(profil_frame, height=6, progress_color=FARBE_PRIMÄR)
        self.scan.pack(fill="x", padx=10, pady=(5, 15))
        self.scan.set(0.0)
        self.animate_scan()

        self.name_var.trace("w", lambda *args: self.update_profil())
        self.age_var.trace("w", lambda *args: self.update_profil())
        self.gender_var.trace("w", lambda *args: self.update_profil())
        self.gender_var.trace("w", lambda *args: self.update_avatar_bild())
        self.update_profil()

    def update_avatar_bild(self):
        gender = self.gender_var.get().lower()
        if gender == "m":
            bild_pfad = os.path.join(BASE_DIR, "assets", "avatar_m.png")
        elif gender == "w":
            bild_pfad = os.path.join(BASE_DIR, "assets", "avatar_w.png")
        elif gender == "d":
            bild_pfad = os.path.join(BASE_DIR, "assets", "avatar_d.png")
        else:
            bild_pfad = os.path.join(BASE_DIR, "assets", "avatar.png")

        if os.path.exists(bild_pfad):
            bild = Image.open(bild_pfad)
            avatar_img = CTkImage(light_image=bild, size=(150, 150))
            self.avatar.configure(image=avatar_img, text="")
            self.avatar.image = avatar_img
        else:
            self.avatar.configure(image=None, text="")

    def name_random(self):
        self.name_var.set(generiere_name())

    def update_profil(self):
        name = self.name_var.get()
        age = self.age_var.get()
        gender = self.gender_var.get()
        profil_text = f"🪪 Name: {name}\n🎂 Alter: {age}\n⚧ Geschlecht: {gender}"
        self.profil_label.configure(text=profil_text)

    def animate_scan(self):
        if not self.winfo_exists():
            return
        current = self.scan.get()
        self.scan.set(0.0 if current >= 1.0 else current + 0.02)
        self.scan_animation = self.after(50, self.animate_scan)

    def step2(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get().lower()

        if not name or not age.isdigit() or gender not in ["m", "w", "d"]:
            return

        if self.scan_animation:
            self.after_cancel(self.scan_animation)

        self.character.name = name
        self.character.age = int(age)
        self.character.gender = {"m": "männlich", "w": "weiblich", "d": "divers"}[gender]

        self.clear_window()

        frame = ctk.CTkFrame(self, fg_color=FARBE_HINTERGRUND)
        frame.pack(padx=40, pady=40, fill="both", expand=True)

        ctk.CTkLabel(frame, text="📊 Fähigkeiten verteilen (Schritt 2/2)", font=("Orbitron", 20, "bold"), text_color=FARBE_PRIMÄR).pack(pady=10)
        self.points_label = ctk.CTkLabel(frame, text="Verbleibende Punkte: 10", font=("Orbitron", 16), text_color=FARBE_TEXT)
        self.points_label.pack(pady=(0, 20))

        self.character.skills = {"Stärke": 0, "Intelligenz": 0, "Geschick": 0, "Willenskraft": 0}

        slider_frame = ctk.CTkFrame(frame, fg_color="#1c1f21")
        slider_frame.pack(pady=10, padx=20, fill="x")

        for skill in self.character.skills:
            skill_row = ctk.CTkFrame(slider_frame, fg_color=FARBE_HINTERGRUND)
            skill_row.pack(fill="x", pady=10)

            label = ctk.CTkLabel(skill_row, text=skill, width=120, anchor="w", font=("Orbitron", 14), text_color=FARBE_TEXT)
            label.pack(side="left")

            value_label = ctk.CTkLabel(skill_row, text="0", width=30, font=("Orbitron", 14, "bold"), text_color=FARBE_TEXT)
            value_label.pack(side="right", padx=(10, 0))

            slider = ctk.CTkSlider(skill_row, from_=0, to=10, number_of_steps=10, command=lambda val, s=skill: self.update_points(s, val))
            slider.set(0)
            slider.configure(height=18, progress_color=FARBE_PRIMÄR, button_color=FARBE_PRIMÄR, button_hover_color=FARBE_AKZENT)
            slider.pack(side="right", expand=True, fill="x", padx=(10, 10))

            self.sliders[skill] = slider
            self.slider_labels[skill] = value_label

        ctk.CTkButton(frame, text="✅ Fertig", command=lambda: [spiele_sound("confirm.wav"), self.finish()], font=("Orbitron", 16), fg_color=FARBE_PRIMÄR, hover_color=FARBE_AKZENT).pack(pady=30)

    def update_points(self, skill, value):
        self.slider_labels[skill].configure(text=str(int(value)))
        total = sum(int(slider.get()) for slider in self.sliders.values())
        remaining = 10 - total
        self.points_label.configure(text=f"Verbleibende Punkte: {remaining}")
        self.points_label.configure(text_color="red" if remaining < 0 else FARBE_TEXT)

    def finish(self):
        total = sum(int(slider.get()) for slider in self.sliders.values())
        if total > 10:
            return

        for skill, slider in self.sliders.items():
            self.character.skills[skill] = int(slider.get())

        self.callback()
