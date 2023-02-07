from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Score
import time

screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)

screen.bgcolor("black")

screen.title("Pong")

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = Score()
screen.listen()

screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #  Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with Paddle
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when paddle misses the ball
    if ball.xcor() > 390:
        ball.reset_position()
        score.l_scores()
    if ball.xcor() < -390:
        ball.reset_position()
        score.r_scores()

screen.exitonclick()
