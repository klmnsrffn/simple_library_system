import connecter
from administrateur import homepage as homepage

# Menu pour les administrateurs
def admin_menu():
    while True:
        print("\nMenu administrateur :")
        print("1. Créer un utilisateur")
        print("2. Supprimer un utilisateur")
        print("3. Lister les utilisateurs")
        print("4. Quitter")
        choice = input("Votre choix : ")
        if choice == "1":
            username = input("Nom d'utilisateur : ")
            password = input("Mot de passe : ")
            admin = input("Administrateur ? (o/n) ").lower() == "o"
            connecter.create_user(username, password, admin)
            print(f"Utilisateur '{username}' créé avec succès.")
        elif choice == "2":
            username = input("Nom d'utilisateur à supprimer : ")
            connecter.delete_user(username)
        elif choice == "3":
            connecter.list_users()
        elif choice == "4":
            break
            homepage.homepage_menu
        else:
            print("Choix invalide.")

