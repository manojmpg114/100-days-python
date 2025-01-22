import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
# screen.bgpic("./blank_states_img.gif")
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")
# print(data)

all_states = data.state.to_list()

def get_mouse_click_coor(x,y): #method to feed into action listener so it can get our x and y coor when clicking
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop() #Alternative to the exitonclick() that way we aren't closing on click and keeps the window open 

# screen.exitonclick()
guessed_states = []

answer_state = screen.textinput(title=f"{len(guessed_states)}/ 50 States Correct", prompt="What's another state's name?").title()
print(answer_state)

while len(guessed_states) < 50:
    guessed_states.append(answer_state)
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        
        t.write(state_data.state.item())