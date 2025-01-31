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
reps = 0 #global variable for which timer to reference 
timer = None #needs to be a global variable to use it elsewhere

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer) #cancel the timer we setup previously
    checkmark_label.config(text="")
    timer_label.config(text= "Timer")
    canvas.itemconfig(timer_text, text="00:00")
    #have to reference the global var when we want to make use of it otherwise its inferred local 
    global reps
    reps = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0: #8 timers total or 8 repetitions 
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        
    elif reps %2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

"""Gui needs to continue to listen for events looking for events (Event Driven)"""
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1) #time to wait in milliseconds
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
            checkmark_label.config(text=mark)

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
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0 )
tomato_img = PhotoImage(file="tomato.png") #specific class from the tkinter module that helps pass images, requires the file = file or file path location if not relative dir
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=((FONT_NAME, 35, "bold")))
# canvas.pack()
canvas.grid(column=1, row=1)

# count_down(5)

#Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmark_label.grid(column=1, row=3)

#Buttons
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_timer)

start_button.grid(column=0,row=2)
reset_button.grid(column=2, row=2)


window.mainloop() #Actively listening to see if something happens, prevents the ability to use other loops within the program / gui