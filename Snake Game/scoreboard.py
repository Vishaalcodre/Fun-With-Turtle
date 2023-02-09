from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.usr_score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.usr_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.usr_score += 1
        self.update_score()

    def reset(self):
        if self.usr_score > self.high_score:
            self.high_score = self.usr_score
            with open("high_score.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.usr_score = 0
        self.update_score()
