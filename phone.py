from field import Field

# Class for storing the record phone      
class Phone(Field):
    # Includes phone number validation (must be equal to 10 numbers)
    def __init__(self, value):
        if not self.phone_validation(value):
            raise ValueError(f'Phone {value} format is incorrect: phone must consist of 10 numbers')
        super().__init__(value)

    def phone_validation(self, value):
        return len(value) == 10 and value.isnumeric()

        
