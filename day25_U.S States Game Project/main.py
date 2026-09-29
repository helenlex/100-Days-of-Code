# # METHOD ONE - works but we still have to strip

# with open(r"day25_U.S States Game Project\weather_data.csv") as file:
#     data = file.readlines()

# print(data)

# # METHOD TWO  - works but so many lines just to grab one column

# import csv

# with open(r"day25_U.S States Game Project\weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

# # METHOD THREE - pandas! so much more efficient!

# import pandas

# data = pandas.read_csv(r"day25_U.S States Game Project\weather_data.csv")
# print(data["temp"])

# # Turning data into a dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # Turning a column into a list

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# # Average of a column

# avg_temp = data["temp"].mean()
# print(avg_temp)

# # Max of a column

# max_temp = data["temp"].max()
# print(max_temp)

# # Referring to a column, both are the same
# data.temp # like an attribute of an object
# data["temp"] # like pulling data out of dictionary

# # row of data with highest temperature
# row_high_temp = data[data.temp == data.temp.max()]

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# fahrenheit = (monday_temp * 1.8) + 32
# print(fahrenheit)

# # Creating a dataframe from scratch

# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "grades" : [70, 100, 90]
# }

# data_students = pandas.DataFrame (data_dict)
# data_students.to_csv(r"day25_U.S States Game Project\new_data.csv")

#--------------------------------

# Squirrel Project

import pandas as p

data = p.read_csv(r"day25_U.S States Game Project\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrel_count)
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrel_count)
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrel_count)

data_dict = {
"colours": ["Gray", "Cinnamon", "Black"],
"count": [2473, 392, 103]
}

squirrel_count = p.DataFrame(data_dict)
squirrel_count.to_csv(r"day25_U.S States Game Project\new_data.csv")