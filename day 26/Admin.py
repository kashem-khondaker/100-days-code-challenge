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
        
        
    #-------------------------for customer -----------------------------
    
    
    def add_customer(self , customer):
        self.restaurant.add_customer(customer)
    
    def view_customer(self):
        self.restaurant.view_customer()
   
    
    def remove_customer(self , name):
        self.restaurant.remove_customer(name)
 