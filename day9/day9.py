# Day 9 - Blind Auction Project

# TODO-1: Ask the user for input
import art
print(art.logo)
dictionary = {}
new_bids = "yes"
while new_bids == "yes":
    name = input("What is your name? ")
    price = int(input("What is your bid?: $ "))
# TODO-2: Save data into dictionary {name: price}
    dictionary[name] = price
# TODO-3: Whether if new bids need to be added
    new_bids = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    print("\n" * 100)
# TODO-4: Compare bids in dictionary
max_price = max(dictionary.values())
winner = ""
for name in dictionary:
    if dictionary[name] == max_price:
        winner += name

if new_bids == "no":
    print(f"The winner is {winner} with a bid of ${max_price}")



