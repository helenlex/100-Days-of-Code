from turtle import Turtle

WIDTH = 1
HEIGHT = 1
BALL_COR = (300,300)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(WIDTH, HEIGHT)
        self.penup()

    def ball_move(self):
        pass
