class Person:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name


def __str__(self) -> str:
    return f"Person: {self.first_name} {self.last_name},\n{self.age} years old,\n{self.gender})"
