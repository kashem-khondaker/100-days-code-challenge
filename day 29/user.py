from abc import ABC , abstractmethod
from book import Book
from library import Library


class User(ABC):
    def __init__(self , user_name , id):
        self.name = user_name
        self.id = id
    
class Admin(User):
    def __init__(self, user_name, id):
        super().__init__(user_name, id)
    
    def add_books(self , library , book):
            library.books.append(book)
    