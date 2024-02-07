students = ["Hermione", "Harry", "Ron"]


for i in range(len(students)):
    print(i + 1, students[i])


"""Lines 9-10 does the same thing as lines 4-5"""
for i, student in enumerate(students):
    print(i + 1, student)
