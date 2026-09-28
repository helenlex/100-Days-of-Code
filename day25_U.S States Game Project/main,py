# METHOD ONE - works but we still have to strip

with open(r"day25_U.S States Game Project\weather_data.csv") as file:
    data = file.readlines()

print(data)

# METHOD TWO  - works but so many lines just to grab one column

import csv

with open(r"day25_U.S States Game Project\weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)

# METHOD THREE - pandas! so much more efficient!

import pandas

data = pandas.read_csv(r"day25_U.S States Game Project\weather_data.csv")
print(data["temp"])
