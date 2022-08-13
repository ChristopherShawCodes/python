answers = []

def bridge_keeper():
    name = input("What is your name?\n")
    quest = input("What is the quest you seek?\n")
    
    if quest == "adventure":
        print("Greetings",name,"The Adventurer")
        print("----------------")
        follow_up_question = input("Do you know your way?")
        if follow_up_question == "yes":
            print("Safe travels",name)
            print("----------------")
        else:
            print("You'll want to see my wizard friend just past the castle gate")
            print("----------------")
    else:
        print("uh", quest, "?","There shall be no such thing on my watch", name , "For I am the Bridge keeper!")
        print("----------------")
        return False



troll = bridge_keeper()