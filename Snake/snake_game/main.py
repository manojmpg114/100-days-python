from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600) #-300 to 300 length and width to make 600x600
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


# screen.update

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    #detect collisions using turtle method distance
    if snake.head.distance(food) < 15:
        # print("Food!")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    #detect collisions with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
    
    #detect collision with tail
    #if head collides with any segment in the tail trigger game over
    # for segment in snake.segments[1:]: #slice to ignore head
    #     if snake.head.distance(segment) < 10:
    #         # game_is_on = False
    #         # scoreboard.game_over()
    #         scoreboard.reset()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset() 
            snake.reset()


screen.exitonclick()