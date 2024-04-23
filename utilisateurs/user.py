from tabulate import tabulate
import utilisateurs.utilisateur as utilisateurs
import administrateur.livres as livres
from administrateur.livres import emprunter_livre
from administrateur.livres import rendre_livre
from database import users

def emprunter_livre():
    livres.afficher_livres()
    index = int(input("Entrez l'index du livre à emprunter : "))
    livre_trouve = False
    for titre, info in livres.items():
        if info["quantite"] - info["empruntes"] > 0:
            if index == 1:
                if livres[titre]["quantite"] > livres[titre]["empruntes"]:
                    livres[titre]["empruntes"] += 1
                    print(f"Vous avez emprunté le livre '{titre}'.")
                    livre_trouve = True
                    break
            index -= 1
    if not livre_trouve:
        print(f"Le livre avec l'index {index + 1} n'est pas disponible ou tous les exemplaires sont déjà empruntés.")

# Menu pour les utilisateurs
def user_menu():
    while True:
        print("Menu utilisateur :")
        print("1. Lister les livres")
        print("2. Emprunter un livre")
        print("3. Rendre un livre")
        print("4. Se déconnecter")
        choice = input("Votre choix : ")
        if choice == "1":
            livres.afficher_livres()
        elif choice == "2":
            livres.emprunter_livre()
        elif choice == "3":
            livres.afficher_livres()
            livres.rendre_livre()
        elif choice == "4":
            print("Déconnexion réussie.")
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")