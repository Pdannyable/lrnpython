oruko = input("What's your name? ")


with open("oruko.txt", "a") as file:
    file.write(f"{oruko}\n")