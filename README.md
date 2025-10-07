# Quiz-Game

A fun, interactive, and colorful Python-based Quiz Game featuring multiple difficulty levels — Easy, Moderate, and Hard.

Test your general knowledge and computer science basics with real-time scoring, replay options, and color-coded feedback using the colorama library. Perfect for beginners learning Python loops, conditionals, and user input handling!

## Features

- 🎯 **Three Difficulty Levels**: Easy, Moderate, and Hard
- 🌈 **Color-Coded Feedback**: Visual feedback using colorama library
- 📊 **Real-Time Scoring**: Track your progress as you play
- 🔄 **Replay Option**: Play multiple rounds without restarting
- 📚 **Diverse Questions**: General knowledge and computer science topics
- ✨ **Interactive Interface**: User-friendly command-line interface
- 🏆 **Performance Evaluation**: Get rated based on your score

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/akhilbedi826-rgb/Quiz-Game.git
cd Quiz-Game
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the quiz game:
```bash
python quiz_game.py
```

### How to Play

1. **Start the Game**: Run the Python script
2. **Select Difficulty**: Choose from Easy (1), Moderate (2), or Hard (3)
3. **Answer Questions**: Type A, B, C, or D for each question
4. **View Feedback**: Get instant color-coded feedback on your answers
5. **Check Score**: See your real-time score after each question
6. **Final Results**: View your final score and performance rating
7. **Play Again**: Choose to replay or exit

### Difficulty Levels

- **Easy**: Basic questions on general knowledge and fundamental computer science concepts
- **Moderate**: Intermediate questions requiring more specific knowledge
- **Hard**: Advanced questions testing deeper understanding

### Color Coding

- 🟢 **Green**: Correct answers and excellent performance
- 🟡 **Yellow**: Prompts, moderate performance
- 🔴 **Red**: Incorrect answers and poor performance
- 🔵 **Cyan/Blue**: Headers and separators
- 🟣 **Magenta**: Question categories

## Example Output

```
============================================================
           WELCOME TO THE QUIZ GAME!
============================================================

Test your knowledge with multiple difficulty levels!
Get color-coded feedback and track your score in real-time!

Select Difficulty Level:
1. Easy
2. Moderate
3. Hard

Enter your choice (1-3): 1
✓ Easy level selected!

============================================================
Question 1/5
Category: General Knowledge
============================================================

What is the capital of France?
A) London
B) Berlin
C) Paris
D) Madrid

Your answer (A/B/C/D): C

✓ CORRECT! Well done!

------------------------------------------------------------
Current Score: 1/1 (100.0%)
------------------------------------------------------------
```

## Learning Concepts

This project demonstrates several Python programming concepts:

- **Loops**: `while` and `for` loops for game flow and question iteration
- **Conditionals**: `if-elif-else` statements for answer validation and scoring
- **User Input**: `input()` function for interactive gameplay
- **Data Structures**: Dictionaries and lists for organizing questions
- **Object-Oriented Programming**: Class-based design with methods
- **Error Handling**: Try-except blocks for graceful interruption handling
- **External Libraries**: Using colorama for enhanced user experience

## Project Structure

```
Quiz-Game/
├── quiz_game.py       # Main game file
├── requirements.txt   # Python dependencies
├── README.md         # Project documentation
└── .gitignore       # Git ignore file
```

## Dependencies

- **colorama** (0.4.6): Cross-platform colored terminal text

## Contributing

Contributions are welcome! Feel free to:
- Add more questions
- Improve the scoring system
- Add new difficulty levels
- Enhance the user interface

## License

This project is open source and available for educational purposes.

## Author

Created for learning and fun! Perfect for Python beginners to understand basic programming concepts.
