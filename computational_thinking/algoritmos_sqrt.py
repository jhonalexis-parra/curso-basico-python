# Aproximacion
def aproximacion(): 
    objetivo = int(input('Elige un número: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        #print(f'{abs(respuesta**2 -objetivo)} ---- {respuesta}')
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        return("No se encontro la raiz cuadrada del objetivo")
    else:
        return(f'La raiz cuadrada de {objetivo}  es {respuesta}')


#Enumeracion
def enumeracion():  
    
    objetivo = int(input("Escoge un entero: "))
    respuesta = 0

    while respuesta**2 < objetivo:
        # print(respuesta)
        respuesta += 1

    if respuesta** 2 == objetivo:
        return(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        return(f'{objetivo} no tiene una raiz cuadrada exacta')


#Busqueda binaria
def busqueda_binaria():
    objetivo = int(input('Elige un número: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0 , objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        # print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta** 2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2
    return(f'La raiz cuadra del objetivo es la {respuesta}')

def run():
    opcion = -1
    while opcion != 0:
        print(''' 
            Calculo de raíz cuadrada con algoritmos
            Por favor selecciona con el numero correspondiente el algoritmo:
                1 -> Búsqueda binaria
                2 -> Aproximación de soluciones
                3 -> Enumeración exhaustiva
                0 -> Salir    
            ''')
        opcion = input("Seleccione la opcion: ")
        if opcion == '1':
            print(busqueda_binaria())
        elif opcion == '2':
            print(aproximacion())
        elif opcion == '3':
            print(enumeracion())
        elif opcion == '0':
            break
        else:
            print('Seleccione una opción válida')
    
    print("Muchas gracias, vuelva pronto")

if __name__ == "__main__":
    run()