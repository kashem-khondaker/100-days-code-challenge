class Product:
    def __init__(self, brand, product_id, name, quantity, price):
        self.brand = brand
        self.product_id = product_id
        self.product_name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return (f"Brand: {self.brand}\n"
                f"Product ID: {self.product_id}\n"
                f"Product Name: {self.product_name}\n"
                f"Quantity: {self.quantity}\n"
                f"Price: {self.price} taka")


class Shop:
    def __init__(self):
        self.products = {}  # Store products as a dictionary with product_id as the key

    def add_product(self, product):
        if product.product_id in self.products:
            self.products[product.product_id].quantity += product.quantity
            print(f"Updated quantity for {product.product_name}. New quantity: {self.products[product.product_id].quantity}")
        else:
            self.products[product.product_id] = product
            print(f"Added {product.product_name} to the shop.")

    def buy_product(self, product_id, quantity):
        if product_id in self.products:
            product = self.products[product_id]
            if product.quantity >= quantity:
                product.quantity -= quantity
                print(f"Congratulations! You bought {quantity} {product.product_name}(s).")
                if product.quantity == 0:
                    del self.products[product_id]  # Remove the product if quantity reaches 0
                    print(f"{product.product_name} is now out of stock.")
            else:
                print(f"Insufficient stock. Only {product.quantity} {product.product_name}(s) are available.")
        else:
            print("Product not found in the shop.")

    def display_products(self):
        if self.products:
            print("Products available in the shop:")
            for product in self.products.values():
                print(product)
                print("-" * 30)
        else:
            print("The shop is empty.")


# Example Usage
shop = Shop()

# Adding products
product1 = Product("Iphone", 20112, "Iphone 14", 10, 18000)
product2 = Product("Samsung", 20113, "Galaxy S22", 5, 15000)

shop.add_product(product1)
shop.add_product(product2)

# Display available products
shop.display_products()

# Buying a product
shop.buy_product(20112, 3)  # Buy 3 iPhones
shop.buy_product(20112, 8)  # Test insufficient stock
shop.buy_product(20114, 1)  # Test product not in shop

# Display products after purchase
shop.display_products()
