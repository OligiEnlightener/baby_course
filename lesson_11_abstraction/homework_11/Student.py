from lesson_11_abstraction.homework_11.Person import Person


class Student(Person):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return (f"Student: {self.first_name} {self.last_name};\n{self.age} years old;\n{self.gender}; "
                f"\nRecord Book: {self.record_book}\n")