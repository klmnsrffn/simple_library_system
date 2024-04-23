from tabulate import tabulate
import administrateur.homepage as homepage

# Dictionary for books
books = {
        "Harry Potter à l'école des sorciers" : {
        "author": "J.K. Rowling",
        "quantity": 5,
        "loans": 0
    },
       "Le Seigneur des Anneaux" : { 
        "author": "J.R.R. Tolkien",
        "quantity": 3,
        "loans": 0
    },
        "Les Misérables" : {
        "author": "Victor Hugo",
        "quantity": 2,
        "loans": 0
    },
        "L'Homme révolté" : {
        "author": "Albert Camus",
        "quantity": 8,
        "loans": 0
    }
}

# Add books
def add_book(titre, author, quantity=1):
    if titre in books:
        books[titre]["quantity"] += quantity
        books[titre]["loans"] = books[titre]["loans"]
    else:
        books[titre] = {"author": author, "quantity": quantity, "loans": 0}
    print(f"The book '{titre}' has been added to the library.")

def borrow_book():
    display_book()
    try:
        index = int(input("Enter the index of the book to borrow : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return  # Return to the previous menu
    find_book = False
    for titre, info in books.items():
        if info["quantity"] - info["loans"] > 0:
            if index == 1:
                if books[titre]["quantity"] > books[titre]["loans"]:
                    books[titre]["loans"] += 1
                    print(f"You have borrowed '{titre}'.")
                    find_book = True
                    break
            index -= 1
    if not find_book:
        print(f"The book with index {index + 1} is not available or all copies are already borrowed.")

# Return book
def return_book():
    display_book()
    index = int(input("Enter the index of the book to return : "))
    for i, (titre, info) in enumerate(books.items(), start=1):
        if info["loans"] > 0:
            if index == i:
                if books[titre]["loans"] > 0:
                    books[titre]["loans"] -= 1
                    print(f"You have returned the book '{titre}'.")
                    break
    else:
        print(f"No copies of the book with index {index} were borrowed.")

#Display book
def display_book():
    table = []
    headers = ["Index", "Title", "author", "Available copies", "loans"]
    
    for index, (titre, info) in enumerate(books.items(), start=1):
        quantity_disponible = info["quantity"] - info["loans"]
        table.append([index, titre, info["author"], quantity_disponible, info["loans"]])

    print(tabulate(table, headers=headers, tablefmt="grid"))

# Menu to manage book
def livre_menu():
    while True:
        print("\nWhat action would you like to take?")
        print("1. Add book")
        print("2. Borrow book")
        print("3. Return book")
        print("4. Display book")
        print("5. Quit")
        choix = input("Entre your option (1-5) : ")
        if choix == "1":
                while True:
                    title = input("Enter title : ")
                    if not title:  # Check if the input is empty
                        print("Title cannot be empty. Program terminated.")
                        break  # Exit the loop and terminate the program
                    author = input("Enter author : ")
                    if not author:  # Check if the input is empty
                        print("Author cannot be empty. Program terminated.")
                        break  # Exit the loop and terminate the program
                    else:
                        while True:
                            quantity_str = input("Input quantity of the book : ")
                            if quantity_str.isdigit() and int(quantity_str) > 0:
                                quantity = int(quantity_str)
                                print(f"You has been input quantity : {quantity}")
                                break
                            else:
                                print("Please enter a positive integer for the quantity. Please try again.")
                        add_book(title, author, quantity)
                        break
        elif choix == "2":
            borrow_book()          
        elif choix == "3":
            return_book()
        elif choix == "4":
            display_book()
        elif choix == "5":
            break
            homepage.homepage_menu
        else:
            print("Invalid option. Please try again.")
