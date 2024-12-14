from account import Account, CreateAccount
from Customer import Customer
from product import ProductManager
from Seller import Seller

def main():
    account_manager = CreateAccount()
    customer = Customer()
    seller = Seller(email="seller@example.com", password="password")
    
    while True:
        print("\n1. Create Account")
        print("2. View Products")
        print("3. Buy Products")
        print("4. Log in to Account")
        print("5. Add Product (Seller)")
        print("6. Pay Bill")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter your name: ")
            phone = input("Enter your phone: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            
            account = Account(name, phone, email, password)
            account_manager.create(account)
        
        elif choice == 2:
            customer.view_product()
        
        elif choice == 3:
            product_name = input("Enter product name: ")
            quantity = input("Enter quantity: ")
            customer.buy_product(product_name, quantity)
        
        elif choice == 4:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            account_manager.login(email, password)
        
        elif choice == 5:
            product_name = input("Enter product name: ")
            price = input("Enter product price: ")
            quantity = input("Enter product quantity: ")
            seller.add_product(product_name, price, quantity)
        
        elif choice == 6:
            customer.paybill()
        
        elif choice == 7:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
