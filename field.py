# Base class for record fields
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value