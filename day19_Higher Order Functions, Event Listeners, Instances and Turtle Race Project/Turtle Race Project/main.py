""" building a turtle race """
import random as r
import turtle as t

is_race_on = False

SCREEN = t.Screen()
SCREEN.setup(width = 500, height= 400)
user_choice = SCREEN.textinput(title = "Turtle Race", prompt = "Choose the colour of your turtle: ")
colours = ["red", "blue", "green", "orange", "purple", "yellow"]
names = ["andreas", "tim", "harry", "jenny", "helena", "jess"]
y_axis = [-100, -50, 0, 50, 100, 150]

#print(andreas.pos())

all_turtles = []

def create_turtle():
    """ creates a turtle duplicate """
    turtle_dup = t.Turtle(shape= "turtle")
    turtle_dup.penup()
    return turtle_dup

for turtle_index in range(6):
    new_turtle = create_turtle()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x= -230, y = y_axis[turtle_index])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won, the {winning_color} turtle is the winner!")
            elif winning_color != user_choice:
                print(f"You've lost, the {winning_color} turtle is the winner!")
            else:
                print("It's a tie!")
        rand_distance = r.randint(0,10)
        turtle.forward(rand_distance)

SCREEN.exitonclick()
