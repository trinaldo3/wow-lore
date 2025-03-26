import tkinter as tk
from PIL import Image, ImageTk
import json
import os

class CharacterScreen(tk.Frame):
    def __init__(self, master, back_callback):
        super().__init__(master)
        self.back_callback = back_callback
        self.characters = self.load_characters()
        self.current_index = 0
        self.bg_image = None
        self.create_widgets()

    def load_characters(self):
        with open("data/characters.json", "r") as f:
            return list(json.load(f).items())  # list of (name, data)

    def create_widgets(self):
        name, data = self.characters[self.current_index]

        # Background image
        image_path = data["image"]
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((900, 500))
            self.bg_image = ImageTk.PhotoImage(img)
            image_label = tk.Label(self, image=self.bg_image)
            image_label.pack(pady=10)

        title = tk.Label(self, text=name, font=("Helvetica", 20, "bold"))
        title.pack()

        role = tk.Label(self, text=f"{data['role']} | {data['faction']}", font=("Helvetica", 14))
        role.pack()

        bio = tk.Label(self, text=data["bio"], font=("Helvetica", 12), wraplength=550, justify="left")
        bio.pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        prev_btn = tk.Button(button_frame, text="⟵ Prev", command=self.show_prev)
        prev_btn.grid(row=0, column=0, padx=10)

        next_btn = tk.Button(button_frame, text="Next ⟶", command=self.show_next)
        next_btn.grid(row=0, column=1, padx=10)

        back_btn = tk.Button(self, text="Back to Summary", command=self.back_callback)
        back_btn.pack(pady=10)

    def show_prev(self):
        self.current_index = (self.current_index - 1) % len(self.characters)
        self.refresh()

    def show_next(self):
        self.current_index = (self.current_index + 1) % len(self.characters)
        self.refresh()

    def refresh(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_widgets()