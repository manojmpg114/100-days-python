#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

l_use = []
for i in range(nr_letters):
    l_use.append(letters[random.randint(0, len(letters)-1)])
    
n_use = []
for i in range(nr_numbers):
    n_use.append(numbers[random.randint(0, len(numbers)-1)])
    
s_use = []
for i in range(nr_symbols):
    s_use.append(symbols[random.randint(0, len(symbols)-1)])

# print(l_use)
# print(n_use)
# print(s_use)

custom_pass = l_use+n_use+s_use
#print(custom_pass)

new_pass = ''
for i in range(len(custom_pass)):
    #print(len(custom_pass)) #confirming we are eliminating elements with each pop
    r_loc = random.randint(0, len(custom_pass)-1)
    new_pass += custom_pass.pop(r_loc)
    

print(f'Here is your new password: {new_pass}')
