from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def clear(): #Might drop this but need to modify so all turtles go back to their starting position and not just home
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()
    
screen.listen()


screen.onkey(key='space', fun=clear)


screen.exitonclick()