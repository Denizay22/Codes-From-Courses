from turtle import Screen

from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PingPong")
screen.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
game = True
while game:
    time.sleep(0.001)
    ball.move()
    ball.check_wall_collusion(scoreboard)
    ball.check_paddle_collusion(left_paddle, right_paddle)
    screen.update()

screen.exitonclick()
