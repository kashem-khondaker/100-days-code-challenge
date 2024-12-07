# overloading and overriding 
class Person:
    def __init__(self , name , age , height , weight):
        self.name = name
        self.age = age 
        self.height = height
        self.weight = weight
        
    def eat(self):
        print(f' vat mango polau korma')
    
    # force to override this things must be there in cricket
    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight , team):
        self.team = team
        super().__init__(name, age, height, weight)
    
    def eat(self):
        print('Vegetables')
        
    def exercise(self):
        # return super().exercise()
        print('Please exercise every day !')
    def __add__(self, other):
        return self.age + other.age      
    def __mul__(self , other):
        return self.age * other.age
    





sakib = Cricketer('sakib' , 38 , 68 , 91 , 'BD')

sakib.eat() # --> cricketer hit in Person and then print eat method
sakib.eat() # -->after eat method implement in cricket , it override person's eat


# override 
sakib.exercise() # give me an error raise NotImplementedError 
sakib.exercise() # after make method exercise in cricket error is fixed

mushi = Cricketer('mushi' , 36 ,65,78,"BD")


# want to know about over load 
print(5 + 5)
print('kashem ' + 'khondaker') # attach 2 strings 
print([1,2,3,4,5] + [6,7,8,9,10]) # attach 2 list 

# print(sakib + mushi) # give an error unsupported operated type 
print(sakib + mushi) # when i call sakib + mushi it's internaly called __add__ and give that result 
