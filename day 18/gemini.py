class Library:
    book_list = []

    @classmethod
    def entry_book(self, book):
        self.book_list.append(book)

    @classmethod
    def view_all_books(self):
        if not self.book_list:
            print("\nNo books available in the library.")
        else:
            for book in self.book_list:
                book.view_book_info()
                print()

    @classmethod
    def borrow_book_by_id(self, book_id):
        for book in self.book_list:
            if book._book_id == book_id:
                book.borrow_book()
                return
        print("Invalid book ID.")

    @classmethod
    def return_book_by_id(self, book_id):
        for book in self.book_list:
            if book._book_id == book_id:
                book.return_book()
                return
        print("Invalid book ID or book not borrowed.")


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
        print(f"Book ID: {self._book_id}")
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Availability: {'Available' if self._availability else 'Borrowed'}")



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
