# result_screen.py
import tkinter as tk

class ResultScreen(tk.Frame):
    def __init__(self, master, correct, question_data, on_next_callback):
        super().__init__(master)
        self.correct = correct
        self.question_data = question_data
        self.on_next_callback = on_next_callback
        self.create_widgets()

    def create_widgets(self):
        result_text = "✅ Correct!" if self.correct else f"❌ Incorrect! The correct answer was: {self.question_data['correct_answer']}"

        result_label = tk.Label(self, text=result_text, font=("Helvetica", 18), fg="green" if self.correct else "red")
        result_label.pack(pady=20)

        lore_label = tk.Label(self, text=self.question_data["lore_context"], wraplength=500, font=("Helvetica", 14))
        lore_label.pack(pady=10)

        next_button = tk.Button(self, text="Next", font=("Helvetica", 16), command=self.on_next_callback)
        next_button.pack(pady=20)