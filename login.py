import hashlib
import users.user as user
from database import users
from administrateur import homepage
from administrateur import books


# Function to create new user account
def create_user(username, password, admin=False):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = {"password": hashed_password, "admin": admin}
    
# Function to delete user account
def delete_user(username):
    if username in users:
        del users[username]
        print(f"'{username}' has been deleted.")
    else:
        print(f"'{username}' not found.")

# Fonction to do sign in
def login(username, password):
    if username in users:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if users[username]["password"] == hashed_password:
            print(f"Welcome, {username}!")
            if users[username]["admin"]:
                homepage.homepage_menu()
            else:
                user.user_menu()
        else:
            print("Password incorrect.")
    else:
        print(f"'{username}' not found.")

# Fonction pour lister les utilisateurs
def list_users():

    print("List Users :")
    for username in users:
        admin_str = "(admin)" if users[username]["admin"] else ""
        print(f"- {username} {admin_str}")

# Création d'un administrateur par défaut
create_user("admin", "password", admin=True)
create_user("anna", "oui", admin=False)
