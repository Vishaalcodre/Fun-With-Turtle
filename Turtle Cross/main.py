import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Score()
screen.listen()

screen.onkey(player.go_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    if player.ycor() > 280:
        player.reset_pos()
        score.increase_lvl()
        car.car_speed += car.increment

    for new_car in car.cars:
        if new_car.distance(player) < 21:
            score.game_over()
            game_on = False


screen.exitonclick()
