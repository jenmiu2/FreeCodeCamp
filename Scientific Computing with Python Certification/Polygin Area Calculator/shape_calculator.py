import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    # get_area: Returns area (width * height)
    def get_area(self):
        return self.width * self.height

    # get_perimeter: Returns perimeter (2 * width + 2 * height)
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** .5

    def get_picture(self):
        picture = ""
        if self.width >= 50 or self.height >= 50: return "Too big for picture."
        for i in range(self.height):
            picture += "{:*^{length}}\n".format("", length=self.width)
        return picture

    def get_amount_inside(self, other_shape):
        amount = self.get_area()
        other_amount = other_shape.get_area()
        return math.floor(amount / other_amount)

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def __str__(self):
        return "Square(side={})".format(self.width)
