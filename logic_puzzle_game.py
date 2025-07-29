# Logic Puzzle Game 
# Raphael_Bekele_100864017

questions = [
    ("John is tired and hungry.", "P and Q", "Let P = John is tired; Q = John is hungry."),
    ("It is raining or it is sunny.", "P or Q", "Let P = It is raining; Q = It is sunny."),
    ("If it snows, then it is cold outside.", "If P then Q", "Let P = It snows; Q = It is cold outside."),
    ("All snakes are reptiles.", "For all x, if Snake(xP ) then Reptile(x)", "Universal quantifier."),
    ("There exists someone who loves coffee.", "There exists x such that Loves(x, coffee)", "Existential quantifier.")
]

def run_game():
    print("Welcome to the Logic Puzzle Game!\n")
    
    score = 0
    
    for i, (question, correct_answer, hint) in enumerate(questions, start=1):
        print(f"Question {i}: {question}")
        print(f"Hint: {hint}")
        
        player_answer = input("Enter your logical expression: ").strip().lower().replace(" ", "")
        formatted_correct_answer = correct_answer.strip().lower().replace(" ", "")
        
        if player_answer == formatted_correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: '{correct_answer}'.\n")
    
    print(f"Your total score was: {score}/{len(questions)}")
    print("Thanks for playing!")

if __name__ == "__main__":
    run_game()
