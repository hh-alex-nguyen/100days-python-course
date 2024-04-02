import os

bids = {}
in_bidding = True


def winner_bidder(bids_list):
    winner = ''
    max = -1
    for key in bids_list:
        value = bids_list[key]
        if value > max:
            max = value
            winner = key
    return (winner, max)


while in_bidding:
    name = input("What is your name? ")
    price = float(input("What is your price: "))
    bids[name] = price
    room_call = input("Are there any other bidder? Type 'yes' or 'no': ")
    if room_call == 'no':
        in_bidding = False

winner_info = winner_bidder(bids)
print(f"The winner is {winner_info[0]} with price of {winner_info[1]}.")