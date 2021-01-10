#Funciones recursivas
def potencia(valor, exponente):
    if exponente > 0:
        total = valor ** exponente
        print("La potencia de {} a la {} es: {}".format(valor, exponente, total))
        potencia(valor, exponente - 1)
    else:
        print("Muchas gracias")


def run():
    valor = int(input("Escriba la base de la potencia a calcular: "))
    exponente = int(input("Escriba el exponente máximo a calcuar: "))
    potencia (valor, exponente)


if __name__ == "__main__":
    run()
