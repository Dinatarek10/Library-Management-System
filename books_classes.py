class Book:
    def __init__(self, book_id, name, author, copies):
        self.id = book_id
        self.name = name
        self.author = author
        self.copies = copies


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, name, author, copies):
        book = Book(book_id, name, author, copies)
        for book in self.books:
            if book_id == book.id:
                print("This id already taken")
                return
        self.books.append(book)
        self.save_books()

    def view_all(self):
        for book in self.books:
            print("Book ID", "\t\t", "Book", "\t\t", "Author", "\t\t",  "No. of Books", "\n", book.id, "\t\t", book.name, "\t\t", book.author, "\t\t", book.copies, "\n")

    def check_book(self, book_id):
        for book in self.books:
            if book_id == book.id:
                print("Book found:")
                print("Book ID:", book.id)
                print("Name:", book.name)
                print("Author:", book.author)
                print("No. of Books:", book.copies)
                return
        print("Book not found.")

    def update_book(self, book_id, name, author, copies):
        for book in self.books:
            if book.id == book_id:
                if name:
                    book.name = name
                if author:
                    book.author = author
                if copies:
                    book.copies = copies
                self.save_books()
                return
        print("Book not found.")

    def delete_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                return
        print("Book not found.")

    def save_books(self):
        file = open("books.txt", "w")
        for book in self.books:
            file.write(f"{book.id}\n{book.name}\n{book.author}\n{book.copies}\n")
        file.close()

    def load_books(self):
        file = open("books.txt", "r")
        lines = file.readlines()
        for i in range(0, len(lines)-1, 4):
            book_id = lines[i].strip()
            name = lines[i + 1].strip()
            author = lines[i + 2].strip()
            copies = int(lines[i + 3].strip())
            self.books.append(Book(book_id, name, author, copies))
        file.close()







