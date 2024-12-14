from user import User

class Account:
    def __init__(self , name , phone , email , password):
        self.name = name 
        self.phone = phone
        self.email = email
        self.password = password

class CreateAccount:
    def __init__(self):
        self.accounts = []
        self.account_ = Account()
    
    def create(self , account):
        self.accounts.append(account)
        
    def login(self , email , password):
        return self.account_.email == email and self.account_.password == password
             
    
    