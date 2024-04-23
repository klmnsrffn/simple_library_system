from administrateur import account
from administrateur import books

def homepage_menu():
    while True :
        print("\nWhat action would you like to take?")
        print("\n1. Manage user accounts. ")
        print("\n2. Manage Library.")
        print("\n3. Sign Out")
        Input = input("\nEnter your option: ")
        if Input == "1":
            account.admin_menu()
        elif Input == "2":
            books.livre_menu()
        elif Input == "3":
            print("Sign out successful")
            print("See you !")
            break
        else :
            print("Invalid option, please try again.")
