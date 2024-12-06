class Mango_People:
    def __init__(self , name , age , nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    
class Bamboo_eaters(Mango_People):
    def __init__(self, name, age, nationality , roll , class_ ):
        self.roll = roll
        self.class_ = class_
        super().__init__(name, age, nationality)

class Bamboo_giver(Mango_People):
    def __init__(self, name, age, nationality , subject ):
        self.subject = subject
        super().__init__(name, age, nationality)

class Head_Bamboo_giver(Bamboo_giver):
    def __init__(self, name, age, nationality, subject , school):
        self.school = school
        super().__init__(name, age, nationality, subject)


