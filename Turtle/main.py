#Start of working with the Turtle Module which is built upon Tkinter

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")

screen = Screen()
screen.colormode(255)



def draw_square():
    for i in range(4):
        tim.forward(100)
        tim.right(90)

# draw_square()

def draw_dashed_line(distance):
    for i in range(distance):
        tim.forward(10)
        tim.pu()
        tim.forward(10)
        tim.pd()
        tim.forward(10)

# draw_dashed_line(10)

def draw_triangle():
    for i in range(3):
        tim.forward(100)
        tim.right(120)

def draw_pentagon():
    for i in range(5):
        tim.forward(100)
        tim.right(72)

def draw_hexagon():
    for i in range(6):
        tim.forward(100)
        tim.right(360/6)

# draw_triangle()
# draw_square()
# draw_pentagon()
# draw_hexagon()

from random import randint

def draw_shape(num_sides):
    tim.pencolor(randint(1,255),randint(1,255),randint(1,255)) #had to change screen.colormode(255) otherwise this wouldn't work, screen was moved to top of script
    for i in range(num_sides):
        tim.forward(100)
        tim.right(360/num_sides)

draw_shape(3)
draw_shape(4)
draw_shape(5)
draw_shape(6)
draw_shape(7)
draw_shape(8)
draw_shape(9)
draw_shape(10)


# screen = Screen()
screen.exitonclick()