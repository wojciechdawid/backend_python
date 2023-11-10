import math


class Circle:
    def __init__(self, radius: int | float = 1):
        """Initializes Circle object"""
        self.__radius: int | float = radius
        self.__diameter = 2 * radius
        self.__area = math.pi * radius ** 2

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
            raise ValueError('Radius must be a positive numerical value!')

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
            raise ValueError("Diameter must be a positive numerical value!")

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
            raise ValueError("Area must be a positive numerical value!")

    def __str__(self):
        """Returns text representation of an instance"""
        return f'Okrąg o średnicy {round(self.__radius, 2)}.'

    def __eq__(self, other) -> bool:
        """Checks if two instances of a class are not equal"""
        if isinstance(other, Circle):
            return self.__radius == other.__radius
        elif isinstance(other, Square):
            return self.__area == other.area
        else:
            raise TypeError("Both objects must be instances of a Circle or Square class!")

    def __ne__(self, other) -> bool:
        """Checks if two instances of a class are not equal"""
        if isinstance(other, Circle):
            return self.__radius != other.__radius
        elif isinstance(other, Square):
            return self.__area != other.area
        else:
            raise TypeError("Both objects must be instances of a Circle or Square class!")

    def __lt__(self, other) -> bool:
        """Checks if first circle is smaller than the second"""
        if isinstance(other, Circle):
            return self.__radius < other.__radius
        elif isinstance(other, Square):
            return self.__area < other.area
        else:
            raise TypeError("Both objects must be instances of a Circle or Square class!")

    def __le__(self, other) -> bool:
        """Checks if first circle is smaller or equal than the second"""
        if isinstance(other, Circle):
            return self.__radius <= other.__radius
        elif isinstance(other, Square):
            return self.__area <= other.area
        else:
            raise TypeError("Both objects must be instances of a Circle or Square class!")

    def __gt__(self, other) -> bool:
        """Checks if first circle is bigger than the second"""
        if isinstance(other, Circle):
            return self.__radius > other.__radius
        elif isinstance(other, Square):
            return self.__area > other.area
        else:
            raise TypeError("Both objects must be instances of a Circle or Square class!")

    def __ge__(self, other) -> bool:
        """Checks if first circle is bigger or equal than the second"""
        if isinstance(other, Circle):
            return self.__radius >= other.__radius
        elif isinstance(other, Square):
            return self.__area >= other.area
        else:
            raise TypeError("Both objects must be instances of a Circle or Square class!")

    def __add__(self, other):
        """Adds two instances and creates a new one based on their area"""
        if isinstance(other, Circle):
            return Circle(math.sqrt((self.__area + other.__area) / math.pi))
        elif isinstance(other, Square):
            return Circle(math.sqrt((self.__area + other.area) / math.pi))
        else:
            raise TypeError("Both objects must be instances of a Circle class!")


class Square:
    def __init__(self, side: int | float = 1):
        """Initializes Square object"""
        self.__side: int | float = side
        self.__area = side ** 2

    @property
    def side(self):
        """Gets side value"""
        return round(self.__side, 2)

    @side.setter
    def side(self, value: int | float):
        """Sets side value"""
        if isinstance(value, (int, float)) and value > 0:
            self.__side = value
        else:
            raise ValueError("Side must be a positive numerical value!")

    @property
    def area(self):
        """Gets area value"""
        return round(self.__area, 2)

    @area.setter
    def area(self, value: int | float):
        """Sets area value and calculates other metrics"""
        if isinstance(value, (int, float)) and value > 0:
            self.__area = value
            self.__side = math.sqrt(value)
        else:
            raise ValueError("Area must be a positive numerical value!")

    def __str__(self):
        """Returns text representation of an instance"""
        return f'Kwadrat o boku {round(self.__side, 2)}.'

    def __eq__(self, other) -> bool:
        """Checks if two instances of a class are not equal"""
        if isinstance(other, Square):
            return self.__side == other.__side
        elif isinstance(other, Circle):
            return self.__area == other.area
        else:
            raise TypeError("Both objects must be instances of a Circle or Square class!")

    def __ne__(self, other) -> bool:
        """Checks if two instances of a class are not equal"""
        if isinstance(other, Square):
            return self.__side == other.__side
        elif isinstance(other, Circle):
            return self.__area != other.area
        else:
            raise TypeError("Both objects must be instances of a Circle or Square class!")

    def __lt__(self, other) -> bool:
        """Checks if first circle is smaller than the second"""
        if isinstance(other, Square):
            return self.__side < other.__side
        elif isinstance(other, Circle):
            return self.__area < other.area
        else:
            raise TypeError("Both objects must be instances of a Circle or Square class!")

    def __le__(self, other) -> bool:
        """Checks if first circle is smaller or equal than the second"""
        if isinstance(other, Square):
            return self.__side <= other.__side
        elif isinstance(other, Circle):
            return self.__area <= other.area
        else:
            raise TypeError("Both objects must be instances of a Circle or Square class!")

    def __gt__(self, other) -> bool:
        """Checks if first circle is bigger than the second"""
        if isinstance(other, Square):
            return self.__side > other.__side
        elif isinstance(other, Circle):
            return self.__area > other.area
        else:
            raise TypeError("Both objects must be instances of a Circle or Square class!")

    def __ge__(self, other) -> bool:
        """Checks if first circle is bigger or equal than the second"""
        if isinstance(other, Square):
            return self.__side >= other.__side
        elif isinstance(other, Circle):
            return self.__area >= other.area
        else:
            raise TypeError("Both objects must be instances of a Circle or Square class!")

    def __add__(self, other):
        """Adds two instances and creates a new one based on their area"""
        if isinstance(other, Square):
            return Square(math.sqrt(self.__area + other.__area))
        elif isinstance(other, Circle):
            return Square(math.sqrt(self.__area + other.area))
        else:
            raise TypeError("Objects must be instances of Circle or Square class!")


if __name__ == '__main__':
    c = Circle(10)
    assert c.area == round(math.pi * 10 ** 2, 2)
    c2 = Circle(20)
    c3 = c + c2
    assert isinstance(c3, Circle)
    s1 = Square(10)
    sc1 = s1 + c2
    assert sc1.side == 36.83
