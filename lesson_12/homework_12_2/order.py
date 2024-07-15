from lesson_12.homework_12_2 import Buyer, Product


class Order:
    def __init__(self, number: int, buyer: Buyer):
        self.products = {}
        self.number = number
        self.buyer = buyer
        self.total = 0

    def add_product(self, product: Product, qnt: int):
        self.products[product] = qnt
        self.update_total()

    def update_total(self):
        total_updated = 0
        for key, value in self.products.items():
            total_updated += key.price * value
        self.total = total_updated

    def get_total(self) -> int:
        return self.total

    def __str__(self) -> str:
        order_info = f'Order N#: {self.number}\nFor: {self.buyer}\nOrdered:\n'
        order_info += "".join(str(product) for product in self.products)
        return order_info
