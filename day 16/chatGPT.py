class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} \n(Price: ${self.price} \nQuantity: {self.quantity})"


class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product
        print(f"Added {product.name} to the shop.")

    def buy_product(self, product_name, quantity):
        if product_name in self.products:
            product = self.products[product_name]
            if product.quantity >= quantity:
                product.quantity -= quantity
                print(f"Congratulations! You successfully bought {quantity} {product_name}(s).")
                if product.quantity == 0:
                    del self.products[product_name]
            else:
                print(f"Sorry, only {product.quantity} {product_name}(s) are available.")
        else:
            print(f"Sorry, {product_name} is not available in the shop.")

    def display_products(self):
        if self.products:
            print("Available products in the shop:")
            for product in self.products.values():
                print(product)
        else:
            print("The shop is currently empty.")


# Example usage
shop = Shop()

# Adding products
product1 = Product("Apple", 1.5, 10)
product2 = Product("Banana", 0.5, 20)

shop.add_product(product1)
shop.add_product(product2)

# Display available products
shop.display_products()

# Buying products
shop.buy_product("Apple", 5)
shop.buy_product("Apple", 6)  # Testing insufficient stock
shop.buy_product("Orange", 2)  # Testing unavailable product

# Display available products after buying
shop.display_products()
