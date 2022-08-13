# person = {"first":"Aiden", "last":"Shaw", "age" : 8, "lives in tn":True}
#can also be written out as 
person = {
    "first":"Aiden",
    "last":"Shaw",
    "age" : 8,
    "lives in tn":True
}

# person["email"] = "aiden@google.com"
# print(person)

# person["email"] = "wrongemailprovided@google.com"

# if "email" not in person:
#     person["email"] = "wrongemail@gmail.com"

print(person["email"]) #prints email only
print(person) #prints list and adds value to that list



#DICTIONARY NOTES
#List of Dictionaries 
# users = [
#     {"first": "Aiden", "last": "Shaw"}, #INDEX 0
#     {"first": "Christopher", "last": "Shaw", "birthday": "December 6th"}, #INDEX 1
#     {"first": "Brittany", "last": "Shaw"} #INDEX 2
# ]

# print(users[0]["last"])
# #output = {'first': 'Aiden', 'last': 'Shaw'}

#hardcoded dictionary example
# first_user = {"first": "Billy", "last": "Joe"}
# print(first_user["last"])

resumes = [
{
    "skills": ["front-enda", "back-enda", "databasea"],
    "languages": ["Pythona", "Javascripta"],
    "hobbies": ["racing", "video-games"]
},
{
    "skills": ["front-endb", "back-endb", "databaseb"],
    "languages": ["Pythonb", "Javascriptb"],
    "hobbies": ["racingb", "video-gamesb"]
},
{
    "skills": ["front-endc", "back-endc", "databasec"],
    "languages": ["Pythonc", "Javascriptc"],
    "hobbies": ["racingc", "video-gamesc"]
}
]

print (resumes[1]["languages"][0])
