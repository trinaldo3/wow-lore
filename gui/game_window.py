import tkinter as tk
import os

from gui.start_screen import StartScreen
from gui.question_screen import QuestionScreen
from gui.result_screen import ResultScreen
from logic.question_manager import QuestionManager

class GameWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("WoW Lore Quiz")
        self.root.geometry("1150x1000")  # adjust if needed 
        self.current_screen = None

        # Load questions
        question_path = os.path.join("data", "questions.json")
        self.qm = QuestionManager(question_path)

        # Track score
        self.correct_count = 0
        self.total_questions = len(self.qm.questions)

        self.show_start_screen()

    def show_start_screen(self):
        self._switch_screen(StartScreen(self.root, self.start_game))

    def start_game(self):
        self.correct_count = 0
        self.qm.current_index = 0
        self.show_next_question()

    def show_next_question(self):
        question = self.qm.get_current_question()
        if question:
            self._switch_screen(QuestionScreen(self.root, question, self.handle_answer))
        else:
            self.show_summary()

    def handle_answer(self, correct, question_data):
        if correct:
            self.correct_count += 1

        self.qm.advance()

        self._switch_screen(
            ResultScreen(
                self.root,
                correct=correct,
                question_data=question_data,
                on_next_callback=self.show_next_question
            )
        )

    def show_summary(self):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text="Quiz Complete!", font=("Helvetica", 24))
        label.pack(pady=20)

        score_text = f"You got {self.correct_count} out of {self.total_questions} correct."
        score_label = tk.Label(frame, text=score_text, font=("Helvetica", 18))
        score_label.pack(pady=10)

        restart_button = tk.Button(frame, text="Restart", font=("Helvetica", 16), command=self.start_game)
        restart_button.pack(pady=20)

        close_button = tk.Button(frame, text="Close", font=("Helvetica", 16), command=self.root.destroy)
        close_button.pack(pady=10)

        self._switch_screen(frame)

    def _switch_screen(self, screen):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = screen
        self.current_screen.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()
