import ninja_pet

class Pet:
    def __init__(self,name,type,tricks,noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self


    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self


    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    
    # noise() - prints out the pet's sound
    def noise(self):
        print(self.noise)

my_treats = ['Snausages','Bacon','Generic Treat']
my_pet_food = ['Average Dog Food','Organic Dog Food','Cheap Dog Food']

fido = Pet("Fido","Dog",["Speak, Sit"],"Bark Bark")
max = Ninja("Max","Goofy",my_treats,my_pet_food,fido)

max.feed()
max.feed()
max.feed()
max.feed()