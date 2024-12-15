class Contact:
    def __init__(self , name , phone_number , email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    
    
class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self , contact):
        self.contacts.append(contact)
        print('contact added !\n')
        
            
    def display_contacts(self):
        print('\nContact History \n')
        for contact in self.contacts:
            print(f'{contact.name}\t{contact.phone_number}\t{contact.email}')
        print('\n')
        
            
    def search_contact_by_name(self , contact_name):
        for contact in self.contacts:
            if contact.name.lower() == contact_name.lower():
                print('Yes , Number is available !')
                return contact
        print('Number is not available !')
        return None 
    

            
manager = ContactManager()


while(True):
    print('1. Add a new contact.')
    print('2. View all contacts.')
    print('3. Search for a contact.')
    print('4. Exit.')
    
    x = int(input('Please input number between 1 to 4 : '))
    
    if x == 1:
        name = input('name : ')
        phone = input('phone : ')
        email = input('email: ')
        
        name = Contact(name , phone , email)
        manager.add_contact(name)
    elif x == 2:
        manager.display_contacts()
    elif x == 3:
        name = input('name : ')
        manager.search_contact_by_name(name)
    elif x == 4:
        print('The End ...')
        break
    else:
        print('Invalid input , please inter number between 1 to 4')
    
