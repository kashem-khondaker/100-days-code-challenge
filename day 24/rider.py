from abc import ABC 

class User(ABC):
    def __init__(self , name , email , nid ):
        self.name = name 
        self.email = email
        self.nid = nid
        self.wallet = 0
        
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, nid , current_location , initial_amount):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = initial_amount
        self.current_ride = None
        