import random

answers = []

def bridge_keeper():
    
    questions = ["What will you do with the treasure you seek?", "Why do you feel you are worthy?","Before you can proceed, tell me a joke."]
    correct_answer = "help others"

    print("STOP!!!!\nThose who approach the Bridge of Death must answer me these questions three, ere the other side they see.\n")
    # the built in input function can prompt with a string, and then return whatever the user has input into the console as a string.  Even if it's a number!!!
    name = input("What is your name?\n")
    quest = input("What is your quest?\n")
    random_question = random.randint(0,len(questions)-1)
    third = input(f"{questions[random_question]}\n")

    # What is your favourite colour?
    if random_question == 0:
        # checks to see if the color has been guessed already.
        if third in answers:
            print("You have been casted into gorge!!!\n")
            return True
        else:
            answers.append(third)
            print("Right. Off you go.\n")
            return True
    # Why do you feel you are worthy?
    elif random_question == 1:
        if third == correct_answer:
            print("Wait... I don't know.  AHHHHHHH!!!!!!\nThe bridge keeper was casted into the gorge.")
            return False
        else:
            print("You have been casted into gorge!!!\n")
            return True
    # What is the capital of Assyria?
    elif random_question == 2:
        # checks for correct answer
        if third == "Ninevah":
            print("Right. Off you go.\n")
            return True
        else:
            print("You have been casted into gorge!!!\n")
            return True

isGuessing = True

while isGuessing == True:
    isGuessing = bridge_keeper()