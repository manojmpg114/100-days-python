#blackjack.py
import os
from art import logo
import random
import sys

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(player_hand):
    player_hand.append(cards[random.randint(0,len(cards)-1)])
    return player_hand

#calculate the value of cards per hand
def calculate_score(player_hand):
    ace_count = 0
    total_count = 0
    for val in player_hand: #Accounts for a differing 11 & 1 to represent Ace, otherwise could use total_count = sum(player_hand) 
        if val == 1 or val == 11:
            ace_count +=1
        else:
            total_count += val
    
    #Alternative way to deal with ace counting  is check the list for any 11s and see the value if we do list.remove(11) and list.append(1)
    #Depending on length of the check could be summed down to 2-3 lines of code making the switch
    if ace_count > 0 and total_count < 21:
        for i in range(ace_count):
            test = total_count + 11
            if test <= 21:
                total_count = test
            else:
                test = total_count + 1
                if test <= 21:
                    total_count = test
                else:
                    return test
    
    
    
  
    
    if ace_count > 0 and total_count >= 21:
        return total_count + ace_count #return ace count as a value of 1, BUST regardless
    
    return total_count

#MAIN with overall logic
if __name__ == '__main__':
    
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    if play_game != 'y':
        sys.exit('Ok we can play another time')
        
    keep_playing = True
    while keep_playing:
            
        
        print(logo)
        
        user = []
        dealer = []
        
        user_total = 0
        dealer_total = 0
        
        for i in range(0,2): #initial 2 cards, we can read our hand, we can't read the dealers and or we can read the dealers first card
            user_total = calculate_score(deal_card(user))
            dealer_total = calculate_score(deal_card(dealer))
        
        
        keep_asking = True
        while keep_asking and user_total <= 21:
            
            print(f'User Total: {user_total}')
            hit = input("Do you want to hit or stay? type 'y' to hit or 'n' to stay: ")
            if hit == 'y':
                print('User Hits')
                user_total = calculate_score(deal_card(user))
            else:
                keep_asking = False
        
        if user_total > 21:
            user_total = calculate_score(deal_card(user))
            print('BUST, YOU LOSE')
        elif user_total == 21:
            user_total = calculate_score(deal_card(user))
            print('YOU WIN')
        elif dealer_total < user_total:
            #Dealers turn
            print('Dealers turn:')
        
            while dealer_total < 17 or dealer_total == user_total or (dealer_total >= 17 and user_total > dealer_total):
                
                print(f'Dealer Total: {dealer_total}')
                print('Dealer Hits')
                dealer_total = calculate_score(deal_card(dealer))
                if dealer_total > user_total and dealer_total <= 21:
                    print(f'Dealer Total: {dealer_total}')
                    print('HOUSE WINS')
                elif dealer_total == user_total:
                    print('DRAW')
                    break
                
                if dealer_total > 21:
                    print(f'Dealer Total: {dealer_total}')
                    print('You Win, Dealer BUST')
            
            if dealer_total == 17 and dealer_total > user_total:
                print(f'Dealer Total: {dealer_total}')
                print('HOUSE WINS')
        else:
            print(f'User Total: {user_total}')
            print(f'Dealer Total: {dealer_total}')
            print('HOUSE WINS')
                    
            
        again = input("Do you want to play another game? 'y' or 'n': ")
        if again == 'y':
            keep_playing = True
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            keep_playing = False
