list = {}

with open("hasmaptutorial.csv") as file:
    for line in file:
        vals = line.split(',')
        day = vals[0]
        price = int(vals[1])
        list[day] = price

print(list)
print(list.get('price', 0))
