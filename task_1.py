from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __repr__(self):
        return f'Name(name={self.value})'

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

        if not (value.isdigit() and len(value) == 10): 
            raise ValueError(f'Invalid phone number {value}')

    def __repr__(self):
        return f'Phone(phone={self.value})'
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        
        for index, item in enumerate(self.phones):
            if item.value == Phone(phone).value:
                self.phones.pop(index)
                return
        raise ValueError(f"Phone number: {phone} not found")
            
    def edit_phone(self, old_phone, new_phone):

        for i, item in enumerate(self.phones):
            if item.value == Phone(old_phone).value:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError(f"Phone number: {old_phone} not found")
    
    def find_phone(self, phone):
        result = None
        for item in self.phones:
            if item.value == Phone(phone).value:
                result = item
        return result
                
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def __str__(self):
        if not self.data:
            return "Address book is empty"
        return "\n".join(str(record) for record in self.data.values())
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record 
    
    def find(self, name):
        result = [self.data[item] for item in self.data if item.lower() == name.lower()]
        if result: return result[0] 
        else: return None

    def delete(self, name):
        self.data ={key: value for key, value in self.data.items() if key.lower() != name.lower()}
    

        

#-------------------------------------------------------------------

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
     
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
