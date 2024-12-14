from product import ProductManager

class Customer:
    def __init__(self):
        self.cart = {}
        self.product_manager = ProductManager()

        
    def view_product(self):
        self.product_manager.view_product()
        

    def buy_product(self, product_name, quantity):
        quantity = int(quantity)
        product = self.product_manager.is_product_available(product_name, quantity)
        if product:
            if product.name in self.cart:
                self.cart[product.name] += quantity
            else: 
                self.cart[product.name] = quantity

            self.product_manager.stock_correction(product_name, quantity)
            print(f"{quantity} units of {product.name} added to cart.")
        else: 
            print(f"Not enough stock for {product_name}.")
    

    def buying_history(self):
        total = 0
        print("\n--- Your Cart ---")
        for product_name, quantity in self.cart.items():
            for product in self.product_manager.products:
                if product.name == product_name:
                    total += product.price * quantity
                    print(f"{product_name} - {quantity} units")
        print(f"Total Amount: {total}\n")
        

    def paybill(self):
        self.buying_history()
        print("Bill paid successfully.")
        self.cart = {}
