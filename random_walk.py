import turtle as t
import random

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_c = (r, g, b)

    return random_c


directions = [0, 90, 180, 270]

t.pensize(7)

t.speed(10)

for i in range(100):

    t.color(random_color())
    t.forward(10)
    t.setheading(random.choice(directions))


