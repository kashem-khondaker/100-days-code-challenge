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
        print(f"{product.name} has been added successfully.")


    def view_product(self):
        print("Name\tPrice\tQuantity")
        for product in self.products:
            if product.quantity > 0:    
                print(f"{product.name}\t{product.price}\t{product.quantity}")



    def is_product_available(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name and product.quantity >= quantity:
                return product
        return None



    def stock_correction(self, product_name, quantity):
        product = self.is_product_available(product_name, quantity)
        if product:
            product.quantity -= quantity
            # print(f"Stock updated for {product_name}. Remaining: {product.quantity}")
        # else:
            
            # print(f"Stock update failed: {product_name} has insufficient quantity.")
