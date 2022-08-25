arr = [1, 2, 3, 4, 5, 10]

target = int(input("Enter target to search: "))

d = {}

for index, num in enumerate(arr):
    if target - num not in d:
        d[num] = index
    else:
        print(d[target - num], index)
