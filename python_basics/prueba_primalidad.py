def es_primo(numero):
    contador = 0
    if numero == 1:
        return False
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
        if contador > 2:
            return False 
    return True 


def run():
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo") 


if __name__ == "__main__":
    run()