class Flower:
    been_picked = False
    
    def __init__(self,color,type,height,num_petals):
        self.color = color
        self.type = type
        self.height = height
        self.num_petals = num_petals

    def grow(self):
        self.height += 3
        self.num_petals += 2
        print("Flower Grew !")
        return self

    def custom_grow(self):
        print("How much height do you want to add to your flower?")
        self.height = input()
        print("How many more petals do you want to add to your flower?")
        self.num_petals = input()
        print("Flower has grown in height by",self.height,"and in petals by",self.num_petals)
        return self

    def picked(self):
        self.been_picked == True
        print("Flower Picked !")
        return self

    def planted(self):
        self.been_picked == False
        print("Flower Planted !")
        return self

    def stepped_on(self):
        if self.height > 1:
            self.height -= 2
            print("Flower Stepped On !")
        else:
            print("height can not go less than 1")
            return self

    def plucked(self):
        if self.num_petals > 0:
            self.num_petals -= 1
            print("Flower has been plucked !")
        else:
            print("number of petals can not go lower than 0")
            return self


    def say_info(self):
        if self.been_picked == False:
            print("------------------------------")
            print(f"Flower Color: {self.color}")
            print(f"Flower Type: {self.type}")
            print(f"Flower Height: {self.height}")
            print(f"Flower Number Of Petals: {self.num_petals}")
            print("------------------------------")
            return self
        else:
            print("Can't find the flower, has it been picked?")

rose = Flower("red","rose",4,9)
sunflower = Flower("yellow","sunflower",15,8)
rose.grow()
rose.say_info()
sunflower.say_info()
sunflower.stepped_on()
sunflower.say_info()
sunflower.plucked()
sunflower.say_info()
sunflower.stepped_on()
sunflower.say_info()
sunflower.custom_grow()

#update