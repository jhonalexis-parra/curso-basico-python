frutas = ['manzana', 'pera', 'mango']
for fruta in frutas:
    print(fruta)


iter('cadena') # cadena
iter(['a', 'b', 'c']) # lista
iter(('a', 'b', 'c')) # tupla
iter({'a', 'b', 'c'}) # conjunto
iter({'a': 1, 'b': 2, 'c': 3}) # diccionario


#Iterador
iterador = iter(frutas)
print(next(iterador))
print(next(iterador))
print(next(iterador))
#print(next(iterador)) #Genera error debido a que es no hay mas iterables

#Iterar en diccionarios
estudiantes = {
    'mexico': 10,
    'colombia' : 15,
    'puerto_rico' : 4,
}

for pais in estudiantes:
    print(pais)

for pais in estudiantes.keys():
    print(pais)

for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)

for pais, numero_de_estudiantes in estudiantes.items():
    print(f'El país: {pais} estudiantes {numero_de_estudiantes} ')