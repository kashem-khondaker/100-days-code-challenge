from user import User
from product import Product , ProductManager

class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.product_manager = ProductManager()
       
       
    def add_product(self , product_name , price , quantity):
        product1 = Product(product_name , price , quantity)
        self.product_manager.add_product(product1)
        print(f'{product_name} added successfully')
        
        
    def view_product(self):
        self.product_manager.view_product()
        
