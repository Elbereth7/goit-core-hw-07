from pathlib import Path
from functools import wraps
import data_handler as dh
from record import Record
from address_book import AddressBook

file_path = Path('contacts.txt')

# Decorator to add a logic for Exceptions which can appear while reading the file (file does not exist)
def file_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try: 
            return func(*args, **kwargs)
        except FileNotFoundError:
            book = AddressBook()
            return book
    return inner

def write_to_file(book, file_path=file_path):
    with open(file_path, 'w') as file:
        for output_string in dh.show_all(book):
            file.write(f'{output_string}\n')
            
@file_error
def read_from_file(file_path=file_path):
    book = AddressBook()
    with open(file_path, 'r') as file:
        string = file.read()
        if string:
            records_list = string.strip().split('\n')
            for record in records_list:
                args = record.split('; ')
                parameters = {}
                for arg in args:
                    arg_list = arg.split(': ')
                    parameters.update({arg_list[0]:arg_list[1]})
                new_record = Record(parameters['Contact name'])
                if 'phones' in parameters.keys():
                    for phone in parameters['phones'].split(', '):
                        new_record.add_phone(phone)
                if 'birthday' in parameters.keys():
                    new_record.add_birthday(parameters['birthday'])
                book.add_record(new_record)
    return book
