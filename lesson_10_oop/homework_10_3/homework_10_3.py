from lesson_10_oop.homework_10_3.item import Item
from lesson_10_oop.homework_10_3.purchase import Purchase
from lesson_10_oop.homework_10_3.user import User

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, f"Всього 60, {cart.get_total()}"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40, f'{cart.get_total()}'

cart1 = Purchase(buyer)
apple = Item('apple', 2, "red", "middle", )
carrot = Item('carrot', 1, "red", "middle", )
pear = Item('pear', 3, "red", "middle", )

cart1.add_item(apple, 10)
cart1.add_item(carrot, 15)
cart1.add_item(pear, 5)
print(f'cart1: {cart1}')
print(f"total: {cart1.get_total()}")
cart1.add_item(apple, 20)
print(f'cart1: {cart1}')
print(f"total: {cart1.get_total()}")