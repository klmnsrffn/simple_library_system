from tabulate import tabulate
import administrateur.homepage as homepage

# Dictionnaire pour stocker les livres
livres = {
        "Harry Potter à l'école des sorciers" : {
        "auteur": "J.K. Rowling",
        "quantite": 5,
        "empruntes": 0
    },
       "Le Seigneur des Anneaux" : { 
        "auteur": "J.R.R. Tolkien",
        "quantite": 3,
        "empruntes": 0
    },
        "Les Misérables" : {
        "auteur": "Victor Hugo",
        "quantite": 2,
        "empruntes": 0
    },
        "L'Homme révolté" : {
        "auteur": "Albert Camus",
        "quantite": 8,
        "empruntes": 0
    }
}

# Fonction pour ajouter un livre
def ajouter_livre(titre, auteur, quantite=1):
    if titre in livres:
        livres[titre]["quantite"] += quantite
        livres[titre]["empruntes"] = livres[titre]["empruntes"]
    else:
        livres[titre] = {"auteur": auteur, "quantite": quantite, "empruntes": 0}
    print(f"Le livre '{titre}' a été ajouté à la bibliothèque.")

# Fonction pour emprunter un livre
def emprunter_livre():
    afficher_livres()
    
            # print(f'sama men {value['auteur']} ')

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

        
# Fonction pour emprunter un livre
def emprunter_livre():
    afficher_livres()
    index = int(input("Entrez l'index du livre à emprunter : "))
    for i, (titre, info) in enumerate(livres.items(), start=1):
        if info["quantite"] - info["empruntes"] > 0:
            if index == i:
                if livres[titre]["quantite"] > livres[titre]["empruntes"]:
                    livres[titre]["empruntes"] += 1
                    print(f"Vous avez emprunté le livre '{titre}'.")
                    break
    else:
        print(f"Le livre avec l'index {index} n'est pas disponible ou tous les exemplaires sont déjà empruntés.")

# Fonction pour rendre un livre
def rendre_livre():
    afficher_livres()
    index = int(input("Entrez l'index du livre à rendre : "))
    for i, (titre, info) in enumerate(livres.items(), start=1):
        if info["empruntes"] > 0:
            if index == i:
                if livres[titre]["empruntes"] > 0:
                    livres[titre]["empruntes"] -= 1
                    print(f"Vous avez rendu le livre '{titre}'.")
                    break
    else:
        print(f"Aucun exemplaire du livre avec l'index {index} n'était emprunté.")

#fonction pour afficher livre
def afficher_livres():
    table = []
    headers = ["Index", "Titre", "Auteur", "Exemplaires disponibles", "Empruntes"]
    
    for index, (titre, info) in enumerate(livres.items(), start=1):
        quantite_disponible = info["quantite"] - info["empruntes"]
        table.append([index, titre, info["auteur"], quantite_disponible, info["empruntes"]])

    print(tabulate(table, headers=headers, tablefmt="grid"))

# Boucle principale
def livre_menu():
    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1. Ajouter un livre")
        print("2. Emprunter un livre")
        print("3. Rendre un livre")
        print("4. Afficher la liste des livres disponibles")
        print("5. Quitter")
        choix = input("Entrez votre choix (1-5) : ")

        if choix == "1":
            titre = input("Entrez le titre du livre : ")
            auteur = input("Entrez l'auteur du livre : ")

            while True:
                quantite_str = input("Entrez la quantité d'exemplaires : ")
                if quantite_str.isdigit() and int(quantite_str) > 0:
                    quantite = int(quantite_str)
                    print(f"Vous avez entré la quantité : {quantite}")
                    break
                else:
                    print("Veuillez entrer un nombre entier positif pour la quantité. Réessayez.")
            ajouter_livre(titre, auteur, quantite)
        elif choix == "2":
            emprunter_livre()          
        elif choix == "3":
            rendre_livre()
        elif choix == "4":
            afficher_livres()
        elif choix == "5":
            break
            homepage.homepage_menu
        else:
            print("Choix invalide. Veuillez réessayer.")
