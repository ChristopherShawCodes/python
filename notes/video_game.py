class VideoGame:
    def __init__(self,name,genre,console_type):
        self.game_name = name
        self.game_genre = genre
        self.game_multiplayer_ability = False
        self.game_player_count = 0
        self.game_console_type = console_type
        self.game_review = ""

    def player_count(self):
        self.game_player_count = input('What is the player count?')
        print(self.game_player_count)

    def multiplayer_ability(self,bool):
        self.game_multiplayer_ability = bool
        print(self.game_multiplayer_ability)

    def review_game(self):
        self.game_review = input('Please provide a review of this game.')
        print(self.game_review)

    def what_genre(self):
        self.game_genre = "action"
        print(self.game_genre)


game_one = VideoGame("Overwatch","Battle Royal","Xbox")
game_one.player_count()
game_one.what_genre()
game_one.multiplayer_ability(True)
game_one.review_game()
