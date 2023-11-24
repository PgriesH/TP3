import random

nb =random.randint(1, 100)
nbtour = 0
trouve = False

while trouve == False:

    nombre = int(input("Entrez un nombre : "))

    if nombre > nb:
        print("Plus petit")
        nbtour = nbtour + 1
    

    elif nombre < nb:
        print("Plus grand")
        nbtour = nbtour + 1

    elif nombre == nb:
        trouve == True
        print("Egal")
        print(nbtour)
        break 
    
