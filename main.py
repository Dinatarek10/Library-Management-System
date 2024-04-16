from books_classes import *


library = Library()
library.load_books()

while True:
    print("1. Add book")
    print("2. Display books")
    print("3. Check book")
    print("4. Update book")
    print("5. Delete book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("book ID: ")
        name = input("book name: ")
        author = input("author name: ")
        copies = int(input("No. of Books: "))
        library.add_book(book_id, name, author, copies)
    elif choice == "2":
        library.view_all()
    elif choice == "3":
        book_id = input("book ID: ")
        library.check_book(book_id)
    elif choice == "4":
        book_id = input("book ID: ")
        name = input("new book name (press enter to skip): ")
        author = input("new author name (press enter to skip): ")
        copies = input("new No. of Books (press enter to skip): ")
        if copies:
            copies = int(copies)
        library.update_book(book_id, name, author, copies)
    elif choice == "5":
        book_id = input("Enter book ID to delete: ")
        library.delete_book(book_id)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")


