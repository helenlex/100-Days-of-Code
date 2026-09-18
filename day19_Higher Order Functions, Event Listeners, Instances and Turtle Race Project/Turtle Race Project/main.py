""" building a turtle race """
import turtle as t

SCREEN = t.Screen()
SCREEN.setup(width = 500, height= 400)
user_choice = SCREEN.textinput(title = "Turtle Race", prompt = "Choose the colour of your turtle: ")
colours = ["red", "blue", "green", "orange", "purple", "yellow"]
names = ["andreas", "tim", "harry", "jenny", "helena", "jess"]
y_axis = [-100, -50, 0, 50, 100, 150]

#print(andreas.pos())

def create_turtle():
    """ creates a turtle duplicate """
    new_turtle = t.Turtle(shape= "turtle")
    new_turtle.penup()
    return new_turtle


for index in range(6):
    names[index] = create_turtle()
    names[index].color(colours[index])
    names[index].goto(x= -230, y= y_axis[index])


SCREEN.exitonclick()
