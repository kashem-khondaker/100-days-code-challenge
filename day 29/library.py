class Library:
    def __init__(self):
        self.books = []
        
    def view_all_books(self):
        for book in self.books:
            print(f'Title -{book.title}\tAuthor -{book.author}\tISBN -{book.ISBN}\tGenre -{book.genre}\tTotal copy -{book.total_copy}\n')
    
    def search_book_by_author(self , author):
        for book in self.books:
            if book.author == author:
                print(f'Title -{book.title}\tAuthor -{book.author}\tISBN -{book.ISBN}\tGenre -{book.genre}\tTotal copy -{book.total_copy}\n')
            else:
                print('Book not find !!')
    
        
                