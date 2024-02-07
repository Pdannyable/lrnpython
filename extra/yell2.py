"""Alternnatively, lines 4-11 can be replaced with lines 16-32"""
"""

def main():
    yell(["This", "is", "s76D"])


def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)
    
    
if __name__ == "__main__":
"""


def main():
    yell("This", "is", "s76d")


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
