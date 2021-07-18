import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.3, 0.3)
        self.color("red")
        self.speed("fastest")
        self.relocate_food()

    def relocate_food(self):
        self.setposition(random.randint(-290, 290), random.randint(-290, 290))
