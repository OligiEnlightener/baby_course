from math import sqrt


class Rectangle:
    def __init__(self, width: int | float, height: int | float):
        self.height = height
        self.width = width
        self.area = round(height * width)

    def __eq__(self, other):
        return self.area == other.area

    def __add__(self, other):
        new_side = sqrt(self.area + other.area)
        return Rectangle(new_side, new_side)

    def __mul__(self, other: int):
        new_side = sqrt(self.area * other)
        return Rectangle(new_side, new_side)

    def __str__(self):
        return f"Height: {self.height}\nWidth: {self.width}\nArea: {self.area}\n"
