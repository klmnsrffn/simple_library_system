import login

# Sign in page
while True:
    print("\nHello !")
    print("1. Sign in")
    print("2. Quit")
    choice = input("Input your option : ")
    if choice == "1":
        username = input("Enter username : ")
        password = input("Enter password : ")
        login.login(username, password)
    elif choice == "2":
        print("See you !")
        break
    else:
        print("Invalid option.")