from tabulate import tabulate
import users.user_book as utilisateurs
import administrateur.books as books
from administrateur.books import borrow_book
from administrateur.books import return_book
from database import users

def borrow_book():
    books.display_book()
    index = int(input("Enter the index of the book to borrow : "))
    find_book = False
    for titre, info in books.items():
        if info["quantity"] - info["loans"] > 0:
            if index == 1:
                if books[titre]["quantity"] > books[titre]["loans"]:
                    books[titre]["loans"] += 1
                    print(f"You borrowed the book '{titre}'.")
                    find_book = True
                    break
            index -= 1
    if not find_book:
        print(f"The book with index {index + 1} is not available or all copies are already borrowed.")
# Menu for the users
def user_menu():
    while True:
        print("User Menu :")
        print("1. List books")
        print("2. Borrow book.")
        print("3. Return book")
        print("4. Sign out")
        choice = input("Your option : ")
        if choice == "1":
            books.display_book()
        elif choice == "2":
            books.borrow_book()
        elif choice == "3":
            books.display_book()
            books.return_book()
        elif choice == "4":
            print("Sign out successful.")
            print("See you !")
            break
        else:
            print("Invalid option.")