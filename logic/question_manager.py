import json

class QuestionManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.questions = self.load_questions()
        self.current_index = 0

    def load_questions(self):
        with open(self.filepath, "r") as f:
            return json.load(f)

    def get_current_question(self):
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        else:
            return None

    def advance(self):
        self.current_index += 1
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        else:
            return None
