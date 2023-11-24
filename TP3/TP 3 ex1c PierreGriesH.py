for loop in range(10):
    N = int(input("Entrez un entier entre 0 et 20 : "))
    if N < 0 or N > 20:
       pass 
    if N < 10:
        print("Le nombre de valeur inférieur strictement à 10")
        
    elif N >= 10 and N < 15:
        print("Le nombre de valeur supérieur ou égal à 10 et inférieur strictement à 15")

    elif N >= 15 and N <= 20:
        print("Le nombre de valeur supérieur ou égal à 15")

