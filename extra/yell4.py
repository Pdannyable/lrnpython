""" Use of list comprehension"""


def main():
    yell("This", "is", "s76d")


def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
