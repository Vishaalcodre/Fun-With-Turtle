from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.usr_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Home = {self.usr_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.usr_score += 1
        self.write(f"Home = {self.usr_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
