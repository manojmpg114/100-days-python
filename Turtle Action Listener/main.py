from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
#Passing the function as input into another funciton is by passing just its name 
screen.onkey(key="space", fun=move_forwards) #We just used a function as an Input by passing its name without the paraenthesis 
screen.exitonclick()

