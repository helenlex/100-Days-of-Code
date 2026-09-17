"""using colorgram to create a painting"""
# import colorgram as c

# image = r"C:\GitHub Repos\100-Days-of-Code\day18_GUI and Painting Project\Hirst Painting Project\image.png"

# colours = c.extract(image, 10)

# colours_tuple = []

# for colour in colours:
#     rgb = colour.rgb
#     colours_tuple.append (tuple(rgb))

# print(colours_tuple)

# removed a few colours that were white

import random as r
import turtle as t

SCREEN = t.Screen()
SCREEN.colormode(255)

colour_list = [
    (241, 117, 34),
    (240, 78, 93),
    (163, 111, 8),
    (242, 232, 238),
    (130, 214, 207),
    (213, 152, 161),
    (167, 45, 136),
    (85, 183, 4),
]

monty = t.Turtle()
monty.hideturtle()
# repositioning monty so we get the art centred
monty.seth(270)
monty.penup()
monty.forward(100)
monty.seth(0)
monty.pendown()

for y in range(10):  # rows
    for x in range(10):  # dots per row
        monty.speed(10)
        tup = r.choice(colour_list)
        monty.pencolor(tup)
        monty.dot(20)
        monty.penup()
        monty.forward(50)
    monty.backward(500) # starting a new row
    monty.seth(90)
    monty.forward(50)
    monty.seth(0)

SCREEN.exitonclick()
