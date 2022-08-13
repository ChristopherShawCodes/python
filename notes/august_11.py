# class Beverage:
#     def __init__(self,brand,type,color):
#         self.brand = brand 
#         self.type = type
#         self.color = color
#         self.alcoholic = True 

#     def make_drink(self,brand,type,color):
#         pass


# class Food:
#     def __init__(self,brand,type,taste,color):
#         self.brand = Beverage(brand,type,color)
#         self.type = type
#         self.taste = taste
#         return self

#     def display_info(self):
#         for x in range(0,len(Food)):
#             print(Food(self.brand),(self.type),(self.taste))


# Walmart = Food("Walmart","Retail","Great","Green")
# print(Walmart.brand)


children = [
    {"name": "Tommy","age":2},
    {"name": "Rachel","age":4},
    {"name": "Susan","age":1},
    {"name": "Albert","age":6},
]

# for child in children:
#     print(child['name'])

for elephant in children:
    print(elephant['name'])

    print(f"{elephant['name']} is {elephant['age']} years old")


def addNums(a,b):
    print(a + b)

addNums(2,3)
