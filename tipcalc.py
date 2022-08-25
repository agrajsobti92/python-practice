bill = float(input("Total bill: $"))
people = int(input("Number of people: "))
perc = int(input("Bill percentage. 10, 12, or 18? "))

calc = bill * (1 + (perc / 100)) / people

print("Each person should pay {:.1f}".format(calc))
