# oop -> Object Oriented Programming 
class Company:
    def __init__(self , name ):
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.manager = []
        self.supervisors = []
        self.fare = []

class Drivers:
    def __init__(self , name , license , age):
        self.name = name
        self.license = license
        self.age = age
        
class Counters:
    def __init__(self):
        pass
    def purchase_a_ticket(self , start , destination ):
        pass
 
class Passengers:
    pass

class Supervisors:
    pass


# drivers
red_mia = Drivers('a','123',32)
