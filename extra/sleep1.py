def main():
    n = int(input("What is n? "))
    for i in range(n):
        print(sheep(i))


def sheep(n):
    return "🐏" * n


if __name__ == "__main__":
    main()