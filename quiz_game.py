"""
Quiz Game - A fun, interactive Python quiz with multiple difficulty levels
Features: color-coded feedback, real-time scoring, and replay options
"""

from colorama import Fore, Style, init
import sys

# Initialize colorama
init(autoreset=True)


class QuizGame:
    """Main Quiz Game class with multiple difficulty levels"""
    
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.difficulty = None
        
        # Quiz questions organized by difficulty level
        self.questions = {
            'easy': [
                {
                    'question': 'What is the capital of France?',
                    'options': ['A) London', 'B) Berlin', 'C) Paris', 'D) Madrid'],
                    'answer': 'C',
                    'category': 'General Knowledge'
                },
                {
                    'question': 'What is 2 + 2?',
                    'options': ['A) 3', 'B) 4', 'C) 5', 'D) 6'],
                    'answer': 'B',
                    'category': 'General Knowledge'
                },
                {
                    'question': 'Which planet is known as the Red Planet?',
                    'options': ['A) Venus', 'B) Mars', 'C) Jupiter', 'D) Saturn'],
                    'answer': 'B',
                    'category': 'General Knowledge'
                },
                {
                    'question': 'What does CPU stand for in computers?',
                    'options': ['A) Central Processing Unit', 'B) Computer Personal Unit', 
                               'C) Central Program Utility', 'D) Computer Processing Unit'],
                    'answer': 'A',
                    'category': 'Computer Science'
                },
                {
                    'question': 'Which programming language is known for its use in web development?',
                    'options': ['A) Python', 'B) JavaScript', 'C) Java', 'D) C++'],
                    'answer': 'B',
                    'category': 'Computer Science'
                },
            ],
            'moderate': [
                {
                    'question': 'Who wrote the play "Romeo and Juliet"?',
                    'options': ['A) Charles Dickens', 'B) William Shakespeare', 
                               'C) Jane Austen', 'D) Mark Twain'],
                    'answer': 'B',
                    'category': 'General Knowledge'
                },
                {
                    'question': 'What is the largest ocean on Earth?',
                    'options': ['A) Atlantic Ocean', 'B) Indian Ocean', 
                               'C) Arctic Ocean', 'D) Pacific Ocean'],
                    'answer': 'D',
                    'category': 'General Knowledge'
                },
                {
                    'question': 'In which year did World War II end?',
                    'options': ['A) 1943', 'B) 1944', 'C) 1945', 'D) 1946'],
                    'answer': 'C',
                    'category': 'General Knowledge'
                },
                {
                    'question': 'What does HTML stand for?',
                    'options': ['A) Hyper Text Markup Language', 'B) High Tech Modern Language',
                               'C) Home Tool Markup Language', 'D) Hyperlinks and Text Markup Language'],
                    'answer': 'A',
                    'category': 'Computer Science'
                },
                {
                    'question': 'Which data structure uses LIFO (Last In First Out)?',
                    'options': ['A) Queue', 'B) Stack', 'C) Array', 'D) Tree'],
                    'answer': 'B',
                    'category': 'Computer Science'
                },
            ],
            'hard': [
                {
                    'question': 'What is the smallest prime number?',
                    'options': ['A) 0', 'B) 1', 'C) 2', 'D) 3'],
                    'answer': 'C',
                    'category': 'General Knowledge'
                },
                {
                    'question': 'Which element has the atomic number 79?',
                    'options': ['A) Silver', 'B) Gold', 'C) Platinum', 'D) Mercury'],
                    'answer': 'B',
                    'category': 'General Knowledge'
                },
                {
                    'question': 'Who developed the theory of relativity?',
                    'options': ['A) Isaac Newton', 'B) Nikola Tesla', 
                               'C) Albert Einstein', 'D) Stephen Hawking'],
                    'answer': 'C',
                    'category': 'General Knowledge'
                },
                {
                    'question': 'What is the time complexity of binary search?',
                    'options': ['A) O(n)', 'B) O(log n)', 'C) O(n^2)', 'D) O(1)'],
                    'answer': 'B',
                    'category': 'Computer Science'
                },
                {
                    'question': 'Which sorting algorithm has the best average-case time complexity?',
                    'options': ['A) Bubble Sort', 'B) Quick Sort', 
                               'C) Insertion Sort', 'D) Selection Sort'],
                    'answer': 'B',
                    'category': 'Computer Science'
                },
            ]
        }
    
    def display_welcome(self):
        """Display welcome message with colorful formatting"""
        print(Fore.CYAN + "=" * 60)
        print(Fore.YELLOW + Style.BRIGHT + "   WELCOME TO THE QUIZ GAME!".center(60))
        print(Fore.CYAN + "=" * 60)
        print(Fore.GREEN + "\nTest your knowledge with multiple difficulty levels!")
        print(Fore.GREEN + "Get color-coded feedback and track your score in real-time!\n")
    
    def select_difficulty(self):
        """Allow user to select difficulty level"""
        print(Fore.CYAN + "\nSelect Difficulty Level:")
        print(Fore.WHITE + "1. Easy")
        print(Fore.WHITE + "2. Moderate")
        print(Fore.WHITE + "3. Hard")
        
        while True:
            choice = input(Fore.YELLOW + "\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                self.difficulty = 'easy'
                print(Fore.GREEN + "✓ Easy level selected!")
                break
            elif choice == '2':
                self.difficulty = 'moderate'
                print(Fore.GREEN + "✓ Moderate level selected!")
                break
            elif choice == '3':
                self.difficulty = 'hard'
                print(Fore.GREEN + "✓ Hard level selected!")
                break
            else:
                print(Fore.RED + "✗ Invalid choice! Please enter 1, 2, or 3.")
    
    def ask_question(self, question_data, question_number):
        """Display a question and get user's answer"""
        print(Fore.CYAN + "\n" + "=" * 60)
        print(Fore.WHITE + Style.BRIGHT + f"Question {question_number}/{self.total_questions}")
        print(Fore.MAGENTA + f"Category: {question_data['category']}")
        print(Fore.CYAN + "=" * 60)
        print(Fore.WHITE + "\n" + question_data['question'])
        
        # Display options
        for option in question_data['options']:
            print(Fore.WHITE + option)
        
        # Get user's answer
        while True:
            answer = input(Fore.YELLOW + "\nYour answer (A/B/C/D): ").strip().upper()
            
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            else:
                print(Fore.RED + "✗ Invalid input! Please enter A, B, C, or D.")
    
    def check_answer(self, user_answer, correct_answer):
        """Check if the answer is correct and provide feedback"""
        if user_answer == correct_answer:
            print(Fore.GREEN + Style.BRIGHT + "\n✓ CORRECT! Well done!")
            self.score += 1
            return True
        else:
            print(Fore.RED + Style.BRIGHT + f"\n✗ INCORRECT! The correct answer was {correct_answer}.")
            return False
    
    def display_score(self):
        """Display current score"""
        percentage = (self.score / self.total_questions * 100) if self.total_questions > 0 else 0
        print(Fore.CYAN + "\n" + "-" * 60)
        print(Fore.YELLOW + Style.BRIGHT + f"Current Score: {self.score}/{self.total_questions} ({percentage:.1f}%)")
        print(Fore.CYAN + "-" * 60)
    
    def display_final_results(self):
        """Display final quiz results with performance evaluation"""
        percentage = (self.score / self.total_questions * 100) if self.total_questions > 0 else 0
        
        print(Fore.CYAN + "\n" + "=" * 60)
        print(Fore.YELLOW + Style.BRIGHT + "   QUIZ COMPLETED!".center(60))
        print(Fore.CYAN + "=" * 60)
        print(Fore.WHITE + f"\nDifficulty Level: {self.difficulty.capitalize()}")
        print(Fore.WHITE + f"Total Questions: {self.total_questions}")
        print(Fore.WHITE + f"Correct Answers: {self.score}")
        print(Fore.WHITE + f"Incorrect Answers: {self.total_questions - self.score}")
        
        # Color-coded percentage display
        if percentage >= 80:
            print(Fore.GREEN + Style.BRIGHT + f"\nFinal Score: {percentage:.1f}%")
            print(Fore.GREEN + "★ Excellent! You're a quiz master!")
        elif percentage >= 60:
            print(Fore.YELLOW + Style.BRIGHT + f"\nFinal Score: {percentage:.1f}%")
            print(Fore.YELLOW + "★ Good job! Keep practicing!")
        else:
            print(Fore.RED + Style.BRIGHT + f"\nFinal Score: {percentage:.1f}%")
            print(Fore.RED + "★ Keep learning! You'll do better next time!")
        
        print(Fore.CYAN + "=" * 60)
    
    def play_quiz(self):
        """Main game loop"""
        # Get questions for selected difficulty
        quiz_questions = self.questions[self.difficulty]
        self.total_questions = len(quiz_questions)
        
        # Ask each question
        for i, question_data in enumerate(quiz_questions, 1):
            user_answer = self.ask_question(question_data, i)
            self.check_answer(user_answer, question_data['answer'])
            self.display_score()
        
        # Display final results
        self.display_final_results()
    
    def ask_replay(self):
        """Ask if user wants to play again"""
        print(Fore.CYAN + "\n" + "-" * 60)
        while True:
            choice = input(Fore.YELLOW + "Would you like to play again? (Y/N): ").strip().upper()
            
            if choice == 'Y':
                return True
            elif choice == 'N':
                return False
            else:
                print(Fore.RED + "✗ Invalid input! Please enter Y or N.")
    
    def reset_game(self):
        """Reset game state for replay"""
        self.score = 0
        self.total_questions = 0
        self.difficulty = None


def main():
    """Main entry point for the quiz game"""
    game = QuizGame()
    
    # Display welcome message once
    game.display_welcome()
    
    # Game loop with replay option
    while True:
        # Select difficulty and play
        game.select_difficulty()
        game.play_quiz()
        
        # Ask if user wants to play again
        if game.ask_replay():
            game.reset_game()
            print(Fore.GREEN + "\n" + "=" * 60)
            print(Fore.GREEN + "Starting new game...")
            print(Fore.GREEN + "=" * 60)
        else:
            print(Fore.CYAN + "\n" + "=" * 60)
            print(Fore.YELLOW + Style.BRIGHT + "   Thank you for playing!".center(60))
            print(Fore.GREEN + "   See you next time!".center(60))
            print(Fore.CYAN + "=" * 60 + "\n")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)
