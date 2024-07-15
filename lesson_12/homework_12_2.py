from lesson_12.homework_12_2 import Order
from lesson_12.homework_12_2.buyer import Buyer
from lesson_12.homework_12_2.product import Product

vasyl = Buyer("Vasyl", "Virastiuk", "Fedorovich", 380507859086)
fedor = Buyer("Fedor", "Virastiuk", "Ivanovich", 380505870968)

macobook = Product("MacBook", 55000, "13 Pro M2",'16/512 gb')
iphone = Product("Iphone", 33000, "13 Pro max",'12/256 gb')
asus_rog = Product("Игровой компуктер", 33000, "2 гига, 2 ядра, игровая видеокарта "
                   ,'И босс корейский или не босс')
rice_plate = 300
xiaomi = Product("Xiaomi redmi mega pro", rice_plate, "Нисе не лагает и все летает"
                 ,'100gb ram, 1000 gb SSd ')
samsung = Product("Samsung S228 Ultra", 32999, "Дешевле чем афон и без челки, и бос внатуре корейский "
                  ,'12/256 gb')

#Если отсылку не поймешь, то ты пидор
order_227 = Order(227, vasyl)
order_227.add_product(macobook, 1)
order_227.add_product(iphone, 2)
print(order_227)
print(order_227.get_total())
order_227.add_product(iphone, 3)
order_227.add_product(macobook, 2)
print(order_227)
print(order_227.get_total())