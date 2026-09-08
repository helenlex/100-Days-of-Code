# Day 2 - Tip Calculator Project

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percentage = (tip / 100) + 1
pay_excl_tip = (bill / people)
pay_incl_tip = round((pay_excl_tip * percentage))

# tip formatted to 2 decimal places
print(f"Each person should pay ${pay_incl_tip:.2f}")

