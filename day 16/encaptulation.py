class Bank:
    def __init__(self , branch , name , balance ):
        self.__branch = branch # private 
        self.__name = name # private property
        self.__balance = balance # private property
    def deposit(self , amount):
        if amount < 0:
            pass
        else :
            self.__balance += amount # private property
    def withdraw(self , amount):
        if amount < 0 and amount > 50000:
            pass
        else :
            self.__balance -= amount
    def dashboard(self ):
        print(f'Branch : {self.__branch}\nName : {self.__name}\nBalance : {self.__balance}')
    


Kashem = Bank('Islami Bank' , "Kashem Khondaker" , 500)
print(Kashem.dashboard())

        
# try to access 
Kashem.__balance = 0
print(Kashem.dashboard())
    