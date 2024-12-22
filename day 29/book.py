class Book:
    def __init__(self , title , author , ISBN , genre , total_copy):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.total_copy = total_copy
        
    def display_info(self):
        print(f'Title -{self.title}\tAuthor -{self.author}\tISBN -{self.ISBN}\tGenre -{self.genre}\tTotal copy -{self.total_copy}\n')
        
