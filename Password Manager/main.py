from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk() #200x200 with 20 padding
window.title("Password Manager")
window.config(padx=20, pady= 20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo_img)

canvas.pack()

"""with some widgets needing more spaces than others use 
the columnspan keyword attribute within the grid method"""

website_label = Label() #column 0
username_label = Label() #column 0
password_label = Label() #column 0

gen_password_button = Button() #column 2
add_button = Button() #column 1 but columnspan = 2 ; width 36

website_entry = Entry() #column 1 but columnspan = 2 ; width 35
username_entry = Entry() #column 1 but columnspan = 2 ; width 35
password_entry = Entry() #column 1 ; width 21

window.mainloop() 
