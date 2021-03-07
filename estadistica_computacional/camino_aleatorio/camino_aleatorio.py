from borracho import BorrachoTradicional
from borracho import BorrachoColombiano
from campo import Campo
from coordenada import Coordenada

from bokeh.plotting import figure, show

def caminata (campo,borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    x_ilum = []
    y_ilum = []


    for _ in range(pasos):
        campo.mover_borracho(borracho)
        x_ilum.append(campo.obtener_coordenada(borracho).x)
        y_ilum.append(campo.obtener_coordenada(borracho).y)

    graficar(x_ilum, y_ilum)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata (pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho (nombre = 'David')
    origen = Coordenada(0,0)
    distancias = []
    

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(simulacion_caminata)

    return distancias


def graficar (x , y):
    grafica = figure(title = "Camino aleatorio", x_axis_label = 'pasos', y_axis_label='distancia')
    grafica.line(x, y, legend = 'distancia media')

    show(grafica)


def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):

    distancias_media_por_caminata = []
    
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media =  round(sum(distancias) / len(distancias), 4)
        distancia_max = max(distancias)
        distancia_min = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print ( f'{tipo_de_borracho.__name__} caminata aleatorio de {pasos}')
        print ( f'Media = {distancia_media}')
        print ( f'Max = {distancia_max}')
        print ( f'Min = {distancia_min}')

    graficar (distancias_de_caminata, distancias_media_por_caminata)



if __name__ == '__main__':

    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)

    main(distancias_de_caminata, numero_de_intentos, BorrachoColombiano)


  