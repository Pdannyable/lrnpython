# Test if a number is Even or Odd, using the reminder '%' operator
"""
x = int(input("What's x? "))

if x % 2 == 0:      # If x divided by 2 has a reminder of 0
    print("Even")
else:
    print("Odd")
"""


# Alternatively, we can create functions to execute this same task
# and also use boolean expression (True or False)
def main():  # we are creating a main function called main()
    x = int(input("What's x? "))
    if is_even(x):  # we are referencing a function 'is_even()' that will accept an int x.
        print("Even")
    else:
        print("Odd")


"""
def is_even(n):     # we are creating the function is_even() that was referenced in ln 15
    if n % 2 == 0:
        return True
    else:
        return False
"""


# ln 21 - 25 can be condense into ln 28-29
def is_even(n):
    return True if n % 2 == 0 else False


main()  # this line executes the function main()
