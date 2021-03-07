import random
import collections
from estadisticas import desviacion_estandar, media
from bokeh.plotting import figure, show

def tirar_dado (numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro_1 = random.choice([1,2,3,4,5,6])
        tiro_2 = random.choice([1,2,3,4,5,6])
        tiro = tiro_1 + tiro_2
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros


def graficar (x,y):
    plot = figure(title = 'Distribución normal')
    plot.vbar(x, top=y, width=0.5, color="#CAB2D6")
    show(plot)


def estimado(numero_de_tiros):
    estimados = tirar_dado(numero_de_tiros)

    media_estimados = media(estimados)
    sigma_estimados = desviacion_estandar(estimados)

    counter_estimados = dict(collections.Counter(estimados))

    graficar (list(counter_estimados.keys()), list (counter_estimados.values()))

    return (media_estimados, sigma_estimados)



def main (numero_de_tiros, numero_de_intentos):
    tiros_resultados = []

    for _ in range(numero_de_intentos):
        secuencia_de_tiros = estimado(numero_de_tiros)
        tiros_resultados.append(secuencia_de_tiros)

    tiros_con_12 = 0
    tiros_sin_12 = 0

    for tiro in tiros_resultados:
        if 12 in tiro:
            tiros_con_12 += 1
        elif 12 not in tiro:
            tiros_sin_12 += 1


    probabilidad_tiros_con_12 = tiros_con_12 / numero_de_intentos
    probabilidad_tiros_sin_12 = tiros_sin_12 / numero_de_intentos
    print( f'Probabilidad de que sea uno es {probabilidad_tiros_con_12}')
    print( f'Probabilidad de que no sea uno es {probabilidad_tiros_sin_12}')


if __name__ == '__main__':
    numero_de_tiros = int (input('Cuantos tiros del dado: '))
    numero_de_intentos = int (input('Cuantas simulaciones quieres correr: '))
    
    main(numero_de_tiros, numero_de_intentos)
