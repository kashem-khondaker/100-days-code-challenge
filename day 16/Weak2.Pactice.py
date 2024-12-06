# class Product:
#     # list = []
#     def __init__(self , brand , product_id, name , quantity , price):
#         self.brand = brand
#         self.product_id = product_id
#         self.product_name = name 
#         self.quantity = quantity
#         self.price = price  
    
#     def __str__(self):
#         return f"Brand : {self.brand} \nProduct id : {self.product_id} \nProduct Name : {self.product_name} \nQuantity : {self.quantity} \nPrice : {self.price} taka"


# class Shop(Product):
    
#     def __init__(self, brand, product_id, name, quantity, price):
#         super().__init__(brand, product_id, name, quantity, price)
    
#     # def add_product(self , brand , product_id , name , quantity , price):
#     #     super().__init__(brand , product_id , name , quantity , price)
    
#     def buy_product(self , brand , name , quantity , price):
#         if self.product_name == name and self.brand == brand :
#             #product available 
#             # how many available ?
#             if self.quantity >= quantity:
#                 # product available quantity will be (-)
#                 # if product = 0 delete product 
#                 pass
#             else:
#                 # I have only this product quantity
#                 pass
            
#         else:
#             #product not available
#             pass

# product1 = Product("Iphone" , 111 , "Iphone 14 " , 1 , 18000)

# # product1.add_product()

# print(product1)
# # product2 = Product("Banana", 0.5, 20)

# # how many issue have this code ?
# """

# Your code structure for Product and Shop is a good starting point, but there are several issues and areas for improvement. Let's evaluate it step by step in the context of the requirements from your earlier question and refine it to satisfy the requirements fully.

# Key Observations:
# Inheritance Misuse:

# The Shop class inherits from Product, but it does not make logical sense for a Shop to be a Product. A Shop should manage a collection of Product instances, not be a Product itself.
# Instead of inheritance, composition (using a list of Product objects within the Shop) would be more appropriate.
# add_product Method:

# The add_product method in Shop overwrites the existing product attributes because it directly calls the Product initializer via super().__init__. This is incorrect behavior; it should instead add products to a collection (e.g., a list or dictionary) within the Shop.
# buy_product Method:

# The method partially implements the logic for buying a product, but it lacks a proper structure to manage multiple products. A dictionary of products, keyed by a unique identifier (e.g., product_id or name), would make this implementation more effective.
# Unnecessary Arguments in Shop:

# The Shop initializer mirrors the Product initializer, which is redundant. A Shop should not have attributes like brand or product_id.


# """