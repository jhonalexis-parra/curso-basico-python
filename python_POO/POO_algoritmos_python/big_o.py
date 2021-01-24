#ley de la suma

def suma_1(n):

    for i in range(n):
        print(i)


    for i in range(n):
        print(i)

# 0(n) + 0(n) = 0 (n + n) = 0 (2n) = 0 (n)  --> Se busca el orden la función, en esta caso es lineal la funcipin crece en big o de n


def suma_2(n):

    for i in range(n):
        print(i)
    
    for i in range(n * n):
        print( i )

# 0(n) + 0 (n * n) = 0 (n + n^2) = 0 (n^2)  --> la función crece en big o de n^2 (cuadratica)


# Ley de la multiplicación


def multplicacion(n):

    for i in range(n):
        for j in range (n):
            print(i, j)

# 0 (n) * 0 (n) = 0 (n * n) = 0 (n^2)


# REcursividad múltiple

def fibonnaci (n):

    if n == 0 or n == 1:
        return 1

    return fibonnaci ( n - 1) + fibonnaci (n - 2)

# 0 ( 2 ** n)