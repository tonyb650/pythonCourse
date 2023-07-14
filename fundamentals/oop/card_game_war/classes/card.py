class Card:

    def __init__( self , suit , point_val , string_val ): # create a single card
        
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val

    def card_info(self): #print a single card out to terminal
        print(f"{self.string_val} of {self.suit} : {self.point_val} points")