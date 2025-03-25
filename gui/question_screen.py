# question_screen.py
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class QuestionScreen(tk.Frame):
    def __init__(self, master, question_data, on_answer_callback):
        super().__init__(master)
        self.question_data = question_data
        self.on_answer_callback = on_answer_callback
        self.create_widgets()

    def create_widgets(self):
        question_text = self.question_data["question"]
        options = self.question_data["options"]

        pic_filename = self.question_data["img"]
        image_path = os.path.join("assets", "images", pic_filename)
        img = Image.open(image_path)
        img = img.resize((1150, 1000))
        self.bg_image = ImageTk.PhotoImage(img)

        # Display the image
        bg_label = tk.Label(self, image=self.bg_image)
        bg_label.image = self.bg_image  # prevent garbage collection
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        label = tk.Label(self, text=question_text, font=("Helvetica", 18), wraplength=500)
        label.pack(pady=20)

        for option in options:
            btn = tk.Button(
                self,
                text=option,
                font=("Helvetica", 14),
                command=lambda opt=option: self.check_answer(opt)
            )
            btn.pack(pady=5)


    def check_answer(self, selected_option):
        correct = selected_option == self.question_data["correct_answer"]

        #if correct:
           # messagebox.showinfo("Correct", f"You got it right!\n\n{self.question_data['lore_context']}")
       # else:
           # messagebox.showerror("Incorrect", f"You got it wrong! The correct answer was:\n\n{self.question_data['lore_context']}")
        self.on_answer_callback(correct, self.question_data)