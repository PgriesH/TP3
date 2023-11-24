X = int(input("Entrez X : "))

N = 0

nombre = 0

while nombre < X:

    nombre  = nombre + N
    N = N + 1
    if nombre == X or nombre > X:
        print(N - 1)
   
