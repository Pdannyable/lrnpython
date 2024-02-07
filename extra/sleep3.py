"""Use of yield (an iterator) to handle large data"""


def main():
    n = int(input("What is n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐏" * i   # this generates a little bit of data at a time


if __name__ == "__main__":
    main()