# Day 12 - Number Guessing Project
import art
import random

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# number can be between 1 and 100 inclusive
number = random.randint(1, 100)

def difficulty_level(type_of_difficulty):
    """ accepts the type of difficulty as an input.
    if the difficulty is easy, 10 attempts are allowed.
    if the difficulty is hard, 5 attempts are allowed.
    each attempt will remind the user how many attempts they have remaining.
    the function will also comment on whether the guess is too high/low.
    Guess is revealed whether or not user wins or loses."""
    attempts = ""
    guess = ""
    if type_of_difficulty == "easy":
        attempts = 10
    elif type_of_difficulty == "hard":
        attempts = 5
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Guess is too high")
        elif guess < number:
            print("Guess is too low")
        attempts -= 1
        if attempts == 0:
            print(f"Ah damn! The answer was {number}")
            break
        elif guess == number:
            break
    if guess == number:
        print(f"You got it! The answer was {number}")
    elif attempts == 0 and guess != number:
        print("You've run out of guesses. Refresh the page to run again.")

# running the game
difficulty_level(difficulty)


