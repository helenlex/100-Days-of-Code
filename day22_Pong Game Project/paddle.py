from turtle import Turtle

MOVE_DISTANCE = 20
R_PADDLE_COR = (350, 0)
L_PADDLE_COR = (-350, 0)

class R_Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(R_PADDLE_COR)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

class L_Paddle(R_Paddle):
    def __init__(self):
        super().__init__()
        self.goto(L_PADDLE_COR)
