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
    
# *** CHALLENGE ONE ***
class Player:
    def __init__(self, player): # Constructor method accepting a dictionary as a parameter
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    def __repr__(self): # this was from the solution video. The __repr__ method "overloads" the default system print method for this class. Very cool!
        return "Player: {}, {} y/o, pos: {}, team: {}".format(self.name, self.age, self.position, self.team)

    # BONUS: Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.
    @classmethod
    def get_team(cls, team_list): # Parameter 'team_list' is a list of dictionaries
        new_team_list = [] # start an empty list to store new objects
        for player in team_list: # iterate through dictionaries in passed in list
            new_team_list.append(Player(player)) # append a new object to 'new_team_list' for each dictionary in 'team_list'
        return new_team_list

# *** CHALLENGE TWO ***        
player_kevin = Player(kevin) # create instance of Player from individual dictionaries
player_jason = Player(jason)
player_kyrie = Player(kyrie)
print(player_jason) # Confirm instance is instantiated correctly 

# *** CHALLENGE THREE ***
new_team = [] 
for count in range(len(players)): #loop through each index of 'players' list
    new_team.append(Player(players[count])) #push player object to 'new_team' list
print(new_team[0]) # confirm list is created correctly

# ***  BONUS ***
new_team_2 = Player.get_team(players) #create a list of objects using @classmethod 'get_team'. Should pass in argument that is a list of dictionaries. 
print(new_team_2[1]) # confirm list of objects is created correctly
print(new_team_2)