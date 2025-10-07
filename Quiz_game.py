# QUIZ GAME
easy_questions = ("Which Language is known as the 'Mother of all Languages",
             "Which planet is known as the 'red planet' ",
             "What is the Capital of India",
             "Which Animal is the King of the Jungle",
             "Who invented Light Bulb",
             "Which color is formed by mixing red and blue?",
             "Which is the largest mammal on Earth?",
             "What is 5 + 7?",
             "Which country is called the 'Land of the Rising Sun'?",
             "What is the boiling point of water at sea level?")

moderate_questions = ("Which data structure follows the FIFO principle?",
                      "What is the chemical formula of water?",
                      "Who wrote the Indian national anthem?",
                      "Which keyword is used to define a function in Python?",
                      "What is the full form of CPU?",
                      "Which gas do plants absorb during photosynthesis?",
                      "Who was the first Prime Minister of India?")

hard_questions = ("Which algorithm is used in Google's PageRank?",
                  "In which year was C programming language developed?",
                  "Which part of the human brain is responsible for balance and coordination?",
                  "Which data structure is used in recursion?",
                  "What is the default port number for HTTPS?",)

easy_options = (("A. C", "B. Assembly", "C. Python", "D. Java"),
                ("A. Earth", "B. Mars", "C. Venus", "D. Jupiter"),
                ("A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"),
                ("A. Tiger", "B. Elephant", "C. Lion", "D. Leopard"),
                ("A. Nikola Tesla", "B. Thomas Edison", "C. Albert Einstein", "D. Isaac Newton"),
                ("A. Green", "B. Purple", "C. Orange", "D. Brown"),
                ("A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"),
                ("A. 10", "B. 11", "C. 12", "D. 13"),
                ("A. India", "B. China", "C. Japan", "D. Thailand"),
                ("A. 90°C", "B. 95°C", "C. 100°C", "D. 110°C"))

moderate_options = (("A. Stack", "B. Queue", "C. Tree", "D. Graph"),
                    ("A. H2O", "B. CO2", "C. NaCl", "D. O2"),
                    ("A. Bankim Chandra Chatterjee", "B. Rabindranath Tagore", "C. Mahatma Gandhi", "D. Subhash Chandra Bose"),
                    ("A. function", "B. def", "C. lambda", "D. define"),
                    ("A. Central Processing Unit", "B. Computer Power Unit", "C. Control Process Utility", "D. Central Program Unit"),
                    ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
                    ("A.Sardar Patel", "B. Subhash Bose", "C. Jawaharlal Nehru", "D. Mahatma Gandhi"))

hard_options = (("A. Dijkstra's Algorithm", "B. Markov Chain", "C. Binary Search", "D. Depth-First Search"),
                ("A. 1969", "B. 1972", "C. 1975", "D. 1980"),
                ("A. Cerebrum", "B. Cerebellum", "C. Medulla", "D. Thalamus"),
                ("A. Queue", "B. Heap", "C. Stack", "D. Graph"),
                ("A. 80", "B. 21", "C. 25", "D. 443"))

easy_ans = ("A","B","B","C","B","B","B","C","C","C")

moderate_ans = ("B","A","B","B","A","C","C")

hard_ans = ("B","B","A","C","D")


from colorama import Fore, Style
def play_game():
    while True:
        guesses = []
        score = 0
        question_num = 0
        

        print("Choose the Difficulty of the Questions")
        print("1. For Easy Questions (10 Questions)",
              "2. For Moderate Questions (7 Questions)",
              "3. For Hard Questions (5 Questions)")

        choice = input("Enter 1, 2 or 3 : ")
        if choice not in ["1", "2", "3"]:
            print(Fore.RED + "Invalid choice! Enter 1, 2 or 3"+ Style.RESET_ALL)
            continue

        if choice == "1":
            question_num = 0
            for easy_question in easy_questions:
                print("----------------------")
                print(easy_question)

                for easy_option in easy_options[question_num]:
                    print(easy_option)

                while True:
                    guess = input("Enter (A,B,C,D) : ").upper().strip()
                    if guess in ["A","B","C","D"]:
                        break
                    else:
                        print(Fore.RED +"Invalid choice Type A, B, C, D"+ Style.RESET_ALL)
                guesses.append(guess)

                if guess == easy_ans[question_num]:
                    score += 1
                    print(Fore.GREEN +"CORRECT!" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "INCORRECT!"+ Style.RESET_ALL)
                    print(f"{easy_ans[question_num]} is the answer ")
                question_num += 1

        elif choice == "2":
            question_num = 0
            for moderate_question in moderate_questions:
                print("----------------------")
                print(moderate_question)

                for moderate_option in moderate_options[question_num]:
                    print(moderate_option)

                while True:
                    guess = input("Enter (A,B,C,D) : ").upper().strip()
                    if guess in ["A","B","C","D"]:
                        break
                    else:
                        print(Fore.RED +"Invalid choice Type A, B, C, D"+ Style.RESET_ALL)

                guesses.append(guess)

                if guess == moderate_ans[question_num]:
                    score += 1
                    print(Fore.GREEN +"CORRECT!" + Style.RESET_ALL)
                else:
                    print(Fore.RED +"INCORRECT!" + Style.RESET_ALL)
                    print(f"{moderate_ans[question_num]} is the answer ")
                question_num += 1

        elif choice == "3":
            question_num = 0
            for hard_question in hard_questions:
                print("----------------------")
                print(hard_question)

                for hard_option in hard_options[question_num]:
                    print(hard_option)

               

                while True:
                    guess = input("Enter (A,B,C,D) : ").upper().strip()
                    if guess in ["A","B","C","D"]:
                        break
                    else:
                        print(Fore.RED +"Invalid choice Type A, B, C, D"+ Style.RESET_ALL)

                guesses.append(guess)

                if guess == hard_ans[question_num]:
                    score += 1
                    print(Fore.GREEN +"CORRECT!"+ Style.RESET_ALL)
                else:
                    print(Fore.RED +"INCORRECT!"+ Style.RESET_ALL)
                    print(f"{hard_ans[question_num]} is the answer ")
                question_num += 1

        print("\nYour final Score", score, "/", question_num)
        break


play_game()

while True:  
        play_again = input("\nDo you want to play again? (y/yes or n/no): ").strip().lower()

        if play_again in ["y", "yes"]:
            play_game()
        elif play_again in ["n", "no"]:
            print( Fore.BLUE +"\nThank you for playing! Goodbye "+ Style.RESET_ALL)
            exit()
        else:
            print(Fore.RED +"Invalid input! Please type 'y/yes' or 'n/no'."+ Style.RESET_ALL)
   

 









