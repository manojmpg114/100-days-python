from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600,height=600) #-300 to 300 length and width to make 600x600
screen.bgcolor("black")
screen.title("My Snake Game")

starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []

screen.tracer(0)

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.pu()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)
    
# screen.update

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for seg in segments:
        seg.forward(20)
    





screen.exitonclick()