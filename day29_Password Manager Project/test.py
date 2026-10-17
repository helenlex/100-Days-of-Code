import json

with open(r"day29_Password Manager Project\data.json", "r") as file:
    data = json.load(file)

print(data["amazon"])