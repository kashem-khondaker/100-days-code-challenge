class Library:
    book_list = []

    @classmethod
    def entry_book(self, book):
        self.book_list.append(book)
        
    @classmethod
    def print_book_list(cls):
        print("\nBook List:")
        for book in cls.book_list:
            print(f"ID: {book._book_id}, Title: '{book._title}', Author: {book._author}, Availability: {'Available' if book._availability else 'Not Available'}")



class Book(Library):
    def __init__(self, book_id, title, author):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._availability = True
        Library.entry_book(self)

    def borrow_book(self):
        if self._availability:
            self._availability = False
            print(f"Book '{self._title}' borrowed successfully.")
        else:
            print("Book is not available for borrowing.")

    def return_book(self):
        if  self._availability == False:
            self._availability = True
            print(f"Book '{self._title}' returned successfully.")
        else:
            print("Book is not borrowed.")

    def view_book_info(self):
        for book in self.book_list:
            print(f'ID : {book.book_id} ')



book1 = Book(1, "Python programming", "JON")
book2 = Book(2, "Python for beginner", "Jane Austen")
book3 = Book(3, "Basic to Advanced Python", "Harper Lee")

# Menu System
while True:
    print("\nLibrary Management System")
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            Library.view_all_books()
        elif choice == 2:
            book_id = int(input("Please input book ID: "))
            Library.borrow_book_by_id(book_id)
        elif choice == 3:
            book_id = int(input("Please input book ID: "))
            Library.return_book_by_id(book_id)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
