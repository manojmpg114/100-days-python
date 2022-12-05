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

#Hurdle 4 code switching devices 

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    count = 0
    while wall_on_right():
        move()
        count +=1
    turn_right()
    move()
    turn_right()
    for i in range(count):
        move()
    turn_left()
    
while not at_goal(): #version 2 dynamic
    if not is_facing_north():
        while not wall_in_front():
            move()
        if wall_in_front():
            jump()
    if at_goal():
        break
        

"""
#Final Project: Escaping the Maze

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
wall_front = False
wall_right = False
while not at_goal():
    wall_front = wall_in_front()
    wall_right = wall_on_right()
    if wall_front and wall_right:
        turn_left()
    elif not wall_front and wall_right:
        move()
    elif not wall_front and not wall_right:
        move()
    elif not wall_right:
        turn_right()
"""
