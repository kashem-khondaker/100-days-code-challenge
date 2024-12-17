from Admin import Admin
from Customer import Customer
from Menu import Menu , Order
from Restaurant import Restaurant

restaurant = input('Please input restaurant name : ')
restaurant = Restaurant(restaurant)


def customer():
    customer = Customer('','','','')
    while(True):
        print('\n1. Create Account .')
        print('2. View Restaurant Menu .')
        print('3. Place an Order .')
        print('4. Check balance .')
        print('5. Add balance to account .')
        print('6. view orders history .')
        print('7. Exit ..\n\n')
        
        y = int(input('Please input number between 1 to 6 : '))
        
        if y == 1:
            
            name = input('name : ')
            email = input('email : ')
            address = input('address : ')
            
            customer = Customer(restaurant , name , email , address)
            restaurant.add_customer(customer)
            
        elif y == 2:
            restaurant.view_menu()
        elif y == 3:
            name = input('input item name : ')
            quantity = int(input('input quantity : '))
            customer.place_order(name , quantity)
        elif y == 4:
            customer.show_balance()
        elif y == 5:
            amount = int(input('how many money do you want to add : '))
            customer.add_funds(amount)
        elif y == 6:
            customer.view_orders()
        elif y == 7:
            print('The end ...\n')
            break
        else : 
            print('Invalid input , Please input number between 1 to 6 ...\n')



def admin():
    while(True):
        print('\n1. Add a new customer account .')
        print('2. View all customer account .')
        print('3. Remove a customer account .')
        print('4. Add menu items .')
        print('5. Remove a menu items .')
        print('6. Update a menu items .')
        print('7. View all menu items .')
        print('8. Exit ..\n\n')
        
        z = int(input('Please input number between 1 to 6 : '))
        
        if z == 1:
            name = input('name : ')
            email = input('email : ')
            address = input('address : ')
            
            customer = Customer(restaurant , name , email , address)
            restaurant.add_customer(customer)
            print(f'{name} added successfully ...\n\n')
        elif z == 2:
            restaurant.view_customer()
        elif z == 3:
            name = input('name : ')
            restaurant.remove_customer(name)
            # print(f'{name} ')
        elif z == 4:
            name = input('name : ')
            price = int(input('price : '))
            quantity = input('quantity : ')
            menu = Menu(name , price , quantity)
            restaurant.add_item_to_menu(menu)
        elif z == 5:
            name = input('name : ')
            restaurant.remove_item_to_menu(name)
        elif z == 6:
            old_name = input('old name : ')
            new_name = input('new name : ')
            new_price = int(input('new price  : '))
            new_quantity = int(input('new quantity  : '))
            restaurant.update_menu_item(old_name , new_name , new_price , new_quantity)
        elif z == 7:
            restaurant.view_menu()
        elif z == 8:
            print('The end ...\n')
            break
        else:
            print("Invalid input ...\n")


while(True):
    print('1. Customer .')
    print('2. Admin .')
    print('3. Exit .\n\n')
    
    x = int(input('please input number between 1 to 3 : '))
    
    if x == 1:
        customer()
    elif x == 2:
        admin()
    elif x == 3:
        print('The End ...\n')
        break
    else:
        print('Invalid input , Please input number between 1 to 3 !..\n')
        
    