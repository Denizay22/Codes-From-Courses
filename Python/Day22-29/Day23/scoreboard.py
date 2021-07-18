from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setposition(x=-210, y=260)
        self.level = 1
        self.write(f"Level = {self.level}", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level = {self.level}", align="center", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", align="center", font=FONT)
