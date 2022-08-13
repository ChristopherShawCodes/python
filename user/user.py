# Assignment: User
# For this assignment you will create the user class and add a couple methods!

####### Note: NOT ALL CODE FROM THE VIDEO IS PROVIDED #######

class user:

    def __init__(self,first_name, last_name, email, age, is_rewards_member, gold_card_points):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.age = age 
            self.is_rewards_member = False
            self.gold_card_points = 0
            
    # Methods:
    # display_info(self) - Have this method print all 
    # of the users' details on separate lines.

    def display_info(self):
        # Prints each item on a seperate line
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points Balance: {self.gold_card_points}")
        return self

    def enroll(self):
        # Have this method change the user's member status to True and gold points to 200
        #check if user is a mamber if they are print "user already a member" and return False, otherwise return True
        if self.is_rewards_member:
            print("User already a member.")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self,amount):
        #add logic to the spend_points method to be sure they have enough points to spend that amount and handle appropriately.
        self.gold_card_points = self.gold_card_points - amount
        if self.gold_card_points < amount:
            print("You don't have enough points")
            return self
        #decrease the user's points by the amount specified



user_one = user("Christopher", "Shaw", "admin@thejitteryape.io", "33","","")
user_one.enroll().display_info()


