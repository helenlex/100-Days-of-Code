from turtle import Screen

from paddle import Paddle

# CREATE THE SCREEN
SCREEN = Screen()
SCREEN.setup(width = 800, height = 600)
SCREEN.bgcolor("black")
SCREEN.title("My Pong Game")
SCREEN.tracer(n = 0, delay = 0)

# CREATE AND MOVE A PADDLE
paddle = Paddle()
SCREEN.listen()
SCREEN.onkeypress(fun = paddle.move_up, key= "Up")
SCREEN.onkeypress(fun = paddle.move_down, key= "Down")
SCREEN.onkeypress(fun = paddle.move_left, key= "Left")
SCREEN.onkeypress(fun = paddle.move_right, key= "Right")

game_is_on = True

while game_is_on:
    SCREEN.update()   
    
# CREATE ANOTHER PADDLE

# CREATE A BALL AND MAKE IT MOVE

# DETECT COLLISION WITH WALL AND BOUNCE

# DETECT COLLISION WITH PADDLE

# DETECT WHEN PADDLE MISSES 


# KEEP SCORE

SCREEN.exitonclick()
