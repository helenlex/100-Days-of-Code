""" learning about higher order functions and event listeners """
import turtle as t

andreas = t.Turtle()
SCREEN = t.Screen()

SCREEN.listen()

def move_forwards():
    """ function to move turtle forward 10 spaces """
    andreas.forward(10)

def move_backwards():
    """ function to move turtle backward 10 spaces """
    andreas.backward(10)

def counter_clockwise():
    """ function to move counter_clockwise """
    andreas.left(10)

def clockwise():
    """ function to move clockwise """
    andreas.right(10)

def clear_drawing():
    """ function to move clear the screen """
    andreas.clear()
    andreas.penup()
    andreas.home()
    andreas.pendown()

# note below, we don't add the () next to the function
# () prompts system to trigger function right then and there

# if you are using methods you haven't built yourself, use keyword arguments, as shown below
SCREEN.onkey(key = "w",  fun = move_forwards)
SCREEN.onkey(key = "s",  fun = move_backwards)
SCREEN.onkey(key = "a",  fun = counter_clockwise)
SCREEN.onkey(key = "d",  fun = clockwise)
SCREEN.onkey(key = "c",  fun = clear_drawing)

SCREEN.exitonclick()
