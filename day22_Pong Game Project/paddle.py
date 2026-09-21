from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle:
    def __init__(self):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x = 350, y = 0)

    def move_up(self):
        new_y = self.paddle.ycor() + MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y)

    def move_down(self):
        new_y = self.paddle.ycor() - MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y)

    def move_left(self):
        new_x = self.paddle.xcor() - MOVE_DISTANCE
        self.paddle.goto(new_x, self.paddle.ycor())

    def move_right(self):
        new_x = self.paddle.xcor() + MOVE_DISTANCE
        self.paddle.goto(new_x, self.paddle.ycor())
