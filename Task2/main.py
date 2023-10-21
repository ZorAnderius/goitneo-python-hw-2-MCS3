from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
    
class Name(Field):
    def __init__(self, name):
        super().__init__(name)
        
        
class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)
           
            
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        if phone and len(phone) == 10:
            self.phones.append(Phone(phone))
        else:
            print("Invalid phone number. Length of phone must be 10 numbers.")
    
    def find_phone(self, phone):
        if phone in (p.value for p in self.phones):
            return phone
        else:
            return None
        
    def remove_phone(self, phone):
        if self.find_phone(phone):
            index = (p.value for p in self.phones).index(phone)
            del self.phones[index]
            return index
        else:
            return None
    
    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone):
            index = self.remove_phone(old_phone)
            if index:
                self.phones.insert(index, Phone(new_phone))
        else:
            return f"Phone number {old_phone} is not in the {self.name} record"
        
    def __str__(self):
        if self.phones:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        else:
            return f"Contact name: {self.name.value}, phones: Phonebook is empty"
        
         
class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
  
        
    def add_record(self, record):
        self.data[record.name.value] = record
        
        
    def find(self, name):
        if name in self.data:
            return self.data[name]
        
    def delete(self, name):
        del self.data[name]




# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567903")
john_record.add_phone("5555555555")
john_record.add_phone("555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)