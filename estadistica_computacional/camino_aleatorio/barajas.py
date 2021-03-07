import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']
REAL = [1,10,11,12,13]


def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas


def obtener_mano (barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    
    return mano


def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []

    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    pares_dobles = 0
    trios = 0
    poker = 0
    full  = 0
    color = 0
    escalera = 0
    escalera_colores = 0
    escalera_real = 0

    for mano in manos:
        valores = []
        palos = []
        orden = []
        j = 0
        pares_cantidad = 0

        for carta in mano:
            valores.append(carta[1])
            palos.append(carta[0])

        for val in valores:
            if val == 'as':
                orden.append(1) 
            elif val == 'jota':
                orden.append(11)
            elif val == 'reina':
                orden.append(12)
            elif val == 'rey':
                orden.append(13)
            else:
                orden.append(int(val))
                                 
        counter_valores = dict (collections.Counter(valores))
        counter_palos = dict (collections.Counter(palos))
        orden = sorted(orden)

        print(orden)
        
        for i in range(orden[0], orden[0] + 5):
            j += i

        for val in counter_valores.values():
            if val == 2:
                pares_cantidad +=1
                continue

        if pares_cantidad == 2:
            pares_dobles += 1
        
        if pares_cantidad >= 1:
            pares += 1
        
        for val in counter_valores.values():
            if val == 3:
                trios +=1
                break
        
        for val in counter_valores.values():
            if poker == 3:
                trios +=1
                break

        for val in counter_palos.values():
            if val == 5:
                color += 1
                break

        if pares == 1 and trios == 1:
            full += 1

        if orden == REAL and color == 0:
            escalera += 1

        if orden == REAL and color == 1:
            escalera_real += 1
        
        if j == sum(orden) and color == 1:
            escalera_colores += 1
        
        if j == sum(orden) and color == 0:
            escalera += 1

        print(pares)
        print(pares_dobles)

    probabilidad_par = pares / intentos
    probabilidad_par_doble = pares_dobles / intentos
    probabilidad_trios = trios / intentos
    probabilidad_poker = poker / intentos
    probabilidad_color = color / intentos
    probabilidad_full = full / intentos
    probabilidad_escalera = escalera / intentos
    probabilidad_escalera_colores = escalera_colores / intentos
    probabilidad_escalera_real = escalera_real / intentos

    print (f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')
    print (f'La probabilidad de obtener un par doble en una mano de {tamano_mano} barajas es {probabilidad_par_doble}')
    print (f'La probabilidad de obtener un trio en una mano de {tamano_mano} barajas es {probabilidad_trios}')
    print (f'La probabilidad de obtener un poker en una mano de {tamano_mano} barajas es {probabilidad_poker}')
    print (f'La probabilidad de obtener un color en una mano de {tamano_mano} barajas es {probabilidad_color}')
    print (f'La probabilidad de obtener un full en una mano de {tamano_mano} barajas es {probabilidad_full}')
    print (f'La probabilidad de obtener una escalera en una mano de {tamano_mano} barajas es {probabilidad_escalera}')
    print (f'La probabilidad de obtener una escalera de color en una mano de {tamano_mano} barajas es {probabilidad_escalera_colores}')
    print (f'La probabilidad de obtener una escalera real en una mano de {tamano_mano} barajas es {probabilidad_escalera_real}')


if __name__ == '__main__':
    tamano_mano = int(input('De cuantas bajaras será la mano? '))
    intentos = int(input('Cuantos intetnos para calcular la probabilidad? '))

    main(tamano_mano , intentos)
    
    # barajas = crear_baraja()
    # mano = obtener_mano(barajas, 5)
    
    #print(mano)
