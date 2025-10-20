# -------------------------
# Book Class
# -------------------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Initially, book is available


# -------------------------
# Member Class
# -------------------------
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # List to track borrowed books

    def borrow_book(self, library, title):
        for book in library.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    book.is_borrowed = True
                    self.borrowed_books.append(book)
                    print(f"{self.name} borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                    return
        print("Book not found in library.")

    def return_book(self, library, title):
        for book in self.borrowed_books:
            if book.title.lower() == title.lower():
                book.is_borrowed = False
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book.title}'.")
                return
        print(f"{self.name} did not borrow '{title}'.")

    def show_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has not borrowed any books.")
        else:
            print(f"Books borrowed by {self.name}:")
            for book in self.borrowed_books:
                print(f"- {book.title}")


# -------------------------
# Library Class
# -------------------------
class Library:
    def __init__(self):
        self.books = []  # Empty list to store books

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def show_books(self):
        print("\n📚 Books in Library:")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"- {book.title} by {book.author} ({status})")


# -------------------------
# Main Program
# -------------------------

# Create Library
library = Library()

# Add Books
book1 = Book("Python Basics", "Saqib Ali")
book2 = Book("Learn Java", "Zain-ul-Abidin")
book3 = Book("HTML and CSS", "Saeed Ali")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Create Members
member1 = Member("Saeed")
member2 = Member("Ali")

# Show all books
library.show_books()

# Member actions
member1.borrow_book(library, "Learn Java")
library.show_books()

member1.show_borrowed_books()

member1.return_book(library, "Learn Java")
library.show_books()
