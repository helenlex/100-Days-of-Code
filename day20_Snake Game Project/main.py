""" Creating a snake game """
import time
from turtle import Screen

from snake import Snake

SCREEN = Screen()
SCREEN.setup(width = 600, height = 600)
SCREEN.bgcolor("black")
SCREEN.title("My Snake Game")
SCREEN.tracer(n = 0, delay = 0)

snake = Snake()

SCREEN.listen()
SCREEN.onkey(snake.up, "Up")
SCREEN.onkey(snake.down, "Down")
SCREEN.onkey(snake.left, "Left")
SCREEN.onkey(snake.right, "Right")

GAME_IS_ON = True

while GAME_IS_ON:
    SCREEN.update()
    time.sleep(0.1)

    snake.move()

SCREEN.exitonclick()
