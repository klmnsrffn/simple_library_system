import connecter

# Boucle principale
while True:
    print("\nBienvenue !")
    print("1. Se connecter")
    print("2. Quitter")
    choice = input("Votre choix : ")
    if choice == "1":
        username = input("Nom d'utilisateur : ")
        password = input("Mot de passe : ")
        connecter.login(username, password)
    elif choice == "2":
        print("Au revoir !")
        break
    else:
        print("Choix invalide.")