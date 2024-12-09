class Shopping :
    cart = [] # static attribute 
    oregin = ' ' # static attribute
    
    def __init__(self , name , location): # instance method
        self.name = name # instance attribute
        self.location = location # instance attribute
    
    def purchase(self , item , price , amount): # instance method
        balance = amount - price # instance attribute 
        print(f'current balance = {balance}\nproduct price = {price}')
    
    @classmethod   
    def showup(self , item): # class method
        print('showup to buy things!!!' , item)
    
Jamuna = Shopping("Jamuna future park" , "motirjil Dhaka")        
# Shopping.purchase('bag' , '3a2b' , 25 , 500) # 4 parameter was given 
# Jamuna.purchase('bug' , 27 , 50 ) # now 3 parameter given

#------------------------------------------------------------
# object_name . class_name -->instance methods call example :
# Jamuna.purchase('bug' , 27 , 50 ) 
 
# class_name . method_name  --> call class methods

Shopping.showup("Longi")
Jamuna.showup("longi")
    
    