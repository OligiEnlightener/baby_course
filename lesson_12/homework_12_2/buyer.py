class Buyer:
    def __init__(self, name: str, last_name: str, patronymic: str, phone_number: int):
        self.name = name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone_number = phone_number


    def __str__(self):
        return f'{self.name} {self.last_name} {self.patronymic}\nPhone: {self.phone_number}'