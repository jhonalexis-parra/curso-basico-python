import random


def ordenamiento_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        #llamada recursiva en cada mitad
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        #Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        #Iterador para la lista principal
        k = 0


        while i < len(izquierda) and j < len(derecha):
            print("+" * 5)
            print("agruapcion")
            
            if izquierda[i] < derecha [j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            print("+" * 5)
            print("izquierda")
                        
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            
            print("+" * 5)
            print("derecha")
            
            
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)
        
    print("Entregar lista final")
    
    return lista



if __name__ == '__main__':
    tamano_lista = int ( input (" De que tamano sera la lista? "))

    lista = [random.randint(0,100) for i in range(tamano_lista)]

    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_mezcla(lista)

    print(lista_ordenada)

    print("Final del final")