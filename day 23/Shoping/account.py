class Account:
    def __init__(self, name, phone, email, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password



class CreateAccount:
    def __init__(self):
        self.accounts = []  
    

    def create(self, account):
        if isinstance(account, Account):  
            self.accounts.append(account)
            print("Account created successfully.")
        else:
            print("Invalid account object.")


    def login(self, email, password):
        for account in self.accounts:
            if account.email == email and account.password == password:
                print("Login successful!")
                return True
        print("Invalid email or password.")
        return False  