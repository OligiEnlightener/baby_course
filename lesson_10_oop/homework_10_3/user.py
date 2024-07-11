class User:

    def __init__(self, name: str, surname: str, numberphone: int):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self) -> str:
        return f'User name: {self.name}  {self.surname}; Phone: {self.numberphone}'