# This script demonstrates the use of try and except
# for handling errors
# The introduction of while loop keeps the loop
# until the right input is provided

# Lines 8-16 does same thing as line 19-32
"""
while True:
    try:
        x = int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
"""

def main():
    x = get_int("what's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()