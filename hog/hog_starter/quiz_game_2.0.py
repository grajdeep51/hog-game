questions = ["What was the last name of the first President of the United States?\n", 
             "What is the 90s sitcom featuring characters named Phoebe, Ross, Rachel, Monica, Chandler, and Joey?\n",
             "The fast food restaurant 'In n Out' is known for being in which American state?\n",
             "Did you wash your ass today?\n"]
answers = ["Washington", "Friends", "California", "Yes"]

score = 0

menu = input("Welcome to Big Booty Trivia! Would you like to play?\n").lower()

if menu == "yes" or menu == 'yea' or menu == 'yee':
    print("\nWonderful! Let's begin.\n")
else:
    print("Screw you.")
    quit()

for question in range(len(questions)):
    n = 0
    while n < 2:
        answer = input(questions[n])
        if answer == answers[n].lower():
            print("\nCorrect! Let's move on.\n")
            score += 1
        else:
            print("\nWRONGGG. LMAOOOO DUMBASSSS THESE QUESTIONS AREN'T EVEN HARDDD BOZO\n")
        n += 1
        if n == 2:
            break
    
if input(questions[3]) == answers[3].lower():
    print("\nCorrect! Nice job.\n")
else:
    print("\nWrong again... your time is up.")    
print(f"\nYou got {score}/4 questions correct. Your final score is {(score/4)*100}%.\n")     