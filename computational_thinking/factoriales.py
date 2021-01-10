def factorial(i):
    """[summary] This function calculated the factorial of a number

    Args:
        i ([int]): [Number to calculated factorial]

    Returns:
        [int]: [Factorial of the number]
    """
    if i == 1:
        return 1
    else:
        return i * factorial(i-1) 
    

def run():
    factorial_numero = int(input("Ingrese el numero para encontrar el factorial: "))
    print(f'El resultado es: {factorial(factorial_numero)}')


if __name__ == "__main__":
    run()