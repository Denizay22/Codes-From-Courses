from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=200)
        self.left_score = 0
        self.right_score = 0
        self.write(f"{self.left_score} | {self.right_score}", align="center", font=("Courier", 60, "normal"))

    def updateScore(self, left=0, right=0):
        self.left_score += left
        self.right_score += right
        self.clear()
        self.write(f"{self.left_score} | {self.right_score}", align="center", font=("Courier", 60, "normal"))
