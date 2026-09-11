""" 
This script is all about learning about OOP with the turtle module
"""

# from turtle import Screen, Turtle

# # classes are in pascal case, Turtle is a class
# tutie_pie = Turtle()

# print(tutie_pie)

# tutie_pie.shape("turtle")
# MY_SCREEN = Screen()

# # screen is an object, canvheight is an attribute
# print(MY_SCREEN.canvheight)

# # below are methods, as I call them with parentheses
# tutie_pie.shape("turtle")
# tutie_pie.color("CornflowerBlue")
# tutie_pie.forward(100)

# # screen is an object, exitonclick is the method
# MY_SCREEN.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
