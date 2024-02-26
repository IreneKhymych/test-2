import math

class Triangle:
    def __init__(self, a, b, c):
        if self._is_valid_triangle(a, b, c):
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            raise ValueError("Invalid triangle sides")

    def set_a(self, a):
        if self._is_valid_triangle(a, self.get_b(), self.get_c()):
            self.__a = a
        else:
            print("set_a: Error")

    def set_b(self, b):
        if self._is_valid_triangle(self.get_a(), b, self.get_c()):
            self.__b = b
        else:
            print("set_b: Error")

    def set_c(self, c):
        if self._is_valid_triangle(self.get_a(), self.get_b(), c):
            self.__c = c
        else:
            print("set_c: Error")

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def perimeter(self):
        return self.get_a() + self.get_b() + self.get_c()

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.get_a()) * (p - self.get_b()) * (p - self.get_c()))

    def show(self):
        print("Triangle", self.get_a(), self.get_b(), self.get_c())

    def _is_valid_triangle(cls, a, b, c):
        return a + b > c and a + c > b and b + c > a


class Rectangle:
    def __init__(self, width, height):
        if width > 0 and height > 0:
            self.__width = width
            self.__height = height
        else:
            raise ValueError("Invalid rectangle sides")

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("set_width: Error")

    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            print("set_height: Error")

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def perimeter(self):
        return 2 * (self.get_width() + self.get_height())

    def area(self):
        return self.get_width() * self.get_height()

    def show(self):
        print("Rectangle", self.get_width(), self.get_height())


class Trapeze:
    def __init__(self, base1, base2, side1, side2):
        if base1 > 0 and base2 > 0 and side1 > 0 and side2 > 0 and base1 != base2 and side1 != side2:
            self.__base1 = base1
            self.__base2 = base2
            self.__side1 = side1
            self.__side2 = side2
        else:
            raise ValueError("Invalid trapeze sides")

    def set_base1(self, base1):
        if base1 > 0:
            self.__base1 = base1
        else:
            print("set_base1: Error")

    def set_base2(self, base2):
        if base2 > 0:
            self.__base2 = base2
        else:
            print("set_base2: Error")

    def set_side1(self, side1):
        if side1 > 0:
            self.__side1 = side1
        else:
            print("set_side1: Error")

    def set_side2(self, side2):
        if side2 > 0:
            self.__side2 = side2
        else:
            print("set_side2: Error")

    def get_base1(self):
        return self.__base1

    def get_base2(self):
        return self.__base2

    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def perimeter(self):
        return self.get_base1() + self.get_base2() + self.get_side1() + self.get_side2()

    def area(self):
        h = self._height()
        return (self.get_base1() + self.get_base2()) * h / 2

    def show(self):
        print("Trapeze", self.get_base1(), self.get_base2(), self.get_side1(), self.get_side2())

    def _height(self):
        return math.sqrt(self.get_side1() ** 2 - ((self.get_base2() - self.get_base1()) ** 2) / 4)

class Parallelogram:
    def __init__(self, base, side, height):
        if base > 0 and side > 0 and height > 0:
            self.__base = base
            self.__side = side
            self.__height = height
        else:
            raise ValueError("Invalid parallelogram sides")

    def set_base(self, base):
        if base > 0:
            self.__base = base
        else:
            print("set_base: Error")

    def set_side(self, side):
        if side > 0:
            self.__side = side
        else:
            print("set_side: Error")

    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            print("set_height: Error")

    def get_base(self):
        return self.__base

    def get_side(self):
        return self.__side

    def get_height(self):
        return self.__height

    def perimeter(self):
        return 2 * (self.get_base() + self.get_side())

    def area(self):
        return self.get_base() * self.get_height()

    def show(self):
        print("Parallelogram", self.get_base(), self.get_side(), self.get_height())


class Circle:
    def __init__(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            raise ValueError("Invalid radius")

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("set_radius: Error")

    def get_radius(self):
        return self.__radius

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def area(self):
        return math.pi * (self.__radius ** 2)

    def show(self):
        print("Circle with radius", self.__radius)


if __name__ == '__main__':
    try:
        t = Triangle(14, 16, 20)
        r = Rectangle(22, 5)
        p = Parallelogram(8, 21, 6)
        c = Circle(3)
        tr = Trapeze(20, 23, 6, 3)

        figures = [t, r, p, c, tr]

        max_area_figure = max(figures, key=lambda f: f.area())
        max_perimeter_figure = max(figures, key=lambda f: f.perimeter())

        print(f"Figure with maximum area: {max_area_figure.__class__.__name__}, Area: {max_area_figure.area()}")
        print(f"Figure with maximum perimeter: {max_perimeter_figure.__class__.__name__}, Perimeter: {max_perimeter_figure.perimeter()}")

    except ValueError as e:
        print(e)
