from tabulate import tabulate
from database import users
import administrateur.livres as livres
import connecter


livres = livres.livres

def emprunter_livre(utilisateur, titre):
    if titre in livres:
        if livres[titre]["quantite"] > livres[titre]["empruntes"]:
            livres[titre]["empruntes"] += 1
            if utilisateur not in users:
                users[utilisateur] = {"livres_empruntes": []}
            if "livres_empruntes" not in users[utilisateur]:
                users[utilisateur]["livres_empruntes"] = []
            users[utilisateur]["livres_empruntes"].append(titre)
            print(f"Vous avez emprunté le livre '{titre}'.")
        else:
            print(f"Désolé, tous les exemplaires du livre '{titre}' sont déjà empruntés.")
    else:
        print(f"Le livre '{titre}' n'est pas disponible dans la bibliothèque.")

# Fonction pour afficher la liste des livres disponibles
def afficher_livres_disponibles():
    table = []
    headers = ["Titre", "Auteur", "Exemplaires disponibles"]
    for titre, info in livres.items():
        quantite_disponible = info["quantite"] - info["empruntes"]
        table.append([titre, info["auteur"], quantite_disponible])

    print(tabulate(table, headers=headers, tablefmt="grid"))

