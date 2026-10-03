import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = r"day25_U.S States Game Project\US State Quiz Game Project\blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# 1. convert the guess to title case
answer_state = screen.textinput(title= "Guess the state", 
                                prompt= "What's another state's name?").title()

file = pd.read_csv(r"day25_U.S States Game Project\US State Quiz Game Project\50_states.csv")

game_over = False
correct_guesses = []

def correct_answer_process(user_input):
    for name in file["state"]:
            # 2. check if the guess if among the 50 states
            if user_input == name and user_input not in correct_guesses:
                # 5. record the correct guesses in a list
                correct_guesses.append(name)
                 # 3. write correct guesses onto the map
                new_turtle = turtle.Turtle()
                new_turtle.penup()
                new_turtle.hideturtle()
                record = file[(file["state"] == name)]
                # item grabs the value only, not the index
                xcor = record["x"].item()
                ycor = record["y"].item()
                new_turtle.goto(xcor, ycor)
                new_turtle.write(name)
                

while not game_over:
    #4. Use a loop to allow the user to keep guessing
        if answer_state == "Exit":
             game_over = True
        
        while answer_state != "Exit":
             correct_answer_process(answer_state)
             
             if len(correct_guesses) == 50:
                game_over = True
             # 6. keep track of the score
             answer_state = screen.textinput(title= f"{len(correct_guesses)}/50 States Correct", 
                                                prompt= "What's another state's name?").title()



#states_to_learn = file[]

screen.mainloop()
