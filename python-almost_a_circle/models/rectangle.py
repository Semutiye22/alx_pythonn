""" models/rectangle.py """
class Rectangle:
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
        """
        super().__init__(id)  # Call the superclass constructor with id

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        """
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
        """
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
        """
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
        """
        self.__y = value