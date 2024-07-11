from lesson_11_abstraction.homework_11_1.person import Person


class Student(Person):

    def __init__(self, gender : str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return (f"Student: {self.first_name} {self.last_name};\n{self.age} years old;\n{self.gender}; "
                f"\nRecord Book: {self.record_book}\n")