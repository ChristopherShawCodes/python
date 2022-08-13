
#character is a blueprint holding Woody and buzz currently
class Character:
    def __init__(self,toy_name,toy_catchphrase):#movie_name,movie_genre
        self.name = toy_name
        self.catchphrase = toy_catchphrase
        self.numFans = 0
        self.film = None 
        # self.film = Movie(movie_name,movie_genre) SECOND example. This line coorelates with above

    def say_catchphrase(self):
        print(self.catchphrase)
        return self

    def getFans(self, amountOfFans):
        self.numFans += amountOfFans
        return self

#second class
class Movie:
    def __init__(self,movie_title, movie_genre):
        self.title = movie_title
        self.genre = movie_genre



buzz = Character("Buzz Lightyear", "To infinity and beyond!")
print(buzz.name)
woody = Character("Woody", "Your my favorite deputy")

woody.say_catchphrase().say_catchphrase()
buzz.say_catchphrase().getFans(31)

print(woody.numFans)
woody.getFans(5)
print(woody.numFans)
print(buzz.numFans)

toy_story = Movie("Toy Story", "kids")
spongebob = Movie("Spongebob", "children") #further example from pulling from class movie
buzz.film = toy_story #same as 42 this only works because of self.film=none in the first __init__
buzz.film = Movie("Toy Story", "kids") #same as 41
woody.film = toy_story #see line 48
woody.film = Movie("Woody's Wild West", "R")


print(toy_story.title)
print(buzz.film.title)
print()
print(woody.film.title) #This is only possible cause of line 42
print(woody.film.genre) #read it backwards and replace . with "of" example: genre of film of woody