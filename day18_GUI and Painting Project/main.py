""" doing challenges and playing around with turtle module """

import random as r
import turtle as t  # using an alias

monty = t.Turtle()
monty.shape("turtle")
monty.color("DeepPink")

# challenge 1 - make a square
for x in range(4):
    monty.forward(100)
    monty.right(90)

# challenge 2 - make a dotted line

# for x in range (10):
    monty.forward(10)
    monty.penup()
    monty.forward(10)
    monty.pendown()

# challenge 3 - drawing different shapes

for x in range (3, 11):
    angle = 360 / x
    monty.pencolor(r.random(),r.random(),r.random())
    for y in range(x):
        monty.setheading(angle)
        monty.forward(100)
        angle += 360 / x


# challenge 4 - random walk
    # get turtle to randomly walk (turn in different directions during its walk)
    # line should be thicker
    # each line should be a random colour

while True:
    monty.width(10)
    to_angle = [0, 90, 180, 270]
    angle = r.choice(to_angle)
    monty.pencolor(r.random(),r.random(),r.random())
    monty.seth(angle)
    monty.speed(10)
    monty.forward(30)

# print to screen
SCREEN = t.Screen()
SCREEN.canvheight(50)
SCREEN.canvwidth(50)
SCREEN.exitonclick()

# remember, modules get installed in your project only, (local environment only)
