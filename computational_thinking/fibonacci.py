def fibonacci(valor):
    """Function for calculated fibonacci of a number

    Args:
        valor ([int]): [Number for calculated fibonacci]

    Returns:
        [int]: [Result of the fibonacci math]
    """
    if valor == 0 or valor == 1:
        return 1
    return fibonacci(valor - 1) + fibonacci (valor - 2)


def run():
    valor = int(input("Calcula el valor n para calcular su fibonacci: "))
    print(fibonacci(valor))


if __name__ == "__main__":
    run()