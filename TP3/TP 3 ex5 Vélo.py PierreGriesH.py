
debut = int(input("Donnez l’heure de début de la location (un entier) : "))
fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

if debut < 0 or debut > 24 or fin < 0 or fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !")
elif debut == fin:
    print("L'heure de fin est identique à l'heure de début.")
elif debut > fin:
    print("Erreur")
else:

    duree = fin - debut

    if debut >= 0 and debut < 7:
        if fin <= 7:
            prix = duree * 1
            
        elif fin <= 17:
            prix = (7 - debut) * 1 + (fin - 7) * 2
            
        else:
            prix = (7 - debut) * 1 + (17 - 7) * 2 + (fin - 17) * 1
            
    elif debut >= 7 and debut < 17:
        
        if fin <= 17:
            prix = duree * 2
            
        else:
            prix = (17 - debut) * 2 + (fin - 17) * 1
    else:
        prix = duree * 1

    print("Vous avez loué votre vélo pendant")
    print(duree , "heures")
    print("Le prix de la location est de", prix, "euros.")


