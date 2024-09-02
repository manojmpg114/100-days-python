#Start of working with the Turtle Module which is built upon Tkinter

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

def draw_square():
    for i in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)

draw_square()












#screen portions of code have to stay on the bottom so we can do our turtle operations and then view the result / close on click
screen = Screen()
screen.exitonclick()