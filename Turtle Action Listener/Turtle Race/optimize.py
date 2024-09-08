from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [50,30,10,-10,-30]

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x = -200, y = y_positions[turtle_index])



screen.exitonclick()