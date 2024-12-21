# Quiz game
# Step 1: Define the questions, options, and answers
def quiz_game():
    questions = [
        {
            "question": "What is the capital of Germany?",
            "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
            "answer": "C"
        },
        {
            "question": "What is the largest mammal in the planet?",
            "options": ["A. Elephant", "B. Blue whale", "C. Giraffe", "D. Orca"],
            "answer": "B"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A. Ag", "B. Au", "C. Hg", "D. Pb"],
            "answer": "B"
        },
        {
            "question": "Which programming language is known as the language of the web?",
            "options": ["A. Java", "B. Python", "C. JavaScript", "D. C++"],
            "answer": "C"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Saturn", "C. Jupiter", "D. Uranus"],
            "answer": "C"
        }
    ]

    # Step 2: Initialize variables
    score = 0
    total_questions = len(questions)

    # Step 3: Iterate through the questions and options
    for index, question in enumerate(questions, 1):
        print(f"\nQuestion {index}: {question['question']}")
        for option in question["options"]:
            print(f"{option}")
        
        # Get the user's answer
        user_answer = input("\nEnter your answer (A, B, C, or D): ").upper()

        # Validate the user's input
        while user_answer not in ["A", "B", "C", "D"]:
            user_answer = input("Invalid option. Please select A, B, C, or D: ").upper()

        # Check the answer
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong!, the correct answer is {question['answer']}")
    
    # Step 4: Display the final score
    print(f"\n--- Quiz Over! ---")
    print(f"Your final score is {score} out of {total_questions}.")
    if score == total_questions:
        print("Congratulations, you got a perfect score!")
    elif score > total_questions / 2:
        print("Good job, you got more than half of the questions correct!")
    else:
        print("Better luck next time!")

# Run the game
quiz_game()
