import math


class Circle:
    def __init__(self, radius=1):
        self.__radius: int | float = radius
        self.__diameter: int | float = 2 * radius
        self.__area: int | float = math.pi * radius ** 2

    @property
    def radius(self) -> int | float:
        """Gets radius of a circle"""
        return round(self.__radius, 2)

    @radius.setter
    def radius(self, value: int | float):
        """Sets radius and updates other metrics"""
        if isinstance(value, (int, float)) and value > 0:
            self.__radius = value
            self.__diameter = 2 * value
            self.__area = math.pi * value ** 2
        else:
            raise ValueError('Radius must be a positive numeric value!')

    @property
    def diameter(self) -> int | float:
        """Gets diameter of a circle"""
        return round(self.__diameter, 2)

    @diameter.setter
    def diameter(self, value: int | float):
        """Sets diameter and updates other metrics"""
        if isinstance(value, (int, float)) and value > 0:
            self.__diameter = value
            self.__radius = value / 2
            self.__area = math.pi * (value / 2) ** 2
        else:
            raise ValueError("Diameter must be a positive numeric value!")

    @property
    def area(self) -> int | float:
        """Gets area of a circle"""
        return round(self.__area, 2)

    @area.setter
    def area(self, value: int | float):
        """Sets area and updates other metrics"""
        if isinstance(value, (int, float)) and value > 0:
            self.__area = value
            self.__radius = math.sqrt(value / math.pi)
            self.__diameter = 2 * (math.sqrt(value / math.pi))
        else:
            raise ValueError("Area must be a positive numeric value!")

    def __str__(self):
        """Returns text representation of an instance"""
        return f'Okrąg o średnicy {round(self.__radius, 2)}.'


if __name__ == '__main__':
    c = Circle(5)
    print(c.area)
