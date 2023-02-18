#number_guessing_game.py
#If hard, 5 guesses
#if easy, 10 guesses

from random import randint

logo = """
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \\
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
"""

def play_game(level):
    attempts = 0
    solution = randint(1,100)
    if level == 'hard':
        attempts = 5
    else:
        attempts = 10
    
    # print(attempts)
    # print(solution)
        
    for i in range(0, attempts+1):
        #print(attempts)
        if attempts > 0:      
            guess = int(input('Make a guess: '))
            if(guess > solution) and attempts != 0:
                print('Too high.\nGuess Again.')
            elif(guess < solution) and attempts != 0:
                print('Too low.\nGuess Again.')
            attempts -= 1

            if attempts != 0:
                print(f'You have {attempts} attempts remaining to guess the number.')

            if guess == solution:
                print(f"That's correct, the number is {solution}")
                break
        else:
                print(f'You lose, the number was {solution}')


print(logo)
print("I'm thinking of a number between 1 and 100.")
play_game(input("Choose a difficulty. Type 'easy' or 'hard: ").lower())


