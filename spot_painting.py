# import colorgram
from turtle import *
import random

screen = Screen()

colormode(255)

speed("fastest")

color_list = [(139, 165, 193), (212, 154, 114), (23, 37, 58), (193, 143, 153), (147, 68, 59), (58, 103, 137), (232, 213, 104), (141, 178, 162), (47, 37, 33), (140, 71, 79), (148, 28, 35), (48, 32, 38), (30, 51, 45), (65, 110, 95), (228, 167, 175), (140, 31, 25)]

hideturtle()

penup()

setheading(225)

forward(300)

setheading(0)

for dot_count in range(1, 101):
    showturtle()
    dot(20, random.choice(color_list))
    forward(50)

    if dot_count % 10 == 0:
        hideturtle()
        setheading(90)
        forward(50)
        setheading(180)
        forward(500)
        setheading(0)

screen.exitonclick()

# rgb = []
#
# colors = colorgram.extract('image.jpg', 20)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)
#
# print(rgb)


