# models/base.py
class Base:
    """
    Base class for managing id attribute for other classes.

    Attributes:
        __nb_objects (int): Private class attribute to track the number of objects created.
        id (int): Public instance attribute representing the object's identifier.
    """

    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Args:
            id (int, optional): Identifier for the object. Defaults to None.

        Examples:
            Creating an instance of Base without passing an id:
                >>> obj1 = Base()
                >>> print(obj1.id)
                1

            Creating an instance of Base by passing an id:
                >>> obj2 = Base(100)
                >>> print(obj2.id)
                100

            Creating an instance of Base without passing an id will assign an id:
                >>> obj3 = Base()
                >>> print(obj3.id)
                2

            Creating an instance of Base without passing an id will assign an id + 1 of the previous instance created:
                >>> obj4 = Base()
                >>> print(obj4.id)
                3
        """
        if id is not None:
            self.id = id  # assign the public instance attribute id with the argument value
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  # assign the incremented value to the public instance attribute id