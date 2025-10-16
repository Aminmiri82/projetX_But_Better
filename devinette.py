print("Voici la devinette")

nombre_secret = 42

nombre_utilisateur = int(input("Taper un nombre entre 0 et 100 : "))

if nombre_utilisateur == nombre_secret:
    print("Gagné")
else:
    print("Perdu")