from abc import ABC
from product import Product , ProductManager

class User(ABC):
    def __init__(self , name , phone , email , password):
        self.name = name 
        self.phone = phone
        self.email = email
        self.password = password

    
    
# class Customer(User):
    def __init__(self, email, password ):
        super().__init__(email, password)
        self.cart = {}
        self.product_manager = ProductManager()
        
        
    def view_product(self ):
        self.product_manager.view_product()
        
        
    def buy_product(self , product , quantity):
        
        is_available = self.product_manager.is_product_available(product,quantity)
        if is_available is True:
            if product in self.cart:
                self.cart[product] += quantity
            else : 
                self.cart[product] = quantity
            self.product_manager.stock_correction(product , quantity)
        else : 
            print(f'Not enough stack for {product.name}')
    
    
    
    def buying_history(self):
        for key , value in self.cart.items():
            print(key , value)
        
        
# class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.product_manager = ProductManager()
       
    def add_product(self , product_name , price , quantity):
        product1 = Product(product_name , price , quantity)
        self.product_manager.add_product(product1)
        print(f'{product_name} added successfully')