from tabulate import tabulate
from database import users
import administrateur.books as books
import login


books = books.books

def borrow_book(utilisateur, titre):
    if titre in books:
        if books[titre]["quantity"] > books[titre]["loans"]:
            books[titre]["loans"] += 1
            if utilisateur not in users:
                users[utilisateur] = {"borrow_book": []}
            if "borrow_book" not in users[utilisateur]:
                users[utilisateur]["borrow_book"] = []
            users[utilisateur]["borrow_book"].append(titre)
            print(f"You have borrowed the book '{titre}'.")
        else:
            print(f"Sorry, all copies of the book '{titre}' are already borrowed.")
    else:
        print(f"The book '{titre}' is not available in the library.")

# Display book
def display_available_book():
    table = []
    headers = ["Title", "Author", "Available copies."]
    for titre, info in books.items():
        quantity_disponible = info["quantity"] - info["loans"]
        table.append([titre, info["auteur"], quantity_disponible])

    print(tabulate(table, headers=headers, tablefmt="grid"))

