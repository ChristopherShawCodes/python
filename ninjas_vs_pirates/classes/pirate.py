from multiprocessing.sharedctypes import Value


class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.stamina = 50

    def show_stats(self):
        print("------------------")
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nStamina: {self.stamina}")
        print("------------------")

    def attack (self,ninja):
        ninja.health -= self.strength
        print({self.name}, "used attack!")
        return self

    def defend(self,ninja):
        ninja.health -= self.speed
        self.health += ninja.speed
        print({self.name}, "used defend!")
        return self

    def special_ability(self,ninja):
        ninja.health -= 30
        self.health += 30
        self.stamina -= 20
        print({self.name}, "used their special ability, Pirate Rage!")
        return self

    def rage_quit(self,ninja):
        ninja.health -= 100
        print({self.name}, "Rage Quit! Guess they couldn't hang.")
        return self

