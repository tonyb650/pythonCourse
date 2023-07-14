from . import card

class Deck:
    decks = []
    def __init__( self , deck_name): #create a new deck
        # print(f"Creating empty deck for: {deck_name}")
        self.cards = []
        self.deck_name = deck_name
        Deck.decks.append(self)

    def fill_empty_deck(self):
        # print(f"Filling empty deck for: {self.deck_name}")
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self): # print a deck out to terminal
        print("*** Displaying Deck: {} ***".format(self.deck_name))
        if len(self.cards) != 0:
            for card in self.cards:
                card.card_info()
        else:
            print("  -empty deck-")

    def show_card_count(self): # print a deck card count out to terminal
        print("  *{} deck contains {} cards".format(self.deck_name, len(self.cards)))

    @classmethod
    def show_decks_count(cls):
        print("NEW CARD COUNT")
        for deck in Deck.decks:
            Deck.show_card_count(deck)