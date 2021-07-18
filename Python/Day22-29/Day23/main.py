import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(key="w", fun=player.move_up)

game_is_on = True
iteration = 1
while game_is_on:
    iteration += 1
    time.sleep(0.01)
    if iteration % 15 == 0:
        car_manager.generate_cars()
        iteration = 1

    car_manager.move_cars()

    if car_manager.detect_collusion(player):
        scoreboard.game_over()
        game_is_on = False

    if player.next_level_detect():
        scoreboard.next_level()
        car_manager.increase_speed()
        player.setposition(STARTING_POSITION)
    screen.update()


screen.exitonclick()
