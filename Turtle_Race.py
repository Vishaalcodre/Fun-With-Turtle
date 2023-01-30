import random
import turtle
from turtle import Turtle, Screen


screen = Screen()

race_on = False

screen.setup(width=500, height=400)

usr_bet = screen.textinput(title="Place your bet", prompt="Which color turtle will win the race? ")

print(usr_bet)

colors = ["red", "purple", "green", "blue", "brown"]

y_axis = -100

all_turtles = []

for i in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    y_axis += 50
    all_turtles.append(new_turtle)

if usr_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if usr_bet == winner:
                print(f"You Win!, The {winner} won the race!")
            else:
                print(f"You Lose, {winner} won the race.")
            race_on = False
        pace = random.randint(0, 10)
        turtle.forward(pace)

screen.exitonclick()
