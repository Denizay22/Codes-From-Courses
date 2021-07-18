import time
from turtle import Screen, Turtle

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Tsssss")
screen.tracer(0)  # turn off animations

game = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()
screen.listen()
screen.onkey(snake.go_right, "d")
screen.onkey(snake.go_left, "a")
screen.onkey(snake.go_up, "w")
screen.onkey(snake.go_down, "s")
while game:
    time.sleep(0.05)
    screen.update()
    snake.move_snake()
    if snake.parts[0].distance(food.xcor(), food.ycor()) < 15:
        food.relocate_food()
        scoreboard.update_score()
        snake.add_part()

    if snake.parts[0].xcor() > 290 or snake.parts[0].xcor() < -290 or\
            snake.parts[0].ycor() > 290 or snake.parts[0].ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for i in range(1, len(snake.parts)-1):  # for part in snake.parts[1:]
        if snake.parts[0].distance(snake.parts[i]) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
