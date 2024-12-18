from abc import ABC
from Menu import Order
from Restaurant import Restaurant

class Customer(ABC):
    def __init__(self, restaurant, name, email, address):
        self.restaurant = restaurant  
        self.name = name 
        self.email = email
        self.address = address
        self.balance = 0 
        self.orders_history = []  
        
        
    def create_account(self, customer):
        self.restaurant.add_customer(customer)
    
    
    def show_menu(self):
        self.restaurant.view_menu()
    
    
    def show_balance(self):
        print(f"Balance: {self.balance}")
    
    
    
    def check_balance(self, amount):
        return self.balance >= amount
    
    
    
    def add_funds(self, amount):
        if amount >= 0:
            self.balance += amount
            print('Balance added successfully...\n')
        else:
            print('Negative balance not allowed...\n')
    
    
    def view_orders(self):
        if len(self.orders_history) == 0:
            print('Empty\n')
        else:  
            print('Name\tQuantity\tTotal price\n\n')  
            for order in self.orders_history:
                print(f'{order.name}\t{order.quantity}\t{order.price}')
                
    
    
    def place_order(self, name, quantity):
        menu_item = self.restaurant.find_menu_by_name(name)
        if menu_item:  
            price = menu_item.price  
            total_price = price * quantity  
            print(f"Total Price for {quantity} {name}(s): {total_price}")
        
            if self.check_balance(total_price):  
                self.balance -= total_price  
                ord = Order(name=name, price=total_price, quantity=quantity)  
                self.orders_history.append(ord)  
                print('Order placed successfully. Food item in process.\n')
            else:
                print('Insufficient balance. Please recharge your account.\n')
        else:
            print(f'Please check again, "{name}" not found in the menu list.\n')
