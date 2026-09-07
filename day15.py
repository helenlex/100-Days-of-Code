# Day 15 - Coffee Machine Project

# menu variable is constant

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# maxed out resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

import sys

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
money = 0

on = True
resource_check_passed = True
transaction_check_passed = True
total = 0

def resource_check(ingredients):
    """checks if current resources are sufficient to make menu item"""
    global resource_check_passed
    for x in ingredients:
        if ingredients[x] > resources[x]:
            resource_check_passed = False
            print(f"Sorry there is not enough {x}.")

def coin_calculation():
    """ calculates total coins inputted """
    global total
    print("Please insert coins.")
    quarters = int(input("how many quarters: "))
    dimes = int(input("how many dimes: "))
    nickles = int(input("how many nickles: "))
    pennies = int(input("how many pennies: "))
    total = ((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))

def transaction():
    """checks that total coins are sufficient to make menu item"""
    global transaction_check_passed
    change = total - MENU[order]["cost"]
    if total < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded")
        transaction_check_passed = False
    elif total > MENU[order]["cost"]:
        print(f"Here is ${change:.2f} dollars in change.")

def make_coffee():
    """ functions that makes the coffee and reduces each resource"""
    global resources
    global money
    if transaction_check_passed:
        resources["water"] -= MENU[order]["ingredients"]["water"]
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
        if order != "espresso":
            resources["milk"] -= MENU[order]["ingredients"]["milk"]
        money += MENU[order]["cost"]
        print (f"Here is your {order}. Enjoy!")

# UI of teh coffee machine
while on == True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # 3. Print report.
    if order == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money:.2f} ")
    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # owners of the machine can turn the machine off
    elif order == "off":
        on = False
        sys.exit()
    # 4. Check resources sufficient?
    main_options = ["espresso", "latte", "cappuccino"]
    if order in main_options:
        resource_check(MENU[order]["ingredients"])
        if resource_check_passed:
        # 5. Process coins.
            coin_calculation()
            # 6. Check transaction successful?
            transaction()
            # 7. Make Coffee.
            make_coffee()

