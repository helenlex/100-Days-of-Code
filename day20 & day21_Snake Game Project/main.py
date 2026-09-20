""" Creating a snake game """
import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

SCREEN = Screen()
SCREEN.setup(width = 600, height = 600)
SCREEN.bgcolor("black")
SCREEN.title("My Snake Game")
SCREEN.tracer(n = 0, delay = 0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

SCREEN.listen()
SCREEN.onkey(snake.up, "Up")
SCREEN.onkey(snake.down, "Down")
SCREEN.onkey(snake.left, "Left")
SCREEN.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    SCREEN.update()
    time.sleep(0.1)

    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    # if head collides with any segment in the tail, trigger game over
    for segment in snake.segments[1:]: # slice all segments excluding the head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

SCREEN.exitonclick()
