from abc import ABC
class User:
    def __init__(self , name , phone , email , address):
        self.name = name 
        self.email = email
        self.address = address
        self.phone = phone


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = None
        
    def view_menu_item(self , restaurant):
        restaurant.menu.view_menu_item()
        
        
    def add_to_cart(self , restaurant , item_name):
        item = restaurant.menu.find_item(item_name)
        if item:
            pass
        else:
            print(f'{item_name} not founded')
    
    
    def view_cart(self):
        print('**view cart**')
        print('name\t\tprice\t\tquantity')
    

#--------------------------------------------------


class Employee(User):
    def __init__(self , name , phone , email , address , age , designation , salary):
        super().__init__(name , phone , email , address)
        self.age = age 
        self.designation = designation
        self.salary = salary
        
        
#-----------------------------------------------------        


class Admin(User):
    def __init__(self, name , phone , email , address  ):
        super().__init__( name , phone , email , address)
         
         
    def add_employee(self , restaurant , employee):
        restaurant.add_employee(employee)


    def view_employee(self , restaurant):
        restaurant.view_employee()
        
        
    def add_new_menu_item(self , restaurant , item):
        restaurant.menu.add_menu_item(item)


    def view_menu_item(self , restaurant):
        restaurant.menu.view_menu_item()

        
    def remove_menu_item(self , restaurant , item):
        item = restaurant.menu.find_item(item)
        if item :
            restaurant.menu.remove_item(item)
            print(f'{item} remove successfully')
        else:
            print(f'{item} not found')


#------------------------------------------------------------


class Restaurant:
    def __init__(self , name):
        self.name = name
        self.employees = [] # this is database for now
        self.menu = Menu()
    
    def add_employee(self, employee): # ---> employee ta koi teke astese ?
        self.employees.append(employee)

    
    def view_employee(self):
        print('Employee list')
        for emp in self.employees:
            print(emp.name  , emp.email , emp.phone , emp.salary )
            
            
#----------------------------------------------------------


class Menu:
    def __init__(self):
        self.items = [] # items er database 

    
    def add_menu_item(self , item):
        self.items.append(item)

    
    def find_item(self , item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    
    def remove_item(self , item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item deleted ")
        else:
            print("Item not found!")
    
            
    def view_menu_item(self):
        print('*** menu items ***')
        print('name\tprice\tquantity')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
    
    
#-------------------------------------------------------------------    


class FoodItem:
    def __init__(self , name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        

mn = Menu()
item = FoodItem('vat' , 20 , 100)
mn.add_menu_item(item)
mn.view_menu_item()



