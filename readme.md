# 2048 – AI Game Solver

![2048 AI Screenshot](https://github.com/user-attachments/assets/18573134-003e-41b0-90b5-c82adb5a8ec1)

A Python implementation of the classic 2048 puzzle game with **AI-powered solvers**. This project features both **command-line** and **Pygame** versions of the game and demonstrates AI strategies such as **Expectimax** and **Expectiminimax** for maximizing scores.

---

## Features

- **Playable Versions**: 
  - Command-line version (`main.py`)  
  - Pygame GUI versions (`design_ai_emm.py`, `design_manual.py`, `design_ai_emm.py`)
- **AI Strategies**:  
  - Expectimax  
  - Expectiminimax
- **High Score Optimization**: AI can consistently achieve high scores.
- **Learning Resource**: Built using basic Python and Pygame, great for learning AI in games.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Jasz-rgb/2048.git
   ```
2. Install required packages:
   ```bash
    pip install -r requirements.txt
   ```
  
  If requirements.txt is missing, install manually:
  ```bash
    pip install pygame numpy
```

---

## How to Run
1. Command-Line Version
Run the AI or manual version in your terminal:
```bash
python main.py
```

2. Pygame Versions
AI-powered Pygame game:
```bash
python design_ai_emm.py
```

3. Manual Pygame game:
```bash
python design_manual.py
```

You can also run design_ai_emm.py separately for AI with Pygame visuals.

---

## Project Structure
- 2048/
  - main.py                  # Command-line game
  - design_ai_emm.py         # Pygame AI game
  - design_manual.py         # Pygame manual game
  - README.md
  - requirements.txt
  - other files              # resources and functions

---

## Technologies Used
> Python
> Pygame
> Numpy
> AI Algorithms: Expectimax, Expectiminimax

---

## Outcome
> Created an AI capable of playing 2048 at a high skill level.

## Gained deeper understanding of AI decision-making and algorithm design in games.
