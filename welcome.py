# Demonstration of str (string)
# Ask user for their name
"""
 "name = input(")What is your name? ")

# Remove whitespace from str
name = name.strip()

# Capitalize user's name

#this capitalizes only the first argument
name = name.capitalize()

#this capitalizes all arguments
name = name.title()

# Say welcome to user
print(f"welcome, {name}")
"""

# Lines 3 -17 can be represented in a simpler form as below
# Ask user for their name
name = input("What's your name? ").strip().title()

# Say welcome to user
print(f"Welcome, {name}")

# To split user's mame into first and last name
# and greet by first name
first, last = name.split(" ")
print(f"Welcome, {first}")