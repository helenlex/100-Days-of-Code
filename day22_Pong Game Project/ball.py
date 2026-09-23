from turtle import Turtle

WIDTH = 1
HEIGHT = 1
BALL_COR = (380,280)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(WIDTH, HEIGHT)
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def bounce(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() - 20
        self.goto(new_x, new_y)
