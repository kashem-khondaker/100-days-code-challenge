from abc import ABC
from order import Order

class User(ABC):
    def __init__(self , name , phone , email , address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address ):
        super().__init__(name, phone, email, address)
        self.cart = Order()
    
    
    def view_menu(self , restaurant):
        restaurant.menu.show_menu()
        
    
    def add_to_cart(self , restaurant , item_name , quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print('Limit over !!')
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print('item added')
        else:
            print('item not found')
            
    
    def view_cart(self):
        print('\nview cart')
        print('Name\tPrice\tQuantity')
        
        for item , quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'\nTotal price : {self.cart.total_price}')
        
        
    def pay_bill(self):
        print(f'Total {self.cart.total_price} paid ')
        self.cart.clear()
        
    
class Employee(User):
    def __init__(self, name, phone, email, address , age , designation , salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary
        
        
        
class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        
    
    def add_employee(self,restaurant , employee):
        restaurant.add_employee(employee)
        
        
    def view_employee(self , restaurant):
        restaurant.view_employee()
        
    
    def add_item(self , restaurant , item):
        restaurant.menu.add_menu_item(item)
    
    
    def view_item(self , restaurant):
        restaurant.menu.show_menu()
      
        
    def remove_item(self , restaurant , item):
        restaurant.menu.remove_item(item)
        
        

        