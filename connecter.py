import hashlib
import utilisateurs.user as user
from database import users
from administrateur import homepage
from administrateur import livres


# Fonction pour créer un nouvel utilisateur
def create_user(username, password, admin=False):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = {"password": hashed_password, "admin": admin}
    
# Fonction pour supprimer un utilisateur
def delete_user(username):
    if username in users:
        del users[username]
        print(f"Utilisateur '{username}' supprimé avec succès.")
    else:
        print(f"Utilisateur '{username}' introuvable.")

# Fonction pour se connecter
def login(username, password):
    if username in users:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if users[username]["password"] == hashed_password:
            print(f"Bienvenue, {username}!")
            if users[username]["admin"]:
                homepage.homepage_menu()
            else:
                user.user_menu()
        else:
            print("Mot de passe incorrect.")
    else:
        print(f"Utilisateur '{username}' introuvable.")

# Fonction pour lister les utilisateurs
def list_users():

    print("Liste des utilisateurs :")
    for username in users:
        admin_str = "(admin)" if users[username]["admin"] else ""
        print(f"- {username} {admin_str}")

# Création d'un administrateur par défaut
create_user("admin", "password", admin=True)
create_user("anna", "oui", admin=False)
