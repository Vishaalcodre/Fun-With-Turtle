import random
import turtle
from turtle import Turtle, Screen


screen = Screen()

race_on = False

screen.setup(width=500, height=400)

usr_bet1 = screen.textinput(title="Place your bet", prompt="Which color turtle will win the race? ")
usr_bet2 = screen.textinput(title="Place your bet", prompt="Which color turtle will win the race? ")

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

if usr_bet1 and usr_bet2:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if usr_bet1 == winner:
                print(f"Player 1 Win!, The {winner} won the race!")
            elif usr_bet2 == winner:
                print(f"Player 2 Win!, The {winner} won the race!")
            else:
                print(f"You guys Lose, {winner} won the race.")
            race_on = False
        pace = random.randint(0, 10)
        turtle.forward(pace)

screen.exitonclick()
