from user import User
from product import  ProductManager


class Customer(User):
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
        total = 0
        for product , quantity in self.cart.items():
            total += product.price * quantity 
            print(product , quantity)
        print(f'Total Amount : {total}')
        
        
    def paybill(self):
        self.buying_history()
        print('Bill paid successfully ')
        self.cart = {}
    