import math
import time

class ComplejidadAlgoritmica :

    def __init__ (self, n):
        self.n = n

    def constante (self):
        return 1

    def logaritmica (self):
        return math.log10(self.n)

    def lineal (self):
        return self.n

    def log_lineal (self):
        return self.n * math.log10(self.n)

    def polinomial (self):
        return self.n**2

    def exponecial(self):
        return 2**self.n

def main():
    nums = [1, 10, 100, 1000, 10000]

    for n in nums:
        complejidad = ComplejidadAlgoritmica (n)

        print ( 'N es igual a : {}'.format(n))

        principio = time.time()
        print ( 'El resultado de complejidad constante para {} es:'.format(n), complejidad.constante)
        fin = time.time()
        tiempo = fin - principio
        print("Has tarado {} segundos\n".format(tiempo))

        
        principio = time.time()
        print ( 'El resultado de complejidad logaritmica para {} es:'.format(n), complejidad.logaritmica)
        fin = time.time()
        tiempo = fin - principio
        print("Has tarado {} segundos\n".format(tiempo))

        
        principio = time.time()
        print ( 'El resultado de complejidad lineal para {} es:'.format(n), complejidad.lineal)
        fin = time.time()
        tiempo = fin - principio
        print("Has tarado {} segundos\n".format(tiempo))


        principio = time.time()
        print ( 'El resultado de complejidad logaritmica lineal para {} es:'.format(n), complejidad.log_lineal)
        fin = time.time()
        tiempo = fin - principio
        print("Has tarado {} segundos\n".format(tiempo))

        
        principio = time.time()
        print ( 'El resultado de complejidad polinomial para {} es:'.format(n), complejidad.polinomial)
        fin = time.time()
        tiempo = fin - principio
        print("Has tarado {} segundos\n".format(tiempo))


        principio = time.time()
        print ( 'El resultado de complejidad exponencial para {} es:'.format(n), complejidad.exponecial)
        fin = time.time()
        tiempo = fin - principio
        print("Has tarado {} segundos\n".format(tiempo))

        print ( "\n\n")

if __name__ == "__main__":

    main()