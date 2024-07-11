class Item:

    def __init__(self, name: str, price: int, description: str, dimensions:str):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self) -> str:
        return f'Item name: {self.name}; Price: {self.price}; {self.description}; size: {self.dimensions}'