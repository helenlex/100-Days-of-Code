""" Creating a snake game """
import time
from turtle import Screen, Turtle

SCREEN = Screen()
SCREEN.setup(width = 600, height = 600)
SCREEN.bgcolor("black")
SCREEN.title("My Snake Game")
SCREEN.tracer(n = 0, delay = 0)


starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    SCREEN.update()
    time.sleep(0.1)
    # moving the segments, making each last segment follow the pos of the earlier segment
    for seg_num in range((len(segments) - 1), 0, -1):
        # if seg_num is 2, grab the x cor of seg_num 1
        new_x = segments[seg_num - 1].xcor()
        # if seg_num is 2, grab the y cor of seg_num 1
        new_y = segments[seg_num - 1].ycor()
        # segn_num 2, your new coordinates are the coordinates of seg_num 1
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

SCREEN.exitonclick()
