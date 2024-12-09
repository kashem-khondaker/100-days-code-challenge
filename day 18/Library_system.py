class Library:
    book_list = []
    def __init__(self , book_id , title , author , availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability
        
        Library.book_list.append(self)

    def borrow_book(self):
        pass
    def return_book(self):
        pass
    def view_book_info(self):
        pass
    def menu_system(self):
        # 1 . view all books
        # 2 . Borrow book
        # 3 . Return book
        # 4 . Exit
        pass
    def error_handling(self):
        """
        Implement error handling for:
        - Invalid book ID when borrowing or returning a book.
        - Trying to borrow a book that is already borrowed.
        - Trying to return a book that is not borrowed.

        """
        pass

# Data privacy : 
"""
Make the attributes (such as book_id, title, author, availability) 
as protected/private as possible using Python’s class mechanisms. 
This will ensure that these attributes cannot be accessed directly outside the class.
"""




College_library = Library(123412,"Hero Programmer" , "JON" , 20)
print(College_library.book_list[0])
