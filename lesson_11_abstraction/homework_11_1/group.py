from lesson_11_abstraction.homework_11_1.student import Student


class Group:

    def __init__(self, number: int):
        self.number = number
        self.group = set()

    def add_student(self, student: Student):
        self.group.add(student)

    def delete_student(self, last_name: str):
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name: str) -> Student:
        result = None
        for student in self.group:
            result = student if student.last_name == last_name else result
        return result

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Group number: {self.number}\n{all_students}'