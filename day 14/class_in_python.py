# class Calculator:
#     brand = "Casio MS990"
#     def add(self , num1 , num2):
#         return num1 + num2
    
#     def multiple(self , num1 , num2):
#         return num1 * num2
    
#     def divide(self , num1 , num2):
#         return num1 // num2


# my_Calculator = Calculator()

# add_numbers = my_Calculator.add(5,10) # ans = 15
# multiple_numbers = my_Calculator.multiple(9,10) # ans = 90 
# divide_numbers = my_Calculator.divide(25,5) # ans = 5

# print(add_numbers)
# print(multiple_numbers)
# print(divide_numbers)


# class 2
class Student:
    college_name = "Syad Ahammed College"
    
    def __init__(self , name , roll , subjects , department):
        self.name = name
        self.roll = roll
        self.subjects= subjects
        self.department = department

    def show_Student_data(self):
        print(self.name)
        print(self.roll)
        print(self.subjects)
        print(self.department)
    
st1 = Student("Kashem Khondaker" , 15 , ["Calculus" , "Ordinary" , "Programming" , "Physics 3" , "statistic"] , "Math")

print(Student.college_name)
print(st1.show_Student_data())








