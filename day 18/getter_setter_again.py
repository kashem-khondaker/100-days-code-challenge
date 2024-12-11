class User:
    def __init__(self , name , user_id , password ):
        self._name = name
        self.__user_id = user_id
        self.__password = password
    
    @property
    def method(self):
        return f'name : {self._name}\nuserID : {self.__user_id}\npassword : {self.__password}'
    
JON = User("JON" , 12321 , 'l321233')
print(JON.method)
