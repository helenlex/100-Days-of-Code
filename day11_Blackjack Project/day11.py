# Day 11 - Blackjack Project

import art
import sys
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
def stand_decision_n():
    """If the user decides to stand, program will show the user's final hand,
        and computer will continue to draw cards until its hand is greater than 17.
        Function also determines win and lose conditions"""
    print(f"Your final hand: {user_hand}, final score: {sum(user_hand)}")
    while sum(computer_hand) < 17 and sum(user_hand) < 21:
        computer_hand.extend(random.choices(cards, None, k=1))
    print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
    if sum(user_hand) == 21:
        print("You win with a blackjack!")
    elif sum(user_hand) > 21:
        print("You went bust, you lose!")
    elif sum(computer_hand) > 21:
        print("Computer went bust, you win!")
    elif sum(computer_hand) == sum(user_hand):
        print("You both are tied!")
    elif sum(computer_hand) > sum(user_hand):
        print("You lose!")
    else:
        print("You win!")
def stand_decision_y():
    """If the user decides to hit, user can hit as many times
    until the sum of their hand does not exceed 21."""
    user_hand_check = sum(user_hand)
    while user_hand_check <= 21:
        user_hand.extend(random.choices(cards, None, k=1))
        user_hand_check = sum(user_hand)
        print(f"Your cards: {user_hand}, current score: {sum(user_hand)}")
        print(f"Computer's first card: {computer_hand}")
        if user_hand_check > 21:
            stand_decision_n()
        elif user_hand_check < 21:
            stand_decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()

# If the player does not want to play, exit the program
if start == "n":
    sys.exit(0)

# If the player wants to play the program:
elif start == "y":
    print(art.logo)
    user_hand = random.choices(cards, None, k = 2)
    computer_hand = random.choices(cards, None, k = 1)
    highest_score = 21
    print(f"Your cards: {user_hand}, current score: {sum(user_hand)}")
    print(f"Computer's first card: {computer_hand}")
# Winning condition for the user:
    if sum(user_hand) == 21:
        print("You win with a blackjack!")
# User can stand or hit
    elif sum(user_hand) < 21:
        stand_decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if stand_decision == "n" or sum(user_hand) > 21:
            stand_decision_n()
        elif stand_decision == "y":
            stand_decision_y()







