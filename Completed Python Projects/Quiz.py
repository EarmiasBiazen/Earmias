def get_valid_input(prompt, valid_responses):
    while True:
        response = input(prompt).strip().upper()
        if response in valid_responses:
            return response
        print(f"Invalid, please answer with one of the following: {', '.join(valid_responses)}")

# List of quiz questions and answers
questions = [
    ("1 - What is the most populated continent?", ["a) India", "b) Europe", "c) Africa", "d) Asia"], "D"),
    ("2 - Which planet is known as the Red Planet?", ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"], "B"),
    ("3 - What is the largest ocean on Earth?", ["a) Atlantic Ocean", "b) Indian Ocean", "c) Arctic Ocean", "d) Pacific Ocean"], "D"),
]

# Prompt the user to take the quiz
user = get_valid_input('Do You Want To Take This Fun Quiz: ', ['YES', 'NO'])

if user == "NO":
    print('Thanks For Your Time!')
else:
    print("Wonderful, Let's Start!")
    
    # Loop through each question
    for question, options, correct_answer in questions:
        print(question)
        for option in options:
            print(option)
        
        attempts = 0
        while True:
            user_answer = get_valid_input("Your answer: ", ["A", "B", "C", "D"])
            attempts += 1
            
            if user_answer == correct_answer:
                print("You're right!")
                print(f"It took you {attempts} attempt(s) to get the correct answer.")
                break
            else:
                print("You're wrong! Try again.")
