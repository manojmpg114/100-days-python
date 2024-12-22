from turtle import Screen
import time

screen = Screen()
screen.setup(width=800,height=600) #height -300,300 ; width -400,400
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0) #animation delay settings


screen.listen() #have to be ready to move user-paddle

game_is_on = True

while game_is_on:
    screen.update()
    
screen.exitonclick()