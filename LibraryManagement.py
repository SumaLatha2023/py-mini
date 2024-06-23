class Book:
    def __init__ (self, id, title, author, status = True):
        self.id = id
        self.title = title
        self.author = author
        self.status = status

    def __str__(self):
        return f"{self.id} : {self.title} by {self.author} , {'Available' if self.status else 'Unavailable'}"
    
class Manager:
    def __init__ (self):
        self.books = {}

    def add_book(self, book):
        if book.id in self.books:
            print("This Book ID already exists.")
        else:
            self.books[book.id] = book
            print("Book added successfully.")

    def update_book(self, id, title=None, author=None):
        if id in self.books:
            if title:
                self.books[id].title = title
            if author:
                self.books[id].author = author
            print("Book updated successfully.")
        else:       
            print("This Book doesn't exist.")
          

    def delete_book(self, id):
        if id in self.books:
            del self.books[id]
            print("Book deleted successfully.")
        else:
            print("This Book doesn't exist.")

    def list_books(self):
        for book in self.books.values():
            print(book)

    def search_books(self, query):
        result = []
        for book in self.books.values():
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                result.append(book)
        if result:
            for book in result:
                print(book)
        else:
            print("No books found.")

    def check_out_book(self, id):
        if id not in self.books:
            print("Book not found.")
        elif not self.books[id].status:
            print("Book is already checked out.")
        else:
            self.books[id].status = False
            print("Book checked out successfully.")

    def check_in_book(self, id):
        if id not in self.books:
            print("Book not found.")
        elif self.books[id].status:
            print("Book is not checked out.")
        else:
            self.books[id].status = True
            print("Book checked in successfully.")

def main():
    library = Manager()

    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. List all books")
        print("5. Search for books")
        print("6. Check out a book")
        print("7. Check in a book")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(Book(id, title, author))
        elif choice == '2':
            id = input("Enter book ID: ")
            title = input("Enter new title (leave blank to skip): ")
            author = input("Enter new author (leave blank to skip): ")
            library.update_book(id, title, author)
        elif choice == '3':
            id = input("Enter book ID to delete: ")
            library.delete_book(id)
        elif choice == '4':
            library.list_books()
        elif choice == '5':
            query = input("Enter search query (title or author): ")
            library.search_books(query)
        elif choice == '6':
            id = input("Enter book ID to check out: ")
            library.check_out_book(id)
        elif choice == '7':
            id = input("Enter book ID to check in: ")
            library.check_in_book(id)
        elif choice == '8':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()