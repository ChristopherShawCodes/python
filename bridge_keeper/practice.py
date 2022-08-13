answers = []

def bridge_keeper():
    name = input("What is your name?\n")
    quest = input("What is the quest you seek?\n")

    if quest == "adventure":
        print("Greetings",name,"The Adventurer")
    else:
        print("There shall be no such thing on my watch!",name,"For I am the Bridge keeper! ")
    

troll = True

while troll == True:
    troll = bridge_keeper()

