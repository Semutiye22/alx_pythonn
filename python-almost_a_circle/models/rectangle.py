"""models/rectangle.py"""
from models.be.pase import Base  

class Rectangle(Base):
    """
    Rectangle class inheriting from Base.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x-coordinate of the rectangle.
        y (int): y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): Identifier for the object. Defaults to None.

        Raises:
            TypeError: If width, height, x, or y are not integers.
            ValueError: If width or height are less than or equal to 0, or if x or y are less than 0.
        """
        super().__init__(id)  # Call the superclass constructor with id

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: Width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): Width value to set.

        Raises:
            TypeError: If the input value is not an integer.
            ValueError: If the input value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: Height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): Height value to set.

        Raises:
            TypeError: If the input value is not an integer.
            ValueError: If the input value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the rectangle.

        Args:
            value (int): x-coordinate value to set.

        Raises:
            TypeError: If the input value is not an integer.
            ValueError: If the input value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the rectangle.

        Args:
            value (int): y-coordinate value to set.

        Raises:
            TypeError: If the input value is not an integer.
            ValueError: If the input value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the rectangle using the '#' character, considering x and y positions.

        Prints:
            The rectangle based on its width and height using '#' with respect to x and y positions.
        """
for _ in range(self.__y):
            print()
for _ in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
            str: String representation of the Rectangle object.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

def update(self, *args, **kwargs):
         """
        Assigns arguments to each attribute in a specific order or using keyword arguments.

        Args:
            *args: Variable number of arguments representing id, width, height, x, and y in the given order.
            **kwargs: Variable number of keyword arguments representing attribute name and value pairs.
        """
if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
else:
            for key, value in kwargs.items():
                setattr(self, key, value)