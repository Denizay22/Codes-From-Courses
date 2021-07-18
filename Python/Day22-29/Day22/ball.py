from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xdir = 1
        self.ydir = 1
        self.gameSpeed = 0.5

    def move(self):
        self.setposition(x=self.xcor() + (4 * self.xdir), y=self.ycor() + (4 * self.ydir))

    def check_wall_collusion(self, scoreboard):
        if self.ycor() > 280 or self.ycor() < -280:
            self.ydir *= -1
        if self.xcor() > 390:
            self.setposition(0, 0)
            self.xdir *= -1
            scoreboard.updateScore(left=1)

        if self.xcor() < -390:
            self.setposition(0, 0)
            self.xdir *= -1
            scoreboard.updateScore(right=1)

    def check_paddle_collusion(self, left_paddle, right_paddle):
        if (self.xcor() > 330 and self.distance(right_paddle) < 50) or \
                (self.xcor() < -330 and self.distance(left_paddle) < 50):
            self.xdir *= -1
            self.gameSpeed *= 0.5
