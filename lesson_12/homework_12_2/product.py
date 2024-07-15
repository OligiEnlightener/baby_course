class Product:
    def __init__(self, name: str, price: int, descript: str, dimensions: str):
        self.dimensions = dimensions
        self.descript = descript
        self.price = price
        self.name = name

    def __str__(self)-> str:
        return f'{self.name} {self.descript}, {self.price} Uah\n'
