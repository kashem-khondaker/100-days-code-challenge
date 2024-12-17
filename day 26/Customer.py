from abc import ABC
from Menu import Order


class Customer(ABC):
    def __init__(self ,restaurant , name , email , address):
        self.restaurant = restaurant
        self.name = name 
        self.email = email
        self.address = address
        self.balance = 0  # initial balance is 0, i have to update it letter 
        self.orders_history = [] # database to store orders(object) that can i view and modify
        
    def create_account(self , customer):
        self.restaurant.add_customer(customer)
    
    def show_menu(self):
        self.restaurant.view_menu()
        
    def show_balance(self):
        print(f" Balance : {self.balance}")
    
    def check_balance(self , amount):
        return self.balance >= amount
        
    
    def add_funds(self , amount):
        if amount >= 0:
            self.balance += amount
            print('Balance added successfully ...\n')
        else:
            print('Negative balance not allow...\n')
    
    
    
    def view_orders(self):
        if len(self.orders_history) == 0:
            print('Empty\n')
        else:    
            for order in self.orders_history:
                print(f'{order.name}\t{order.price}\t{order.quantity}')
    
    

    def place_order(self , name , quantity):
        print(self.restaurant.find_menu_by_name(name))
        is_true = self.restaurant.find_menu_by_name(name)
        if self.restaurant.find_menu_by_name(name):
            pr = 0
            for menu in self.restaurant.menus:
                if menu.name.lower() == name.lower():
                    pr = menu.price
            Total_price = pr * quantity
            print(Total_price)
            if self.check_balance(Total_price):
                self.balance -= Total_price
                ord = Order(name=name , price=pr , quantity=quantity)
                self.orders_history.append(ord)
                print('Oder placed , FoodItem in proses .\n')
        else:
            print(f'Please check again , {name} not found in this menu list ..\n')

    def place_order(self, name, quantity):
        
        menu_item = self.restaurant.find_menu_by_name(name)  
        if menu_item:  
            price = menu_item.price  
            total_price = price * quantity  
            print(f"Total Price for {quantity} {name}(s): {total_price}")
        
            if self.check_balance(total_price):  
                self.balance -= total_price  
                ord = Order(name=name, price=price, quantity=quantity)  
                self.orders_history.append(ord)  
                print('Order placed successfully. Food item in process.\n')
            else:
                print('Insufficient balance. Please recharge your account.\n')
        else:
            print(f'Please check again, "{name}" not found in the menu list.\n')




