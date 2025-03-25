# 🧙‍♂️ World of Warcraft Lore Quiz Game

A simple and immersive quiz game built in Python with Tkinter, testing your knowledge of World of Warcraft lore — from the Lich King to the Burning Legion.

---

## 🕹️ Features

- Multiple-choice questions about WoW lore
- Custom background images for each question
- Immediate feedback with lore explanations
- Score tracking and summary screen
- Sound effects on start or actions
- Clean GUI using Tkinter

---

## 📁 Project Structure

```
wow-lore-quiz-game/
├── main.py                   # Entry point
├── assets/                   # Images and sound files
│   ├── images/
│   └── sounds/
├── data/                     # JSON files with questions and character lore
│   ├── questions.json
│   └── characters.json
├── gui/                      # GUI screen classes
│   ├── start_screen.py
│   ├── question_screen.py
│   ├── result_screen.py
│   └── game_window.py
├── logic/                    # Game logic
│   └── question_manager.py
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install pillow playsound
```

### 2. Run the game

```bash
python main.py
```

> ✅ Make sure you're using Python 3.10+ and that your `assets/images/` and `assets/sounds/` folders contain the necessary files.

---

## ✏️ Customization

- Add questions to `data/questions.json`
- Include character bios in `data/characters.json`
- Swap or add background images and sound effects in `assets/`
- Modify GUI styles or transitions in the `gui/` folder

---

## 🧠 Sample Question Format (`questions.json`)

```json
{
  "id": 1,
  "question": "Who was the first Lich King?",
  "options": ["Arthas Menethil", "Ner'zhul", "Kil'jaeden", "Medivh"],
  "correct_answer": "Ner'zhul",
  "lore_context": "Ner'zhul was an orc shaman who became the first Lich King.",
  "img": "arthas.jpg"
}
```

---

## 📝 License

This project is for educational and personal use only.  
World of Warcraft and related lore are property of **Blizzard Entertainment**.

---

