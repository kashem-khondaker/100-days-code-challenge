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

        
        
    #-------------------------for customer -----------------------------
    
    
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




