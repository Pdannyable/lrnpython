""" Use of map"""


def main():
    yell("This", "is", "s76d")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
