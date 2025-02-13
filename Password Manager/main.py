from tkinter import * #imports all the classes constants
from tkinter import messagebox #have to import separately because its a different module of code
from random import choice, randint, shuffle
#could pip install pyperclip and then import pyperclip to allow us to copy and paste a generated password but we will avoid that here
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    
    password_entry.delete(0, END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")
    # nr_letters= int(input("How many letters would you like in your password?\n")) 
    # nr_symbols = int(input(f"How many symbols would you like?\n"))
    # nr_numbers = int(input(f"How many numbers would you like?\n"))

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91


    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    l_use = [choice(letters) for i in range(randint(2,10))]
    # for i in range(nr_letters):
    #     l_use.append(letters[random.choice(0, len(letters)-1)])


        
    n_use = [choice(numbers) for i in range(randint(2,10))]
    # for i in range(nr_numbers):
    #     n_use.append(numbers[random.choice(0, len(numbers)-1)])
        
    s_use = [choice(symbols) for i in range(randint(2,10))]
    # for i in range(nr_symbols):
    #     s_use.append(symbols[random.choice(0, len(symbols)-1)])

    # print(l_use)
    # print(n_use)
    # print(s_use)

    custom_pass = l_use+n_use+s_use
    #print(custom_pass)

    new_pass = ''

    # print(f'Here is your new password: {new_pass}')

    #alternatively we can also just run the random shuffle method on our custom_pass list 
    custom_pass = l_use+n_use+s_use
    shuffle(custom_pass)
    #print(custom_pass)
    new_pass = ''.join(custom_pass)

    # print(f'Here is your new password: {new_pass}')
    password_entry.insert(0, new_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:    
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it ok to save?")
        
        
        if is_ok:    
            
            with open("data.txt", 'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk() #200x200 with 20 padding
window.title("Password Manager")
window.config(padx=50, pady= 50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo_img)

# canvas.pack()
canvas.grid(column=1,row=0)

"""with some widgets needing more spaces than others use 
the columnspan keyword attribute within the grid method"""

website_label = Label(text="Website:") #column 0
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:") #column 0
username_label.grid(column=0, row=2)

password_label = Label(text="Password:") #column 0
password_label.grid(column=0, row=3)

gen_password_button = Button(text="Generate Password", command=generate_password) #column 2
gen_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command = save) #column 1 but columnspan = 2 ; width 36
add_button.grid(column=1, row=4, columnspan= 2, sticky="ew")

website_entry = Entry(width=35) #column 1 but columnspan = 2 ; width 35
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan= 2, sticky="ew")

username_entry = Entry(width=35) #column 1 but columnspan = 2 ; width 35
username_entry.insert(0, 'generic@gmail.com')
username_entry.grid(column=1, row=2, columnspan= 2, sticky="ew")

password_entry = Entry(width=21) #column 1 ; width 21
password_entry.grid(column=1, row=3, sticky="ew")

window.mainloop() 
