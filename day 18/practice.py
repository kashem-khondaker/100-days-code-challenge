class Student:
    def __init__(self , name , subjects , marks):
        self.name = name 
        self.subjects = subjects
        self.marks = marks
    def avg(self):
        sum = 0
        avg = 0.0
        for val in self.marks:
            sum += val
        avg = sum / 3
        return avg
    
    # static methods in Python
    @staticmethod
    def show_data():
        pass

# s1 = Student('Kashem' , ['Math' , 'Physics' , 'Chemistry'] , [20,30,40])
# print(s1.avg())

class Account:
    def __init__(self,acc_no , acc_pass):
        self.account_number = acc_no
        self.__account_password = acc_pass
    
acc1 = Account("123" , 'abc')
print(acc1.account_number )
# print(acc1.account_password)

