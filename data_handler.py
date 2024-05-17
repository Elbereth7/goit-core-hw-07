from functools import wraps
from address_book import AddressBook
from record import Record

# Decorator to add a logic for Exceptions which can appear in data handling functions
def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try: 
            return func(*args, **kwargs)
        except ValueError as ve:
            if str(ve).startswith("not enough values to unpack (expected at least 3"):
                return "Please provide a name, old phone and new phone. "
            elif str(ve).startswith("not enough values to unpack (expected at least 2"):
                return "Please provide a name and phone / birthday to be added / updated."
            elif str(ve).startswith("not enough values to unpack (expected at least 1"):
                return "Please provide a name for which you need to check phone / birthday."
            else:
                return ve
        except IndexError:
            return "Please provide a name to be checked in a phone book."
        except KeyError:
            return f"Contact {args[0]} does not exist"
        except AttributeError:
            return f'Data you are looking for does not exist'
    return inner

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        print(f'Contact {name} does not exist in a phone book. Should I add it?')
        return change_contact_validation(name, new_phone, book)
    elif old_phone and new_phone:
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    
def change_contact_validation(name, new_phone, book: AddressBook):
    while True:
        user_input = input('Enter yes/no: ').strip().lower()
        if user_input == 'yes':
            add_contact(name, new_phone, book)
            return "Contact added."
        elif user_input == 'no':
            return "Contact skipped."
        else:
            print("Invalid answer.")        

@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    return record.phones

@input_error 
def show_all(book: AddressBook):
    if not book:
        yield "Contact list is empty"
    for name in book.keys():
        yield book[name]

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if birthday:
        record.add_birthday(birthday)
    return message
    
@input_error       
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    return record.birthday

@input_error       
def birthdays(book: AddressBook):
    bdays = []
    for bday in book.get_upcoming_birthdays():
        bdays.append(', '.join([f'{key}: {bday[key]}' for key in bday]))
    result = '\n'.join(bdays)
    return result



  




