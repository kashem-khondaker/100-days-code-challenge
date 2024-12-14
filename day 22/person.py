import random
from school import School
from ClassRoom import ClassRoom

class Person:
    def __init__(self , name):
        self.name = name
        

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        
    def evaluate_exam(self):
        return random.randint(25 , 100)

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        # self.classroom = ClassRoom
        self.classroom = classroom   # find one error
        self.__id = None
        self.grade = None
        self.marks = {}
        self.subject_grade = {}
        
        
    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade)
            sum += point
        if sum == 0:
            gpa = 0.00
            self.grade = 'F'
        else:
            gpa = sum / len(self.subject_grade)
            self.grade = School.value_to_grade(gpa)
        return f"{self.name} final grade : {self.grade} \n GPA : {gpa}"
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self , value):
        self.__id = value
        
    
        
        
    
        