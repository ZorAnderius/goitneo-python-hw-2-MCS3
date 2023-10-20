from colorama import Fore

def add_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return Fore.RED + "Missing one or two arguments. Please try again"
    if name in contacts:
        return Fore.YELLOW + f"User {name} is already in your phonebook. If you want to change phone use 'change' operation"
    contacts[name] = phone
    return Fore.GREEN + 'Contact added.'
    


def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return Fore.RED + "Missing one or two arguments. Please try again"
    if not contacts:
        return Fore.YELLOW + "Phonebook is empty."
    if name in contacts:
        contacts[name] = phone
        return Fore.GREEN + 'Contact changed.'
    else:
        return Fore.RED + 'Contact not found.'


def find_phone(args, contacts):
    try:
        name = args[0]
    except IndexError:
        return Fore.RED + "Missing argument name. Please try again"
    if not contacts:
        return Fore.YELLOW + "Phonebook is empty."
    if name in contacts:
        phone = contacts[name]
        return Fore.LIGHTMAGENTA_EX + phone
    else:
        return Fore.RED + "Wrong username"


def show_all(contacts):
    contacts_str = ''
    if not contacts:
        return Fore.YELLOW + "Phonebook is empty."
    for key, value in contacts.items():
        first_str = Fore.LIGHTMAGENTA_EX + "{: >10}".format(key)
        second_str = Fore.WHITE + "{: <20} \n".format(value)
        contacts_str += f"{first_str} : {second_str}"
    return contacts_str[:-1:]


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = dict()
    print(Fore.BLUE + "Welcome to the assistant bot!")
    while True:
        user_input = input(Fore.BLUE + "Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.BLUE + "Good bye!")
            break

        elif command == "hello":
            print(Fore.BLUE + "How can I help you?")
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(find_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print(Fore.RED + "Invalid command.")

if __name__ == "__main__":
    main()