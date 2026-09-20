""" Creating the snake class """
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """ Snake class"""
    def __init__(self):
        """ constructor """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """ creating the snake method"""
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """ move method """
        # moving the segments, making each last segment follow the pos of the earlier segment
        for seg_num in range((len(self.segments) - 1), 0, -1):
            # if seg_num is 2, grab the x cor of seg_num 1
            new_x = self.segments[seg_num - 1].xcor()
            # if seg_num is 2, grab the y cor of seg_num 1
            new_y = self.segments[seg_num - 1].ycor()
            # segn_num 2, your new coordinates are the coordinates of seg_num 1
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """ moving up method"""
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        """ moving down method"""
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        """ moving left method"""
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        """ moving right method"""
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
