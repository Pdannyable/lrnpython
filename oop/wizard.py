# Inheritance, instead of having repetitions as shown from lines 5-23
# the usefulness of inheritance is shown in lines 26 -
"""
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house
    ...

class Professor:
    def __init__(self, name, subject):
        if not name:
            raise ValueError("Missing name")
        self.subject = subject
"""

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)  # class Student inherits name from class Wizard
        self.house = house

    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")