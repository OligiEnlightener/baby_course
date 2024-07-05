from lesson_10_oop.homework_10_3.Item import Item
from lesson_10_oop.homework_10_3.User import User


class Purchase:
    def __init__(self, user: User):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item: Item, cnt: int):
        self.products[item] = cnt

    def __str__(self) -> str:
        result = f'User: {self.user.name} {self.user.surname}\n'
        for item in self.products:
            result += item.name + ": "
            result += str(self.products[item]) + " pcs\n"
        return result

    def get_total(self) -> int:
        result = 0
        for item in self.products:
            result += (self.products[item] * item.price)
        return result
