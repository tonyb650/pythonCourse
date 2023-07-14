import random
from classes.deck import Deck
from classes.card import Card

def transfer_deck(from_deck, to_deck):
    for i in range(len(from_deck.cards)):
        to_deck.cards.append(from_deck.cards[len(from_deck.cards)-1])
        from_deck.cards.pop()

def transfer_top_card(from_deck, to_deck):
    to_deck.cards.append(from_deck.cards[len(from_deck.cards)-1])
    from_deck.cards.pop()

def show_player_status(): # print out total cards held by each player to terminal
    print("Player 1 has {} cards".format(len(p1_unused_deck.cards)+len(p1_used_deck.cards)))
    print("Player 2 has {} cards".format(len(p2_unused_deck.cards)+len(p2_used_deck.cards)))

def play_round_war(war_round): # MAIN FUNCTION FOR PLAYING A ROUND, parameter is 0 if not a war round, a number besides 0 means it is a war round
    if (len(p1_unused_deck.cards) >0 or len(p1_used_deck.cards) > 0 ) and (len(p2_unused_deck.cards) >0 or len(p2_used_deck.cards) > 0 ): # check if either player is completely out of cards (game over)
        if len(p1_unused_deck.cards)==0: # Does player 1 need to shuffle?
            print("\nPlayer 1 is all out of shuffled cards...")
            transfer_deck(p1_used_deck,p1_unused_deck) #   move used deck to unused deck
            print("....Shuffling cards")
            random.shuffle(p1_unused_deck.cards)
        if len(p2_unused_deck.cards)==0: # Does player 2 need to shuffle?
            print("\nPlayer 2 is all out of shuffled cards...")
            transfer_deck(p2_used_deck,p2_unused_deck) #   move used deck to unused deck
            print("...Shuffling cards")
            random.shuffle(p2_unused_deck.cards)
        # input("\nPlayer 1, press enter to reveal your top card")
        p1_card_played = p1_unused_deck.cards[len(p1_unused_deck.cards)-1]
        Card.card_info(p1_card_played)
        p1_card_point_val = p1_card_played.point_val
        transfer_top_card(p1_unused_deck, p1_in_play_deck)
        # input("Player 2, press enter to reveal your top card")
        p2_card_played = p2_unused_deck.cards[len(p2_unused_deck.cards)-1]
        Card.card_info(p2_card_played)
        p2_card_point_val = p2_card_played.point_val
        transfer_top_card(p2_unused_deck, p2_in_play_deck)
        if war_round == 0: # 0 means not a 'war' round...decide on a winner
            if p1_card_point_val > p2_card_point_val: #Player 1 wins hand
                print("\n>>>>>Player 1 wins!!!!\n")
                transfer_deck(p1_in_play_deck,p1_used_deck) #   move in_play deck to used deck
                transfer_deck(p2_in_play_deck,p1_used_deck) #   move in_play deck to used deck
                show_player_status()
            elif p1_card_point_val < p2_card_point_val: #Player 2 wins hand
                print("\n>>>>>Player 2 wins!!!!\n") #announce winner
                transfer_deck(p1_in_play_deck,p2_used_deck) #   move in_play deck to used deck
                transfer_deck(p2_in_play_deck,p2_used_deck) #   move in_play deck to used deck
                show_player_status()
            else: # Players tie on this hand
                print("\n* * * * * * * * * * * *\nT H I S   I S   W A R !!!!\n* * * * * * * * * * * *")
                for war_turns in range(3,0,-1):
                    if (len(p1_unused_deck.cards)+len(p1_used_deck.cards) > 1 ) and (len(p2_unused_deck.cards) + len(p2_used_deck.cards) > 1 ): # check if either player is down to their last card
                        play_round_war(war_turns) #Recursive!!!
                    else: # exit this loop early when player is down to their last card
                        play_round_war(0)
        else:
            print("\nWar round...")
    else: # one player is completely out of cards
        input("Game is over")
        return


# ******* INITIALIZE THE DECKS *********
p1_used_deck = Deck("Player 1 Used")
p1_unused_deck = Deck("Player 1 Unused")
p2_used_deck = Deck("Player 2 Used")
p2_unused_deck = Deck("Player 2 Unused")
p1_in_play_deck = Deck("Player 1 In Play")
p2_in_play_deck = Deck("Player 2 In Play")

p1_used_deck.fill_empty_deck() # fill a deck with 52 cards
random.shuffle(p1_used_deck.cards) #shuffle filled deck
for i in range(int(len(p1_used_deck.cards)/2)): # split deck in half
    transfer_top_card(p1_used_deck,p2_used_deck)

want_to_play = input("Do you want to play a game of war? ")
print ("Yes or no, here we go!\n")

# ******** START GAME LOOP *********
rounds = 1
while (len(p1_unused_deck.cards) >0 or len(p1_used_deck.cards) > 0 ) and (len(p2_unused_deck.cards) >0 or len(p2_used_deck.cards) > 0 ) and rounds < 10000:
    continue_game = play_round_war(0) # pass in zero for starting outside of a 'war' round
    rounds += 1 # prevent possibility of endless loop
# *********END GAME LOOP *********

# Display final results of game
if len(p1_unused_deck.cards) == 0 and len(p1_used_deck.cards) == 0:
    print(f"Player Two WINS in {rounds} rounds, sorry Player One")
elif len(p2_unused_deck.cards) == 0 and len(p2_used_deck.cards) == 0:
    print(f"Player One WINS in {rounds} rounds, sorry Player Two")
else:
    print(f"No winner after {rounds} rounds of play.") # should never happen