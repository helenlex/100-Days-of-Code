import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.listen()
# Moving the turtle

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    if player.ycor() > player.finish_line:
        player.start()
        scoreboard.level_up()
        cars.level_up()

    for x in cars.all_cars:
        if player.distance(x) < 30 :
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
