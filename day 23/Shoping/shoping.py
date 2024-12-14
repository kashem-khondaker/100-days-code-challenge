class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self, email, password):
        if self.email == email and self.password == password:
            return True
        return False


class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.orders = []  # Track orders placed by customer


    def view_products(self, products):
        print("Available products:")
        for product in products:
            if product.is_in_stock():
                print(f"{product.product_name} - ${product.price} - {product.stock} in stock")
            else:
                print(f"{product.product_name} - Out of stock")


    def place_order(self, product_name, quantity, products):
        for product in products:
            if product.product_name == product_name and product.is_in_stock() and product.stock >= quantity:
                total_price = product.price * quantity
                product.reduce_stock(quantity)
                self.orders.append(Order(self.email, product_name, quantity, total_price))
                print(f"Order placed for {quantity} {product_name}(s) at ${total_price}.")
                return
        print(f"Unable to place order. Either product is out of stock or invalid quantity.")


class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.products = []  # Track products added by the seller


    def add_product(self, product_name, price, stock):
        if stock < 0:
            print("Stock cannot be negative.")
            return
        new_product = Product(product_name, price, stock, self.email)
        self.products.append(new_product)
        print(f"Product '{product_name}' added successfully.")



    def view_products(self):
        if not self.products:
            print("No products added yet.")
            return
        print("Your Products:")
        for product in self.products:
            print(f"{product.product_name} - ${product.price} - {product.stock} in stock")


class Product:
    def __init__(self, product_name, price, stock, seller_email):
        self.product_name = product_name
        self.price = price
        self.stock = stock
        self.seller_email = seller_email



    def reduce_stock(self, quantity):
        self.stock -= quantity



    def is_in_stock(self):
        return self.stock > 0


class Order:
    def __init__(self, customer_email, product_name, quantity, total_price):
        self.customer_email = customer_email
        self.product_name = product_name
        self.quantity = quantity
        self.total_price = total_price


# Global list to store products
products = []

# Sample run of program
def main():
    print("Welcome to the E-Shopping App!")
    users = {}

    while True:
        print("\nAre you a:")
        print("1. Customer")
        print("2. Seller")
        print("3. Exit")
        user_type = input("Enter choice (1/2/3): ")


        if user_type == '1':  # Customer
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if email in users and isinstance(users[email], Customer) and users[email].login(email, password):
                customer = users[email]
            else:
                print("Invalid credentials. Please try again.")
                continue

            while True:
                print("\nCustomer Menu:")
                print("1. View All Products")
                print("2. Place Order")
                print("3. Logout")
                choice = input("Enter choice: ")

                if choice == '1':
                    customer.view_products(products)
                elif choice == '2':
                    product_name = input("Enter product name to order: ")
                    quantity = int(input("Enter quantity: "))
                    customer.place_order(product_name, quantity, products)
                elif choice == '3':
                    break
                else:
                    print("Invalid choice.")
        
        elif user_type == '2':  # Seller
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if email in users and isinstance(users[email], Seller) and users[email].login(email, password):
                seller = users[email]
            else:
                print("Invalid credentials. Please try again.")
                continue

            while True:
                print("\nSeller Menu:")
                print("1. Add Product")
                print("2. View My Products")
                print("3. Logout")
                choice = input("Enter choice: ")

                if choice == '1':
                    product_name = input("Enter product name: ")
                    price = float(input("Enter product price: "))
                    stock = int(input("Enter stock quantity: "))
                    seller.add_product(product_name, price, stock)
                elif choice == '2':
                    seller.view_products()
                elif choice == '3':
                    break
                else:
                    print("Invalid choice.")

        elif user_type == '3':  # Exit
            print("Exiting the app...")
            break
        else:
            print("Invalid choice.")


# Initialize some users
user1 = Customer('customer1@example.com', 'password123')
user2 = Seller('seller1@example.com', 'password123')

# Save users in a dictionary (email as the key)


# Run the main program
main()
