# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd
from numpy.ma.extras import average

# data = pd.read_csv("weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].tolist()
# print(temp_list)
# print(average(temp_list))
# print(data["temp"].mean())
# print(max(temp_list))
# print(data["temp"].max())
#
#
# # Get data condition
# print(data["condition"])
# print(data.condition)
#
# # Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(f"monday temp in celcius: {monday_temp}")
# print(f"monday temp in fahrenheit: {monday_temp_f}")

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
