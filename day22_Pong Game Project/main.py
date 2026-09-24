from turtle import Screen

from paddle import R_Paddle, L_Paddle

from ball import Ball

import time

# CREATE THE SCREEN
SCREEN = Screen()
SCREEN.setup(width = 800, height = 600)
SCREEN.bgcolor("black")
SCREEN.title("My Pong Game")
SCREEN.tracer(n = 0, delay = 0)

# CREATE A BALL AND MAKE IT MOVE
ball = Ball()

# CREATE AND MOVE A PADDLE
paddle2 = R_Paddle()
SCREEN.listen()
SCREEN.onkeypress(fun = paddle2.move_up, key= "Up")
SCREEN.onkeypress(fun = paddle2.move_down, key= "Down")

# CREATE ANOTHER PADDLE
paddle1 = L_Paddle()
SCREEN.listen()
SCREEN.onkeypress(fun = paddle1.move_up, key= "w")
SCREEN.onkeypress(fun = paddle1.move_down, key= "s")

game_is_on = True

while game_is_on:
    SCREEN.update()
    time.sleep(0.1)
    ball.move()
# DETECT COLLISION WITH WALL AND BOUNCE
    # COLLISION ON TOP AND BOTTOM WALLS ONLY, AND BOUNCE
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

# DETECT COLLISION WITH PADDLE

# DETECT WHEN PADDLE MISSES

# KEEP SCORE
    # IF LEFT AND RIGHT WALLS ARE HIT, POINT TO THE OPPONENT

SCREEN.exitonclick()
