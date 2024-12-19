class Inventory:
    def __init__(self , name ):
        self.name = name
        self.products = []

    def display_all_products(self):
        for product in self.products:
            print(f'{product.product_id}\t{product.name}\t{product.quantity}\t{product.price}')
                
    def search_product_by_id(self , id):
        for product in self.products:
            if product.product_id == id:
                print('Product fund ...')
                return product
        print('Product not found ...')
        return None
    
    def update_product_stock(self ,id , quantity): 
        product = self.search_product_by_id(id)
        if product:
            if quantity > 0:
                product.quantity += quantity
                print(f'{quantity} - Product added ')
            else:
                product.quantity += quantity
                print(f'{quantity} product removed !')
        else:
            print('Invalid product id .')
    
    def calculate_total_inventory_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.quantity * product.price
        print(f'Total value of this inventory {total_value}')
        return total_value