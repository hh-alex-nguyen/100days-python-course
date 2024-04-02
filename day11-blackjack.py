import random

N_RANK = 13
N_SUIT = 4
SUITS = ("\u2665", "\u2666", "\u2663", "\u2660")
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
VALUE = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10, 10)

# create deck
deck = {}
for i in range(52):
    deck[i] = True


def get_card():
    available_card = []
    for key in deck:
        if deck[key]:
            available_card.append(key)
    card = random.choice(available_card)
    deck[card] = False
    return card

def display_card(index):
    r = index //4
    s = index % 4
    return RANKS[r]+SUITS[s]


def init_hand():
    return [get_card(), get_card()]


def score(hand):
    s = 0
    ranks_index = [i//4 for i in hand]
    for index in ranks_index:
        s += VALUE[index]
    return s


playing = True
while playing:
    computer_hand = init_hand()
    player_hand = init_hand()
    print("Computer's hand: ", [display_card(i) for i in computer_hand])
    print("Player's hand: ", [display_card(i) for i in player_hand])
    if score(player_hand) == 21:
        print("Blackjack, Congratulations!")
        playing = False
        break

    if score(computer_hand) == 21:
        print("Computer Blackjack, You lose!")
        playing = False
        break



