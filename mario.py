# Using Python to create "mario" blocks
def main():
    print_square(3)


"""
def print_square(size):

#for each row in square
    for i in range(size):

        #for each brick in row
        for j in range(size):

            #Print brick
            print("#", end="")

        print()
"""


# Alternatively, lines 5-18 can be achieved by
# lines 22-27

def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()
