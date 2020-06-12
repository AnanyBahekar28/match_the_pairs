print("    Sportsmen     |    Sport    ")
print("__________________|_____________")
print("                  |             ")
print("1. Virat Kohli    | a. Tennis")
print("2. Leander Paes   | b. Boxing")
print("3. P.V.Sindhu     | c. Cricket")
print("4. Mary Kom       | d. Shooting")
print("5. Abhinav Bindra | e. Badminton")

questions = ["Virat Kohli", "Leander Paes", "P.V.Sindhu", "Mary Kom", "Abhinav Bindra"]
answers = ["c", "a", "e", "b", "d"]
score = 0

for i in range(0, len(questions), 1):
    user_ans = input(f"Enter the option for {questions[i]}: ").lower()
    while user_ans not in answers: # for checking if user has entered a valid input
        print("Invalid input") # for checking if user has entered a valid input
        user_ans = input(f"Enter the option for {questions[i]}: ").lower() # for checking if user has entered a valid input
        if user_ans not in answers: # for checking if user has entered a valid input
            print("Invalid input")
    if user_ans == answers[i]:
        print("Right answer")
    else:
        print("Wrong answer")
    print("--------------------------------------")
