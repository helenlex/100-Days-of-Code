"""creating the food class"""

import random as r
from turtle import Turtle


class Food(Turtle):
    """creating the food class, inherit from Turtle class"""
    # Constructor
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """ food teleports to a new location """
        random_x = r.randint(-270, 270)
        random_y = r.randint(-270, 270)
        self.goto(random_x, random_y)
