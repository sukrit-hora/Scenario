class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def category(self):
        if self.price >= 1000:
            return "Premium"
        else:
            return "Standard"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Price:", book.price)
            print("Category:", book.category())
            print("------------------------")


library = Library()

book1 = Book(101, "Python Programming", "John Smith", 1200)
book2 = Book(102, "Data Structures", "Robert Brown", 800)
book3 = Book(103, "Database Systems", "James Lee", 1500)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()