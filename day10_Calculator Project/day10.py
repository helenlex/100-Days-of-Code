# Day 10 - Calculator Project

def add(n1, n2):
    """adds 2 numbers together"""
    return n1 + n2

def subtract(n1, n2):
    """subtracts 2 numbers together"""
    return n1 - n2

def divide(n1, n2):
    """divides 2 numbers together"""
    return n1 / n2

def multiply(n1, n2):
    """multiplies 2 numbers together"""
    return n1 * n2

operations = {}
operations["+"] = add
operations["-"] = subtract
operations["/"] = divide
operations["*"] = multiply

import art
print(art.logo)

# the flag to continue
cont = "y"

n1 = int(input("Type the first number: "))
while cont == "y":
    chosen_operator = input("Type your mathematical operator of choice (+ , -, /, *): ")
    n2 = int(input("Type the second number: "))
    calculation = operations[chosen_operator](n1, n2)
    print(f"The result is {calculation}")
    cont = input("Would you like to continue working with the previous result? Type 'y' or 'n' ").lower()
    n1 = calculation
    if cont == "n":
        print("\n" * 100)
        n1 = int(input("Type the first number: "))
        cont = "y"
