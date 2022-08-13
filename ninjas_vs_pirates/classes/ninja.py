class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.stamina = 20
    
    def show_stats( self ):
        print("------------------")
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        print("------------------")

    def attack( self , pirate ):
        pirate.health -= self.strength
        print({self.name}, "used attack!")
        return self

    def defend(self,pirate):
        pirate.health -= self.speed
        self.health += pirate.speed
        print({self.name}, "used defend!")
        return self

    def special_ability(self,pirate):
        pirate.health -= 30
        self.health += 30
        self.stamina -= 20
        print({self.name}, "used their special ability, Ninja Focus!")
        return self