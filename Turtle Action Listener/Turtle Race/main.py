from turtle import Turtle, Screen
from random import randint

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()

t1.color("red")
t2.color("blue")
t3.color("green")
t4.color("yellow")
t5.color("purple")



screen = Screen()

screen.setup(width = 500, height = 400) #resize the screen again using keyword arguments since we didn't create this method 
place_your_bet = screen.textinput(title="Place your bets!", prompt= "Which Turtle Will Win? Enter a color: ").lower()

t1.pu()
t2.pu()
t3.pu()
t4.pu()
t5.pu()

t1.setpos(x = -200, y = 20)
t2.setpos(x = -200, y = 10)
t3.setpos(x = -200, y = 0)
t4.setpos(x = -200, y = -10)
t5.setpos(x = -200, y = -20)

t1.pd()
t2.pd()
t3.pd()
t4.pd()
t5.pd()

turtle_distances = [t1.pos()[0], t2.pos()[0], t3.pos()[0], t4.pos()[0], t5.pos()[0]]

# print(turtle_distances)

print(f"You're betting on {place_your_bet} turtle!")

while 200 not in turtle_distances:
    t1.forward(randint(1,10))
    t2.forward(randint(1,10))
    t3.forward(randint(1,10))
    t4.forward(randint(1,10))
    t5.forward(randint(1,10))

    turtle_distances = [t1.pos()[0], t2.pos()[0], t3.pos()[0], t4.pos()[0], t5.pos()[0]]


print(turtle_distances)

if t1.pos()[0] == 200:
    print('Red Turtle Wins')
    if place_your_bet == "red":
        print('You are the winner!')
    else:
        print('Your turtle did not win!')
    
if t2.pos()[0] == 200:
    print('Blue Turtle Wins')
    if place_your_bet == "blue":
        print('You are the winner!')
    else:
        print('Your turtle did not win!')

if t3.pos()[0] == 200:
    print('Green Turtle Wins')
    if place_your_bet == "green":
        print('You are the winner!')
    else:
        print('Your turtle did not win!')

if t4.pos()[0] == 200:
    print('Yellow Turtle Wins')
    if place_your_bet == "yellow":
        print('You are the winner!')
    else:
        print('Your turtle did not win!')

if t5.pos()[0] == 200:
    print('Purple Turtle Wins')
    if place_your_bet == "purple":
        print('You are the winner!')
    else:
        print('Your turtle did not win!')

# def clear(): #Might drop this but need to modify so all turtles go back to their starting position and not just home
#     tim.clear()
#     tim.pu()
#     tim.home()
#     tim.pd()


    
screen.listen()


# screen.onkey(key='space', fun=clear)


screen.exitonclick()