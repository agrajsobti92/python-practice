# Dictionary Implementation
list = {}

with open("nyc_weather.csv") as file:
    next(file)
    for line in file:
        vals = line.split(',')
        day = vals[0]
        temp = int(vals[1])
        list[day] = temp

print(list['Jan 9'])
print(list['Jan 4'])


# # List implementation
# list = []

# with open("nyc_weather.csv") as file:
#     next(file)
#     for line in file:
#         vals = line.split(',')
#         temp = int(vals[1])
#         list.append(temp)

# avg = sum(list[:7]) / len(list[:7])

# print(avg)
# print(max(list[:10]))
