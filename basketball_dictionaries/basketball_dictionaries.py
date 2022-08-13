class Player:
    def __init__(self,player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"] 
        self.team = player_dict["team"]

    def __repr__(self):
        return "Player: {}, {} y/o, pos: {}, team: {}".format(self.name,self.age,self.position,self.team)

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward",
    	"team": "Brooklyn Nets"
}

jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
# print(kevin["name"],kevin["age"],kevin["position"],kevin["team"]) same as line 8+9 but it 
# creates a method to display the info 
#  for all players instead of printing each one as it is called individually 


# Create player objects with the above dictionaries 

player_kevin = Player(kevin)
print(player_kevin)

player_jason = Player(jason)
print(player_jason)

player_kyrie = Player(kyrie)
print(player_kyrie)


# Finally, given the example list of players at the top of this module (the one with many players)
#  write a for loop that will populate an empty list with Player objects from the original list of
#   dictionaries.

# # ... (class definition and large list of players here)
# new_team = []
# Write your for loop here to populate the new_team variable with Player objects.



players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

#for loop over the list of dictionaries
    #each time use that dictionary info 
    # to create a new player instance
new_team = []
# for value in list 
for player_dict in players:
    player = Player(player_dict)
    # new_team.append(object)
    new_team.append(player)

print(new_team)

