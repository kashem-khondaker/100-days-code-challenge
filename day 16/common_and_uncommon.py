# base class , parent class , common attribute + functionality
# derived class , child class , uncommon attribute + functionality

class Device:
    def __init__(self , brand , price , color , origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    
    def run(self):
        return f'Running device : {self.brand}'

class Laptop:
    def __init__(self , memory , ssd , mother_board , display):
        self.memory = memory
        self.ssd = ssd
        self.mother_board = mother_board
        self.display = display
        
    def coding(self):
        return f'learning Python and OOP by Jhonkar vai'

class Phone:
    def __init__(self,processor , camera , charger , display):
        self.processor = processor
        self.camera = camera
        self.charger = charger
        self.display = display
    
    def play_game(self):
        return f'We can play PUBG'

my_Phone = Phone("Snapdragon" , "120 px" , True , 6.9)
print(my_Phone.processor , my_Phone.camera)
