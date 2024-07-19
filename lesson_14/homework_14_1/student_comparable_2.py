from lesson_11_abstraction.homework_11_1.student import Student


class Student_comparable_2(Student):
    def __eq__(self, other: Student):
        return self.age == other.age

    def __gt__(self, other: Student):
        return self.age > other.age

    def __lt__(self, other:Student):
        return self.age < other.age