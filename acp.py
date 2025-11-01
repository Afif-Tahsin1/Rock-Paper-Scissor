# -------------------------------
# QUIZ PROGRAM USING CLASS, CONSTRUCTOR, FUNCTIONS, LOOPS, AND CONDITIONALS
# -------------------------------

# Step 1: Define a class to represent the Quiz
class Quiz:
    # Constructor: initializes the quiz questions and score
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 5 + 3?", "answer": "8"},
            {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
            {"question": "What is the color of the sky on a clear day?", "answer": "Blue"},
            {"question": "Which language are we using now?", "answer": "Python"}
        ]
        self.score = 0

    # Step 2: Function to start the quiz
    def start(self):
        print("🧠 Welcome to the Python Quiz!")
        print("----------------------------------")

        # Step 3: Use a loop to go through each question
        for i, q in enumerate(self.questions, start=1):
            print(f"\nQuestion {i}: {q['question']}")
            user_answer = input("Your answer: ").strip()

            # Step 4: Use conditional statements to check the answer
            if user_answer.lower() == q["answer"].lower():
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Wrong! The correct answer is {q['answer']}.")

        # Step 5: Show final score
        self.show_result()

    # Step 6: Function to display the final result
    def show_result(self):
        print("\n----------------------------------")
        print(f"🏁 Quiz Finished! Your Score: {self.score}/{len(self.questions)}")
        
        # Give feedback using conditionals
        if self.score == len(self.questions):
            print("🌟 Excellent! You got all answers right!")
        elif self.score >= len(self.questions) // 2:
            print("👍 Good job! You passed!")
        else:
            print("😅 Keep practicing and try again!")

# Step 7: Create an object of the Quiz class and start it
if __name__ == "__main__":
    quiz = Quiz()  # Constructor called here
    quiz.start()