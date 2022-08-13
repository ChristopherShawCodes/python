from multiprocessing.sharedctypes import Value


numbers = [5, [7, 3, 12, 14], [8, 99, 60], 16, [9]]

#Print the following numbers using the above variable:

#1 - 16
print(numbers[3])

#2 - 12
print(numbers[1][2])

#3 - 9
print(numbers[4])
print(numbers[4][0])

fido = {"can_roll_over": True, 
        "can_fetch": False, 
        "num_times_barked": 133, 
        "owners": ["Hal", "Lois"]}

# #Print the following things using the above variable:

# #4 - False
print (fido["can_fetch"])

# #5 - "Lois"
print (fido["owners"][1])
# #6 - Change the value of the key num_times_barked to 133, and then print that same key.
print(fido["num_times_barked"])



superheroes = [
    {"name": "Wonder Woman", "power": "super strength"},
    {"name": "Flash", "power": "runs fast", "extra_field": [7, 8, 54]},
    {"name": "Aquaman", "power": "talks to aquatic creatures"},
    {"name": "Spiderman", "power": "shoots webs"}
]

#Print the following things using the above variable:

# #7 - "Aquaman"
print(superheroes[2]["name"])

# #8 - "super strength"
print(superheroes[0]["power"])

# #9 - 54
print(superheroes[1]["extra_field"][2])

#10 - Write a "for in" loop that prints all powers in the above variable. Do not use a "for in range" loop.
for x in superheroes:
    print(x["power"])
