import time
from turtle import Screen

from ball import Ball
from paddle import L_Paddle, R_Paddle
from scoreboard import Scoreboard

# CREATE THE SCREEN
SCREEN = Screen()
SCREEN.setup(width = 800, height = 600)
SCREEN.bgcolor("black")
SCREEN.title("My Pong Game")
SCREEN.tracer(n = 0, delay = 0)

# CREATE A BALL AND MAKE IT MOVE
ball = Ball()

# CREATE AND MOVE A PADDLE
r_paddle = R_Paddle()
SCREEN.listen()
SCREEN.onkeypress(fun = r_paddle.move_up, key= "Up")
SCREEN.onkeypress(fun = r_paddle.move_down, key= "Down")

# CREATE ANOTHER PADDLE
l_paddle = L_Paddle()
SCREEN.listen()
SCREEN.onkeypress(fun = l_paddle.move_up, key= "w")
SCREEN.onkeypress(fun = l_paddle.move_down, key= "s")

# CREATE A SCOREBOARD
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    SCREEN.update()
    ball.move()
# DETECT COLLISION WITH WALL AND BOUNCE
    # COLLISION ON TOP AND BOTTOM WALLS ONLY, AND BOUNCE
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # DETECT COLLISION WITH PADDLE
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    
    # DETECT WHEN BALL GOES OUT OF BOUNDS AT EDGE OF THE SCREEN
    # IF OUT OF BOUNDS, BRING BALL BACK TO CENTER OF SCREEN
    # BALL SHOULD MOVE TOWARDS OTHER PLAYER

# DETECT WHEN R PADDLE MISSES
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

# # DETECT WHEN L PADDLE MISSES
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# KEEP SCORE
    # IF LEFT AND RIGHT WALLS ARE HIT, POINT TO THE OPPONENT

SCREEN.exitonclick()
