from Inventory import Inventory
from product import Product
from management import Manager

name = input('please input inventory name : ')
inventory = Inventory(name)

while(True):
    print('\n1. Add a new product')
    print('2. View all products')
    print('3. Search a product by id .')
    print('4. Update stock increase value (+) and decrease value (-).')
    print('5. Calculate total inventory value .\n')
    print('6. Exit .')
    
    choice = int(input('please input number 1 to 6 : '))
    
    if choice == 1:
        id =   int(input('id : '))
        name = input('name : ')
        price = int(input('price : '))
        quantity = int(input('quantity : '))
        product = Product(product_id=id , name=name , quantity=quantity , price=price)
    elif choice == 2:
        inventory.display_all_products()
    elif choice == 3:
        id = int(input('id : '))
        inventory.search_product_by_id(id)
    elif choice == 4:
        id = int(input('id : '))
        quantity = int(input('quantity : '))
        inventory.update_product_stock(id , quantity)
    elif choice == 5:
        inventory.calculate_total_inventory_value()
    elif choice == 6:
        print('The End ...!')
        break
    