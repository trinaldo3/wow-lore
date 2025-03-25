import tkinter as tk
from PIL import Image, ImageTk
import os
from playsound import playsound

class StartScreen(tk.Frame):
    def __init__(self, master, start_callback):
        super().__init__(master)
        self.start_callback = start_callback
        self.bg_image = None
        self.create_widgets()

    def create_widgets(self):
        # Load and resize the background image
        image_path = os.path.join("assets", "images", "Arthas.jpg")
        img = Image.open(image_path)
        img = img.resize((1150, 1000))
        self.bg_image = ImageTk.PhotoImage(img)

        # Display the image
        bg_label = tk.Label(self, image=self.bg_image)
        bg_label.image = self.bg_image  # prevent garbage collection
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title text
        title = tk.Label(
            self,
            text="World of Warcraft Lore Quiz",
            font=("Helvetica", 24, "bold"),
            bg="black",
            fg="white"
        )
        title.place(relx=0.5, y=60, anchor="center")

        # Start Quiz button
        start_button = tk.Button(
            self,
            text="Start Quiz",
            font=("Helvetica", 16),
            command=self.play_and_start
        )
        start_button.place(relx=0.5, rely=0.5, anchor="center")

    def play_and_start(self):
        sound_path = os.path.join("assets", "sounds", "notPrepared.mp3")
        playsound(sound_path)
        self.start_callback()