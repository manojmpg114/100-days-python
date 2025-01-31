"""
Pomodoro Technique:
Work Timer: 25min
Break Timer: 5min

Work Timer: 25min
Break Timer: 5min

Work Timer: 25min
Break Timer: 5min

Work Timer: 25min
Break Timer: 20min

"""
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

"""Gui needs to continue to listen for events looking for events (Event Driven)"""
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1) #time to wait in milliseconds

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW, highlightthickness=0)


# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)
    
# window.after(1000, say_something, 3, 5, 8) #time to wait in milliseconds

#Canvas Widget - Allows for layering / drawing one on top of another 
canvas = Canvas(width=200, height=224, bg=YELLOW, )
tomato_img = PhotoImage(file="tomato.png") #specific class from the tkinter module that helps pass images, requires the file = file or file path location if not relative dir
canvas.create_image(102, 112, image=tomato_img)

timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=((FONT_NAME, 35, "bold")))
# canvas.pack()
canvas.grid(column=1, row=1)

# count_down(5)

#Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

checkmark_label = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmark_label.grid(column=1, row=3)

#Buttons
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset")

start_button.grid(column=0,row=2)
reset_button.grid(column=2, row=2)


window.mainloop() #Actively listening to see if something happens, prevents the ability to use other loops within the program / gui