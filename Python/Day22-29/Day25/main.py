import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

tempetures = data["temp"].tolist()
avg_temp = sum(tempetures) / len(tempetures)
print(avg_temp)
print(data["temp"].mean())
print(data["temp"].max())  # or you can use data.temp

print(data[data.day == "Monday"])  # to get a specific row
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(int(monday.temp))

# create a dataframe

my_data = {
    "students": ["Deno", "Mezo", "ASD"],
    "scores": [50, 60, 70]
}
data = pandas.DataFrame(my_data)
print(data)
data.to_csv("my_csv.csv")

# ------------------------------------
# ,Fur Color, Count     - Primary Fur Color
# 0, grey, x
# 1, red, y
# 2, black, z

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]),
              len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]),
              len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])]
}

squirrel_color_dataframe = pandas.DataFrame(squirrel_data_dict)
squirrel_color_dataframe.to_csv("squirrel_color_data.csv")
print(squirrel_color_dataframe)
