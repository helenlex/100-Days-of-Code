# Day 14 - Higher or Lower Project

import art
import game_data
import random

data = game_data.data
game_over = False
score = 0

def determine_winner(dict1, dict2):
    """Determines whether A or B's follower account is higher, then returns the string A or B"""
    if dict1["follower_count"] > dict2["follower_count"]:
        return "A"
    else:
        return "B"

def main_display():
    """displays the A and B statements"""
    print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}.")
    print(art.vs)
    print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]}.")

# When the game starts
while game_over == False:
    A = random.choice(data)
    B = random.choice(data)
    if B == A:
        B = random.choice(data)
    print(art.logo)
    main_display()
    winner = determine_winner(A, B)
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    # When the game is continuing
    while winner == guess:
        print("\n" * 100)
        score += 1
        if guess == "A":
            B = random.choice(data)
            while B == A:
                B = random.choice(data)
        elif guess == "B":
            A = B
            B = random.choice(data)
            while B == A:
                B = random.choice(data)
        print(art.logo)
        print(f"You're right! Current score: {score}")
        main_display()
        winner = determine_winner(A, B)
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if winner != guess:
        game_over = True

#If the game is over
if game_over == True:
    print("\n" * 100)
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")
