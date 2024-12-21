from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600,height=600) #-300 to 300 length and width to make 600x600
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()

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
        print("Food!")
        food.refresh()
       


screen.exitonclick()