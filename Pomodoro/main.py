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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW, highlightthickness=0)


#Canvas Widget - Allows for layering / drawing one on top of another 
canvas = Canvas(width=200, height=224, bg=YELLOW, )
tomato_img = PhotoImage(file="tomato.png") #specific class from the tkinter module that helps pass images, requires the file = file or file path location if not relative dir
canvas.create_image(102, 112, image=tomato_img)
canvas.create_text(102, 130, text="00:00", fill="white", font=((FONT_NAME, 35, "bold")))
canvas.pack()


window.mainloop()