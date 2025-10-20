class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Initially, book is available

class Library:
    def __init__(self):
        self.books = []  # Empty list to store books
        
    def add_book(self, book):
        self.books.append(book)
        
    def show_books(self):
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"Title: {book.title}, Author: {book.author}, Status: {status}")
            
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                    return
        print("Book not found in library.")
    

library = Library()


# Add some books
book1 = Book("Python Basics", "Saqib Ali")
book2 = Book("Learn Java", "Zain-ul-Abidin")
book3 = Book("HTML and CSS", "Saeed Ali")
library.add_book(book1)
library.add_book(book2) 
library.add_book(book3)

library.show_books()

library.borrow_book("Learn Java")
library.show_books()

# book1 = Book("1984", "George Orwell")
# book2 = Book("To Kill a Mockingbird", "Harper Lee")
# print(f"Book: {book1.title}, Author: {book1.author}, Borrowed: {book1.is_borrowed}")
# print(f"Book: {book2.title}, Author: {book2.author}, Borrowed: {book2.is_borrowed}")