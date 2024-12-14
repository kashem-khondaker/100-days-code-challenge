class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class ProductManager:
    def __init__(self):
        self.products = []
        

    def add_product(self, product):
        self.products.append(product)
        


    def view_product(self):
        print(f'Name\tPrice\tQuantity')
        for product in self.products:
            if product.quantity != 0:    
                print(f'{product.name}\t{product.price}\t{product.quantity}')
            


    def is_product_available(self, product, quantity):
        return product.quantity >= quantity


    def stock_correction(self, product, quantity):
        # Debug print to track method execution  
        if self.is_product_available(product, quantity):
            product.quantity -= quantity
            print("Stock successfully updated.\n")
        else:
            print("\nStock correction failed. Insufficient quantity.")
        
        
