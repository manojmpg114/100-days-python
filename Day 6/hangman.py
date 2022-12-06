"""
The Game hangman

"""
#hangman.py

#Either ask for a word to guess or generate a word from some collection and present it to the end user
#Display the art + the blank spaces of characters to find matching word length
#input a character for guesses 
#store guesses in a list
#if character in word, display the character in all blanks where character matches location 
#if character not in word, update hang man art 
#maybe display previous guesses list 
#if art completes player loses
#if word guessed player wins (check if all the blanks are full)

#if word is not guessed and player didn't use all guesses, go back to asking for another guess and repeat the cycle 

import random

word_list = ['dive', 'tie', 'doll', 'convenience', 'survey', 'inflation'] #random word list
chosen_word = word_list[random.randint(0, len(word_list)-1)].lower() #randomly selected word from list


fill_chosen_word = '_'*len(chosen_word) #create blanks for the chosen word 

print(chosen_word)
print(fill_chosen_word) #display blanks matching chosen_word length

guess = input('What letter is your guess? ').lower()

if guess in chosen_word:
    counter = 0
    for char in chosen_word:
        if guess == char:
            update_word = list(fill_chosen_word) #create list of the fill for editing, strings are immutable
            update_word[counter] = char #change the string at location counter with the character
            fill_chosen_word = ''.join(update_word) #create a new string with the updated word including any remaining blanks
        counter +=1 #increment counter used for list location 
        
else:
    #some code to draw the hangman, which later needs to be looped while the hangman isn't killed or the solution isn't solved
    pass


print(fill_chosen_word)