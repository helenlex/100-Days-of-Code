import turtle as t # using an alias
import random as r

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

# print to screen
screen = t.Screen()
screen.exitonclick()

# remember, modules get installed in your project only, (local environment only)

