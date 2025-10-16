print("Voici la devinette")

nombre_secret = 42

nombre_utilisateur = int(input("Taper un nombre entre 0 et 100 : "))

has_trouver = False
while not has_trouver:
    if nombre_utilisateur == nombre_secret:
        print("Gagné")
        has_trouver = True
    else:
        nombre_utilisateur = int(input("Taper un nombre entre 0 et 100 : "))