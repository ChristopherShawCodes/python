local_val = "magical unicorns"

class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self


    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name}{food}!")
            self.pet.eat()
        else:
            print("We are out of pet food")
        return self
    

    def bathe(self):
        self.pet.noise
        return self


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
