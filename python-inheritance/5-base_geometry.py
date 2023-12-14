"""Integer validator"""
class BaseGeometry:
    """
    A class representing basic geometry operations.

    Methods:
        area(): Placeholder method for area calculation.
        integer_validator(name, value): Validates the value as an integer.
    """

    def area(self):
        """
        Raises:
            Exception: Indicates that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.

        Args:
            name (str): The name associated with the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        
        print(dir(bg))






































































































































































        