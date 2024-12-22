from abc import ABC

class Menu:
    def __init__(self , name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
class Order:
    def __init__(self,name , price , quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity
        
class Restaurant:
    def __init__(self , name):
        self.name = name
        self.menus = []
        self.customers = []
    
    def add_item_to_menu(self , menu):
        self.menus.append(menu)
        print('Add item successfully .\n\n')
    
    def view_menu(self):
        print(f'Name\tPrice\tQuantity\n')
        for menu in self.menus:
            print(f'{menu.name}\t{menu.price}\t{menu.quantity}')
        print('\n')
    
    def remove_item_to_menu(self , name):
        for menu in self.menus:
            if menu.name.lower() == name.lower():
                self.menus.remove(menu)
                print(f'{name} deleted ..\n')
                return            
        print(f'{name} not found \n')
    
    
    def find_menu_by_name(self , name):
        for menu in self.menus:
            if menu.name.lower() == name.lower():
                return menu
        return None
    
    
    def update_menu_item(self, old_name, new_name, new_price, new_quantity):
        menu = self.find_menu_by_name(old_name)
        if menu:  
            for menu_ in self.menus:
                if menu_.name.lower() == old_name.lower():
                    menu_.name = new_name
                    menu_.price = new_price
                    menu_.quantity = new_quantity
            print('Update successful...\n')
        else:
            print(f'{old_name} does not exist!\n')

        
    def add_customer(self , customer):
        self.customers.append(customer)
        print('Customer added successfully ..\n')
    
    def view_customer(self):
        for customer in self.customers:
            print(f'\n{customer.name}\t{customer.address}\t{customer.email}')
        print('\n\n')
            
        
    def find_customer_by_name(self, name):
        for customer in self.customers:
            if customer.name.lower() == name.lower():
                return customer  
        return None 
    
    def remove_customer(self, name):
        customer = self.find_customer_by_name(name)
        if customer: 
            self.customers.remove(customer)
            print(f'{name} deleted...\n')
        else:
            print(f'{name} does not exist.\n')


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

class Admin:
    def __init__(self , restaurant):
        self.restaurant = restaurant
        
    def add_item_to_menu(self , menu):
        self.restaurant.add_item_to_menu(menu)
    
    def view_menu(self):
        self.restaurant.view_menu()
    
    def remove_item_to_menu(self , name):
        self.restaurant.remove_item_to_menu(name)
    
    def update_menu_item(self , old_name , new_name , new_price , new_quantity):
        self.restaurant.update_menu_item(old_name , new_name , new_price , new_quantity)
        
    def add_customer(self , customer):
        self.restaurant.add_customer(customer)
    
    def view_customer(self):
        self.restaurant.view_customer()
    
    def remove_customer(self , name):
        self.restaurant.remove_customer(name)


restaurant = input('Please input restaurant name : ')
restaurant = Restaurant(restaurant)


def customer():
    customer = Customer(restaurant,'','','')
    
    while(True):
        print('\n1. Create Account .')
        print('2. View Restaurant Menu .')
        print('3. Place an Order .')
        print('4. Check balance .')
        print('5. Add balance to account .')
        print('6. view orders history .')
        print('7. Exit ..\n\n')
        
        y = int(input('Please input number between 1 to 6 : '))
        
        if y == 1:
            
            name = input('name : ')
            email = input('email : ')
            address = input('address : ')
            
            customer = Customer(restaurant , name , email , address)
            restaurant.add_customer(customer)
            
        elif y == 2:
            restaurant.view_menu()
        
        elif y == 3:
            name = input('input item name : ')
            quantity = int(input('input quantity : '))
            customer.place_order(name , quantity)
        
        elif y == 4:
            customer.show_balance()
        
        elif y == 5:
            amount = int(input('how many money do you want to add : '))
            customer.add_funds(amount)
        
        elif y == 6:
            customer.view_orders()
        
        elif y == 7:
            print('The end ...\n')
            break
        else : 
            print('Invalid input , Please input number between 1 to 6 ...\n')



def admin():
    while(True):
        print('\n1. Add a new customer account .')
        print('2. View all customer account .')
        print('3. Remove a customer account .')
        print('4. Add menu items .')
        print('5. Remove a menu items .')
        print('6. Update a menu items .')
        print('7. View all menu items .')
        print('8. Exit ..\n\n')
        
        z = int(input('Please input number between 1 to 6 : '))
        
        if z == 1:
            name = input('name : ')
            email = input('email : ')
            address = input('address : ')
            
            customer = Customer(restaurant , name , email , address)
            restaurant.add_customer(customer)
        
        elif z == 2:
            restaurant.view_customer()
        
        elif z == 3:
            name = input('name : ')
            restaurant.remove_customer(name)
        
        elif z == 4:
            name = input('name : ')
            price = int(input('price : '))
            quantity = input('quantity : ')
            menu = Menu(name , price , quantity)
            restaurant.add_item_to_menu(menu)
        
        elif z == 5:
            name = input('name : ')
            restaurant.remove_item_to_menu(name)
        
        elif z == 6:
            old_name = input('old name : ')
            new_name = input('new name : ')
            new_price = int(input('new price  : '))
            new_quantity = int(input('new quantity  : '))
            restaurant.update_menu_item(old_name , new_name , new_price , new_quantity)
        
        elif z == 7:
            restaurant.view_menu()
        
        elif z == 8:
            print('The end ...\n')
            break
        else:
            print("Invalid input ...\n")

while(True):
    print('1. Customer .')
    print('2. Admin .')
    print('3. Exit .\n\n')
    
    x = int(input('please input number between 1 to 3 : '))
    
    if x == 1:
        customer()
    elif x == 2:
        admin()
    elif x == 3:
        print('The End ...\n')
        break
    else:
        print('Invalid input , Please input number between 1 to 3 !..\n')
        
    