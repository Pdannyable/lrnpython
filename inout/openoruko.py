# This program sorts the names saved in alphabetical order.
oruko = []

with open("oruko.txt") as file:
    for line in file:
        oruko.append(line.rstrip())

for name in sorted(oruko):    # setting reverse=True reverses the order
    print(f"hello, {name}")