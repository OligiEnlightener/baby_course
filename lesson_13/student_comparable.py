from lesson_11_abstraction.homework_11_1.student import Student


class Student_comparable(Student):
    def __eq__(self, student: Student):
        return str(self) == str(student)

    def __hash__(self):
        return hash(str(self))
