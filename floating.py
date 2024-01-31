# Use of Floating point
x = float(input("What's x? "))
y = float(input("What's y? "))

h = (x + y)
z = round(x + y)
print("The sum of x and y is", h, "rounded to", z)
print(f"{z:,}")

# Division
k = x/y
print(k)

# To round the result to 2 decimal places
k = round(x/y, 2)
print(k)

# Alternative way of rounding result to 2 decimal places
print(f"{k:.2f}")