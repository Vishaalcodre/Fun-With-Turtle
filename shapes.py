from turtle import *
import random

screen = Screen()

colors = ["royalblue", "turquoise", "dimgray", "mediumseagreen", "tomato",
          "darkorange", "deeppink", "mediumpurple", "seashell", "yellow"]


def draw_shape(no_of_sides):
    angle = 360/no_of_sides

    for i in range(no_of_sides):
        forward(100)

        right(angle)


for n in range(3, 11):
    color(random.choice(colors))
    draw_shape(n)

screen.exitonclick()