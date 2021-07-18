from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    parts = []

    def __init__(self):
        self.snake_create()

    def snake_create(self):
        for i in range(3):
            self.parts.append(Turtle("square"))
            self.parts[i].color("white")
            self.parts[i].penup()
            self.parts[i].goto(x=i * -20, y=0)

    def move_snake(self):
        for i in range(len(self.parts) - 1, 0, -1):
            self.parts[i].setposition(self.parts[i - 1].xcor(), self.parts[i - 1].ycor())

        self.parts[0].forward(MOVE_DISTANCE)

    def add_part(self):
        self.parts.append(Turtle("square"))
        self.parts[-1].color("white")
        self.parts[-1].penup()

    def go_up(self):
        if self.parts[0].heading() != 270:
            self.parts[0].setheading(90)

    def go_down(self):
        if self.parts[0].heading() != 90:
            self.parts[0].setheading(270)

    def go_left(self):
        if self.parts[0].heading() != 0:
            self.parts[0].setheading(180)

    def go_right(self):
        if self.parts[0].heading() != 180:
            self.parts[0].setheading(0)

    def reset(self):
        for part in self.parts:
            part.setposition(1000, 1000)
        self.parts.clear()
        self.snake_create()
