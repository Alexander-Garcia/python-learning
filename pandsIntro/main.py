import pandas

# data = pandas.read_csv(filepath_or_buffer="weather_data.csv")

# conversions
# temperature_list = data["temp"].to_list()

# Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# TODO: create csv squirrel_count
# TODO: tally squirrels by color from 'Primary Fur Color'
# TODO: create a DF and export it
data = pandas.read_csv(filepath_or_buffer="centralParkSquirrelData.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
