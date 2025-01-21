import pandas as pd

data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data.columns)

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# print(grey_squirrels_count)

red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(data_dict)

df = pd.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")

# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)

# # import csv

# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     # print(data)
# #     temperatures = []
# #     for row in data:
# #         # print(row)
# #         try:
# #             temperatures.append(int(row[1]))
# #         except:
# #             pass
        
# #     print(temperatures)

# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# # print(data)
# # print(type(data))
# # print(type(data["temp"]))
# # print(data["temp"])

# data_dict = data.to_dict()
# # print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# # average = sum(temp_list) / len(temp_list)
# # print(average)

# print(data["temp"].mean())
# # print(data["temp"].nlargest(n=1))
# print(data["temp"].max())
# # print(type(data["temp"].nlargest(n=1)))

# print(data.columns)
# # print(data.condition)

# #Get Data in Row
# print(data[data["day"] == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 +32
# print(monday_temp_f)

# rnd = pd.DataFrame()
# print(rnd)

# rnd.to_csv("new_data.csv")