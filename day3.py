# Day 3 - Treasure Island Project
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("You are broke as hell and need the funds to take Miss Cutie on a date!! Your mission is to find the treasure!")
win = "You WON! yay you get the fundssss! take Miss Cutie on the best date!"

Q1 = input("You stumble across a fork in the road. LEFT or RIGHT? ")
if Q1 == "LEFT":
    Q2 = input("Great choice! You arrive at a wharf. A boat will take 3 hours to arrive. Do you SWIM or WAIT? ")
    if Q2 == "WAIT":
        Q3 = input("Mega slay! You arrive at a house with 3 doors. There is a RED, BLUE and a YELLOW door."
                   "\nBehind one door, lies the funds you need to be rich af. Which one ya opening? ")
        if Q3 == "RED":
            print("So close my love! you were burned by fire :( you died!")
        elif Q3 == "BLUE":
            print("You were eaten by beasts!!!! noooo")
        else:
            print(win)
    else:
        print("NOOOOO you were attacked by catfish!!!!!! you is a dieded one rip")
else:
    print("oh nooo you fell in a hole, damn that sucks! you is a dieded one rip")


