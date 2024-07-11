from lesson_11_abstraction.homework_11_1.group import Group
from lesson_11_abstraction.homework_11_1.student import Student
from lesson_12.homework_12_1.group_limit_size import GroupLimitSizeException


class Group_limited(Group):
    group_size = 10
    WARNING_COLOR = '\033[93m'

    def add_student(self, student: Student):
        try:
            self._add(student)
        except GroupLimitSizeException as gls:
            print(f'{self.WARNING_COLOR}{gls.msg}')

    def _add(self, student: Student):
        if len(self.group) < self.group_size:
            self.group.add(student)
        else:
            raise GroupLimitSizeException
