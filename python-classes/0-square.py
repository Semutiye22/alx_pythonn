class Square:
    def __init__(self, size):
        self.__size = size

# Example usage:
square = Square(5)
# Accessing the private attribute directly will result in an AttributeError
# print(square.__size)  # This would result in an error because __size is private