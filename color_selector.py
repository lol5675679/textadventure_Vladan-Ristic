import customtkinter as ctk

class ColorSelector(ctk.CTkFrame):
    def __init__(self, master, title: str, options: list[str], callback):
        super().__init__(master)
        self.options = options
        self.index = 0
        self.callback = callback  # Wird aufgerufen bei Änderung
        self.title = title

        ctk.CTkLabel(self, text=title, font=("Arial", 14, "bold")).pack(pady=(5, 0))

        nav_frame = ctk.CTkFrame(self)
        nav_frame.pack(pady=5)

        self.left_btn = ctk.CTkButton(nav_frame, text="⬅", width=40, command=self.prev)
        self.left_btn.pack(side="left", padx=5)

        self.display_label = ctk.CTkLabel(nav_frame, text=self.options[self.index], font=("Arial", 14), width=120)
        self.display_label.pack(side="left", padx=5)

        self.right_btn = ctk.CTkButton(nav_frame, text="➡", width=40, command=self.next)
        self.right_btn.pack(side="left", padx=5)

    def prev(self):
        self.index = (self.index - 1) % len(self.options)
        self.update_display()

    def next(self):
        self.index = (self.index + 1) % len(self.options)
        self.update_display()

    def update_display(self):
        self.display_label.configure(text=self.options[self.index])
        self.callback(self.options[self.index])

    def get_value(self):
        return self.options[self.index]
