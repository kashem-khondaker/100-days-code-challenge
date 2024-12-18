from Inventory import Inventory

class Manager:
    def __init__(self , manager_name , inventory):
        self.manager_name = manager_name
        self.inventory = inventory
        self.products = []
    
    def add_product(self , product):
        self.products.append(product)   
    
    def view_product(self):
        self.inventory.display_all_products()
    
    def search_product(self , id):
        self.inventory.search_product_by_id(id)
    
    def update_stock(self , id , quantity):
        self.inventory.update_product_stock(id , quantity)
    
    def calculate_total(self):
        self.inventory.calculate_total_inventory_value()