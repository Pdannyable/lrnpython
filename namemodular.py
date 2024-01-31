import sys

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# Perform actual task
print("Hello, my mane is", sys.argv[1])