from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.lvl = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.hideturtle()
        self.goto(-270, 250)
        self.write(f"Level: {self.lvl}", align="left", font=FONT)

    def increase_lvl(self):
        self.lvl += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)