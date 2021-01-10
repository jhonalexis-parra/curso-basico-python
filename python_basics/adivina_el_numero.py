import random


def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = 0
    while (numero_aleatorio != numero_elegido):
        numero_elegido = int(input("Elige un numero de 1 a 100: ")) 
        if numero_elegido == numero_aleatorio:
            break
        elif numero_elegido > numero_aleatorio:
            print("El número es menor")
        else:
            print("El número es mayor")  
    print("¡Ganaste!") 


if __name__ == "__main__":
    run()