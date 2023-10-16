#!/usr/bin/python3
"""rectangle.py"""


from models.base import Base


class Rectangle(Base):
    """Inherits from Base class"""
    def validate(self, name, value):
        """Validates values"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError('{} must >= 0'.format(name))
        else:
            if value <= 0:
                raise ValueError('{} must be > 0'.format(name))

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instatiation"""
        self.validate("width", width)
        self.__width = width
        self.validate("height", height)
        self.__height = height
        self.validate("x", x)
        self.__x = x
        self.validate("y", y)
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate("width", value)
        self.__value = value

    @property
    def height(self):
        """Getter for height"""
        return self.__width

    @height.setter
    def height(self, value):
        self.validate("height", value)
        self.__value = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.validate("x", value)
        self._x = value

    def area(self):
        """Computes the area"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance"""
        for i in range(self.__y):
            """Print the vertical displacement first"""
            print("")
        for x in range(self.__height):
            """Then print empty spaces first before the #'s"""
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """"overriding __str__()"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """"assigns an argument to each attribute"""

        up = ["id", "width", "height", "x", "y"]
        if (args):
            for i in range(len(args)):
                setattr(self, up[i], args[i])

        else:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """Returns dict representation of a Rectangle"""
        return {
            "x": self.x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            'width': self.__width,
        }
