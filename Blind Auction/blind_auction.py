#blind_auction.py

from art import logo
import os

bids = {}

def get_bids():
    print(logo)
    print('Welcome to the secret auction program.')
    
    more_bids = True
    while more_bids:
        name = input('What is your name?: ')
        bids[name] = int(input("What's your bid? $"))
        
        more_bids = 'yes' == input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')
       
def auction_winner(bidders):
    current_winner = ''
    highest_bid = 0
    
    for name in bidders:
        if bidders[name] > highest_bid:
            highest_bid = bidders[name]
            current_winner = name
    
    print(f'The winner is {current_winner} with a bid of ${bidders[current_winner]}')    

get_bids()
auction_winner(bids)
    
#print(bids)