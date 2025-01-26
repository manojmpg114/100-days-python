############DEBUGGING#####################
# import tkinter #good if we are only using a few modules within the tkinter class
from tkinter import * #now we don't have to make references as tkinter.Label or tkinter.Button and can just assign Label or Button to our variables

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label Component
my_label = Label(text = "I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"

#Button component

def button_clicked():
    # print("I got clicked")
    my_label.config(text= "Button got clicked")

button = Button(text="CLICK ME", command=button_clicked) #use the command keyword arg and pass a function/method name to call that method on click
button.pack()

#Entry component

window.mainloop()

# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)

#Label

# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left") #the packer has to pack the component to the screen otherwise it would never show up

# my_label["text"] = "New Text" #component can be changed like a dictionary because it works with **kwargs
# my_label.config(text ="New Text") #component also has a function called .config() that accepts the keyword argument and what you want to change it too

# button = tkinter.Button()

# window.mainloop() #always has to be at the end of the program -- keeps the window up and running to allow for tkinter to listen

# """any argument leading with an astrik is the unlimited arguments *args then reference var args or *numbers then reference var numbers"""
# def add(*args): #any argument leading with an astrik is the unlimited arguments *args then reference var args or *numbers then reference var numbers
#     #*args is essentially a tuple if printed
#     print(sum(args))

# add(2,3,4,5,6,9)

# """**kwargs: Many keyworded Arguments"""
# def calculate(n,**kwargs): #**kwargs or double astric means we can have unlimited keywork arguments
#     #**kwargs are essentially a dictionary if printed
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
        
    
# calculate(2, add=3, multiply = 5)

# class Car:
#     def __init__(self, **kw):
#         """accessing the keyword args through dictionary direct access can result in errors if the code we build around expected kwargs doesn't exist as input"""
#         # self.make = kw["make"]
#         # self.model = kw["model"]
#         """using dictionary .get() method to get the dictionary key passed will return none and won't give us an error"""
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.seats = kw.get("seats")

# my_car = Car(make="Nissan", model = "GT-R")

# print(my_car.model)
# print(my_car.make)

# my_car_two = Car(make="Honda")

# print(my_car_two.make)
# print(my_car_two.model)

# """List Comprehension -- new_list = [new_item_code for item in list]"""
# numbers = [1,2,3]
# new_list = [n+1 for n in numbers]

# print(new_list)

# name = "Manoj"
# new_list = [letter for letter in name]
# print(new_list)

# """order of operations // python sequence
#     list
#     range
#     string
#     tuple
# """

# new_list = [n*2 for n in range(1,5)]
# print(new_list)

# """Conditional List Comprehension"""
# """new_list = [new_item for item in list if test]"""
# names = ['alex', 'beth', 'caroline', 'Dave', 'Elanor', 'Freddie']

# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# title_names = [name.title() for name in names]
# print(title_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n*n for n in numbers]
# print(squared_numbers)

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(n) for n in list_of_strings if int(n) % 2 == 0]
# print(numbers)

# with open("./file1.txt") as file1:
#     with open("./file2.txt") as file2:
#         list_one = file1.readlines()
#         list_two = file2.readlines()
        
#         list_one = [int(n.rstrip("\n")) for n in list_one]
#         list_two = [int(n.rstrip("\n")) for n in list_two]
        
#         print(list_one)
#         print(list_two)
        
#         common_elements = [n for n in list_one if n in list_two]
#         print(common_elements)

# """Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test_condition}
# """
# import random
# names = ['alex', 'beth', 'caroline', 'Dave', 'Elanor', 'Freddie']

# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)

# passed_students = {student:student_scores[student] for student in student_scores if student_scores[student] > 60} #can also be done with tuples 
# #for (student, score) in student_scores.items() ^^^^^^
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# word_list = sentence.split(" ")
# print(word_list)

# result = {word:len(word) for word in word_list}
# print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# """To convert temp_c into temp_f use this formula: 

# (temp_c * 9/5) + 32 = temp_f

# """
# weather_f = {key:(weather_c[key] * 9/5) + 32 for key in weather_c}

# print(weather_f)

# with open("my_file.txt", mode="a") as file: #using with keyword and assigning an alias we can auto close the file automatically
#     file.write("\nAdditional Text")
    
# with open("my_file.txt") as file: #using with keyword and assigning an alias we can auto close the file automatically
#     content = file.read()
#     print(content)

# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# #print(pages)
# word_per_page = int(input("Number of words per page: "))
# #print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])