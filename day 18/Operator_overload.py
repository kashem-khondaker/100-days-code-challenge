class Person :
    def __init__(self, name , height , weight):
        self.name = name 
        self.height = height
        self.weight = weight
        
    def eat(self):
        print('vat manshow , polau')
    
    def exercise(self):
        # print('Good for body')
        
        #force to implement exercise
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, height, weight , team):
        self.team = team
        super().__init__(name, height, weight)
    # override
    def eat(self):
        print("vegetable")
    #
    def exercise(self):
        print('Good for body')
    
sakib = Cricketer('Sakib',5.6 , 56 ,"BD")
sakib.eat()
sakib.exercise()        