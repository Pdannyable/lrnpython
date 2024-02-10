print("Welcome to my quiz game")


playing = input("Would you like to play? ")
if playing.lower() != "yes":
    quit()


name = input("Please enter your name: ")
print("Okay!", name, "let's play,")
score = 0


print("Question 1")
answer = input("What is the meaning of CPU? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("Question 2")
answer = input("Which continent is Belize located? ")
if answer.lower() == "South America":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("Question 3")
answer = input("What is the largest sense organ in the human body? ")
if answer.lower() == "skin":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("Question 4")
answer = input("What is the most expensive and rarest gemstone in the world? ")
if answer.lower() == "blue diamond":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("Question 5")
answer = input("Which is the smallest country in the world? ")
if answer.lower() == "Vatican city":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(name, "your score is: " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%")
