from product import Product, ProductManager

class Seller:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.product_manager = ProductManager()
       
    
    def add_product(self, product_name, price, quantity):
        product = Product(product_name, int(price), int(quantity))
        self.product_manager.add_product(product)
        
    
    def view_product(self):
        self.product_manager.view_product()
