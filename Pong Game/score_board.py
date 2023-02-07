from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def l_scores(self):
        self.l_score += 1
        self.update_score()

    def r_scores(self):
        self.r_score += 1
        self.update_score()
