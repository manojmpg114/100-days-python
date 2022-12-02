print('hello'[3])

num_char = len(input('what is your name? '))
str_num_char = str(num_char)
print(f'your name has {num_char} characters')

print('output:' + str_num_char)

import random 

random_integer = random.randint(1,10)

print(random_integer)

#import custom module for use in main programming area 
import my_module

print(my_module.pi) #from other module 

random_float = random.random() 
print(random_float)

random_float_large = random_float * 5 #expands range to 0-5
print(random_float_large)

love_score = random.randint(1,100)
print(f'Your love score is {love_score}')

def my_function():
    print('Hello')
    print('Bye')
    
my_function()
