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

# METHOD THREE - pandas! so much more efficient!

import pandas

data = pandas.read_csv(r"weather_data.csv")
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

# row of data with highest temperature
row_high_temp = data[data.temp == data.temp.max()]

monday = data[data.day == "Monday"]
print(type(monday))
