import time
from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1.5
MOVE_INCREMENT = 1.5


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.penup()
        self.setposition(x=300, y=randint(-250, 250))

    def move(self, speed):
        self.setposition(x=self.xcor() - speed, y=self.ycor())


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        for _ in range(0, randint(0, 2)):
            self.cars.append(Car())

    def move_cars(self):
        for car in self.cars:
            car.move(self.speed)

    def detect_collusion(self, player):
        for car in self.cars:
            if car.distance(player) < 25 and player.ycor() > car.ycor() - 20:
                return True
        return False

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
