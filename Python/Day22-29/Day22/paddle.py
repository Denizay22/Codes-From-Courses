from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xpos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x=xpos, y=0)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 15)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 15)
