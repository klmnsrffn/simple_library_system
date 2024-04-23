import login
from administrateur import homepage as homepage

# Menu for Admin
def admin_menu():
    while True:
        print("\nAdministrator Menu :")
        print("1. Create Account")
        print("2. Delete User Account")
        print("3. Display User Account")
        print("4. Quit")
        choice = input("Input your option : ")
        if choice == "1":
            username = input("Username : ")
            password = input("Password : ")
            admin = input("Administrator ? (y/n) ").lower() == "o"
            login.create_user(username, password, admin)
            print(f"'{username}' has been added.")
        elif choice == "2":
            username = input("Enter the username of the account to delete : ")
            login.delete_user(username)
        elif choice == "3":
            login.list_users()
        elif choice == "4":
            break
            homepage.homepage_menu
        else:
            print("Invalid option.")

