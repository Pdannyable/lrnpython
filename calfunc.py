def main():     # this defines the main script
    x = int(input("What's x? "))
    print("x squared is", square(x))


# We will use three methods to create & define square function
# Method 1
def square(n):      # This defines the square function we are creating
    return n * n

# Method 2
def square(n):      # This defines the square function we are creating
    return n ** 2

# Method 3
def square(n):      # This defines the square function we are creating
    return pow(n, 2)


main()      # This calls the main 'function' of the script
