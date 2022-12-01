#rps.py
""" Rock Paper Scissors """

import random

#ascii art 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_hand = int(input('Which option will you go for? Type 0 for Rock, 1 for Paper, and 2 for Scissors. '))
computer_hand = random.randint(0,3)

if player_hand == 0:
    print('Player:')
    print(rock)
    if computer_hand == 0:
        print('Computer:')
        print(rock)
        print('TIE, no winner')
    elif computer_hand == 1:
        print('Computer:')
        print(paper)
        print('Computer Wins!')
    else:
        print('Computer:')
        print(scissors)
        print('Player Wins!')
elif player_hand == 1:
    print('Player:')
    print(paper)
    if computer_hand == 0:
        print('Computer:')
        print(rock)
        print('Player Wins!')
    elif computer_hand == 1:
        print('Computer:')
        print(paper)
        print('TIE, no winner')
    else:
        print('Computer:')
        print(scissors)
        print('Computer Wins!')
elif player_hand == 2:
    print('Player:')
    print(scissors)
    if computer_hand == 0:
        print('Computer:')
        print(rock)
        print('Computer Wins!')
    elif computer_hand == 1:
        print('Computer:')
        print(paper)
        print('Player Wins!')
    else:
        print('Computer:')
        print(scissors)
        print('TIE, no winner')