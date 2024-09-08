from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
#Passing the function as input into another funciton is by passing just its name 
#This is what is called a "Higher Order Function" in Python using one function to work with it inside the body of another function
screen.onkey(key="space", fun=move_forwards) #We just used a function as an Input by passing its name without the paraenthesis 
#When working with methods we did not create ourselves, its recommended to work with keyword arguments and not positional arguments for defined meaning
screen.exitonclick()

