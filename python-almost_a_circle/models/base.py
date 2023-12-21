# models/__init__.py (empty file)

# models/base.py
class Base:
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id  # assign the public instance attribute id with the argument value
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  # assign the incremented value to the public instance attribute id