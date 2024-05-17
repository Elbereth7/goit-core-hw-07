from field import Field
from datetime import datetime

# Class for storing the record birthday
class Birthday(Field):
    def __init__(self, value):
        try:
            super().__init__(value)
            self.value = datetime.strptime(value, '%d.%m.%Y').date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __str__(self):
        return datetime.strftime(self.value, '%d.%m.%Y')