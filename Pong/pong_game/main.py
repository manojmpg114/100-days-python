from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800,height=600) #height -300,300 ; width -400,400
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0) #animation delay settings

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()


screen.listen() #have to be ready to move user-paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    
    screen.update()
    ball.move()
    
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce hitting top or bottom walls 
        ball.bounce_y()
    
    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    
    
screen.exitonclick()