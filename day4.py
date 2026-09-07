# Day 4 - Rock Paper Scissors

import random

# ascii art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

prompt = "What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "
computer = random.randint(0, 2)
win = "YOU WIN"
lose = "YOU LOSE"
tie = "GO AGAIN"
game_images = [rock, paper, scissors]

user = int(input(prompt))

# whatever the computer generates, show the applicable ascii art
if computer < 3:
    print(game_images[computer])
    print("Computer chose")

# whatever the user selects, show the applicable ascii art
if user > 0 and user < 3:
    print(game_images[user])
    
# if computer chooses rock and user chooses paper, user wins
if computer == 0 and user == 1:
    print(win)
# if computer chooses paper and user chooses scissors, user wins
elif computer == 1 and user == 2:
    print(win)
# if computer chooses scissors and user chooses rock, user wins
elif computer == 2 and user == 0:
    print(win)
# if computer and user's choice matches, it's a tie
elif computer == user:
    print(tie)
# else, the computer wins by default
else:
    print(lose)
