'''base class'''
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

        If provided, sets the id directly to the given value.
        If not provided, increments the __nb_objects count and assigns the new value as id.
        """
        if id is not None:
            self.id = id  # assign the public instance attribute id with the argument value
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  # assign the incremented value to the public instance attribute id