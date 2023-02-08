from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.increment = MOVE_INCREMENT

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def create_car(self):
        random_chance = random.randint(1, 10)
        if random_chance == 5:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            y_pos = random.randint(-250, 250)
            car.goto(300, y_pos)
            self.cars.append(car)
