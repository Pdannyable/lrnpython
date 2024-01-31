# Welcome user to Python
print("Welcome to Python")

# Ask user for their name
name = input("What is your name? ")

# Best practice, use of 'f'
print(f"Hello, {name}")

# Greet user, note the inclusion of space after hello
print("Hello, " + name)

# Alternatively, you can output this way. Note the omission of space
print("Hello,",name)

# To demonstrate the effect of default parameters of the function print
# print(*objects, sep=' ', end='\n', file=None, flush=False)
# Alternatively, use end="" to keep output on the same line
print("Hello, ", end="")
print(name)

# Alternatively, demonstrating 'sep' as in separation
# you can override the default space with any character
print("Hello,", name, sep="???")

# To use a quote in a print
print('Hello,', name,'"my friend"')

# Alternatively, you can use \ to include a quote
print("Hello, \"friend\"")