from lesson_12.homework_12_2 import Buyer


class Order:
    def __init__(self, number: int, buyer: Buyer):
        self.products = {}
        self.number = number
        self.buyer = buyer


    def get_total(self):
        pass

    def __str__(self):
        pass