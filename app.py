from utils import database

user_choise="""
enter:
-'a' to add a new book
-'l' to list all books
-'r' to mark book as read
-'d' to delete book
-'q' to quit

your_choise:"""

def menu():
    database.create_book_table()
    user_input=input(user_choise)
    while user_input !='q':
        if user_input=='a':
            prompt_add_book()
        elif user_input=='l':
            list_books()
        elif user_input=='r':
            prompt_read_book()
        elif user_input=='d':
            prompt_delete_book()
        else:
            print("Invalid choise")

        user_input=input(user_choise)

def prompt_add_book():
    name=input("enter book name: ")
    author=input("enter author name: ")
    database.add_book(name,author)

def list_books():
    books=database.get_all_books()
    for book in books:
        if books == []:
            print("no book found")
        else:
            read="Yes" if book['read']=='1' else "No"
            print(f"{book['name']} by {book['author']}, read:{book['read']}")

def prompt_read_book():
    name=input("enter name of book that you finished: ")
    database.mark_book_as_read(name)

def prompt_delete_book():
    name = input("enter name of book that you want to delete: ")
    database.delete_book(name)



menu()
