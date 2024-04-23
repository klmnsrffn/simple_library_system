from administrateur import comptes
from administrateur import livres

def homepage_menu():
    while True :
        print("\nBienvenue Admin!")
        print("\nQue souhaitez-vous faire ?")
        print("\n1. Gérer les comptes des Utilisateurs")
        print("\n2. Gérer la Bibliothéque")
        print("\n3. Se déconnecter")
        Input = input("\nEntrer votre taché: ")
        if Input == "1":
            comptes.admin_menu()
        elif Input == "2":
            livres.livre_menu()
        elif Input == "3":
            print("Déconnexion réussie.")
            print("Au revoir !")
            break
        else :
            print("Choix invalide. Veuillez réessayer.")
