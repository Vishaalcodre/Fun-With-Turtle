from turtle import *

screen = Screen()

showturtle()


def move_forward():
    forward(10)


def move_backward():
    back(10)


def turn_left():
    n = heading() + 10
    setheading(n)


def turn_right():
    a = heading() - 10
    setheading(a)


def clear_screen():
    penup()
    home()
    clear()
    pendown()


listen()

onkey(move_forward, "w")

onkey(move_backward, "s")

onkey(turn_left, "a")

onkey(turn_right, "d")

onkey(clear_screen, "c")

screen.exitonclick()
