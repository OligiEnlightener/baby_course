from lesson_10_oop.homework_10_3.item import Item
from lesson_10_oop.homework_10_3.user import User



class Purchase:
    def __init__(self, user: User):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item: Item, cnt: int):
        self.products[item] = cnt
        self.update_total()

    def update_total(self):
        total_updated = 0
        for key, value in self.products.items():
            total_updated += key.price * value
        self.total = total_updated

    def __str__(self) -> str:
        result = f'User: {self.user.name} {self.user.surname}\n'
        for key, value in self.products.items():
            result += key.name + ": "
            result += str(value) + " pcs —> "
            result += str(key.price) + " uah\n"
        return result

    def get_total(self) -> int:
        return self.total
