from input_parser import parse_input
import data_handler as dh
import file_handler as fh

def main():
    book = fh.read_from_file()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            fh.write_to_file(book)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(dh.add_contact(args, book))
        elif command == "change":
            print(dh.change_contact(args, book))
        elif command == "phone":
            print(dh.show_phone(args, book))
        elif command == "all":
            for output_string in dh.show_all(book):
                print(output_string)
        elif command == "add-birthday":
            print(dh.add_birthday(args, book))
        elif command == "show-birthday":
            print(dh.show_birthday(args, book))
        elif command == "birthdays":
            print(dh.birthdays(book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()