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
            while True:
                username = input("Username : ")
                if not username:  # Check if the input is empty
                    print("Username cannot be empty. Program terminated.")
                    break  # Exit the loop and terminate the program
                password = input("Password : ")
                if not password:  # Check if the input is empty
                    print("Password cannot be empty. Program terminated.")
                    break  # Exit the loop and terminate the program
                if ' ' in username:
                    print("Username cannot contain spaces. Please try again.")
                elif ' ' in password:
                    print("Password cannot contain spaces. Please try again.")
                else:
                    break  # Exit the loop if both inputs are valid
            if username and password:  # Check if both inputs are not empty
                admin = input("Do you want to create this account as an administrator? (y/n) ").lower()
                while True:
                    if admin == "y":
                        admin = True
                        login.create_user(username, password, admin)
                        print(f"'{username}' has been added as an administrator.")
                        break
                    elif admin == "n":
                        admin = False
                        login.create_user(username, password, admin)
                        print(f"'{username}' has been added as a regular user.")
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                        admin = input("Do you want to create this account as an administrator? (y/n) ").lower()
            else:
                print("Program terminated due to invalid input.")
        elif choice == "2":
            username = input("Enter the username of the account to delete : ")
            login.delete_user(username)
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

