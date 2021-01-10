def suma(a,b):
    total = a + b
    return total

print(suma(2,3))

def nombre_completo (nombre, apellido, inverso= False):
    if inverso:
        return f'{apellido}  {nombre}'
    else:
        return f'{nombre}  {apellido}'

nombre_completo( 'Jhon' , 'Parra')
nombre_completo( 'Jhon' , 'Parra' , inverso=True )
nombre_completo( apellido='Parra' , nombre = 'Jhon' )
