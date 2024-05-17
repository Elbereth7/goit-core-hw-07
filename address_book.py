from collections import UserDict
from record import Record
from datetime import timedelta, date

# Class for storing and managing records.
class AddressBook(UserDict):
        
    # Add record to self.data
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    # finds a record by name
    def find(self, name):
        if name in self.data.keys():
            return self.data[name]

    # deletes a record by name
    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]
    


    @staticmethod
    def find_next_weekday(start_date, weekday):
        current_weekday = start_date.weekday()
        days_ahead = weekday - current_weekday
        if days_ahead <= 0:
            days_ahead += 7
        new_date = start_date + timedelta(days=days_ahead)
        return new_date

    @staticmethod
    def adjust_for_weekend(birthday):
        if birthday.weekday() >= 5:
            birthday = AddressBook.find_next_weekday(birthday, 0)
        return birthday

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()
        for name in self.data.keys():
            if self.data[name].birthday != None:
                birthday_this_year = self.data[name].birthday.value.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = self.data[name].birthday.value.replace(year=today.year + 1)
                if 0 <= (birthday_this_year - today).days <= days:
                    congratulation_date_str = str(AddressBook.adjust_for_weekend(birthday_this_year))
                    upcoming_birthdays.append({"name": name, "congratulation_date": congratulation_date_str})
        return upcoming_birthdays
    

            
        
        

    