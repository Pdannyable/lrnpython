name = input("What's your name? ")

"""
file = open("names.txt", "a")   #"a" appends to overwrite use "w"
file.write(f"{name}\n")         #This introduces a new line at the end of each entry
file.close()
"""

# Lines 4-6 can be written as lines 10-11
with open("names.txt", "a") as file:
    file.write(f"{name}\n")