from turtle import *
import random

screen = Screen()

colormode(255)

angle = []

speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    colour = (r, g, b)

    return colour


for i in range(0, 360, 10):
    angle.append(i)
    color(random_color())
    setheading(i)
    circle(100)

print(angle)

screen.exitonclick()
