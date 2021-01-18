class Automovil ():


    def __init__ (self, modelo, marca, color, tanque, cilindros):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en resposo'
        self._motor = Motor(cilindros, tanque)
        self.velocidad = 0


    def acelerar (self, tipo = 'despacio'):
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
            self.control_velocidad('rapida')
        else:
            self._motor.inyecta_gasolina(5)
            self.control_velocidad('despacio')

        self._estado = 'andando'
        return self._estado

    
    def control_velocidad (self, aceleracion = 'despacio'):
        if aceleracion == 'rapido':
            self.velocidad += 8
        else:
            self.velocidad += 3

    
    def frenar (self, tipo='suave'):
        if self.velocidad == 0:
            self._estado = 'en reposo'
            return self._estado
        if tipo == 'suave':
            self.velocidad -= 1
        else:
            self.velocidad -= 3  

    
class Motor:


    def __init__ (self, cilindros, tanque, tipo='gasolina', ):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
        self._tanque = Tanque(tanque)


    def inyecta_gasolina (self, cantidad):
        self._tanque.pierde_gasolina(cantidad)


class Tanque:


    def __init__(self, max_centimetros_cubicos, gasolina = 'corriente'):
        self.max_centimetros_cubicos = max_centimetros_cubicos
        self.gasolina = gasolina
        self.cantidad = max_centimetros_cubicos / 2


    def pierde_gasolina(self, cantidad):
        self.cantidad -= cantidad


    def cargar_gasolina(self, cantidad):
        self.cantidad += cantidad


if __name__ == "__main__":

    car_jhon = Automovil('Aveo', 'Chevrolet', 'Rojo', 250, 16)
    print (car_jhon.velocidad)
    car_jhon.acelerar(tipo = 'rapido')
    car_jhon.acelerar(tipo = 'despacio')
    car_jhon.acelerar(tipo = 'rapido')
    car_jhon.acelerar(tipo = 'rapido')
    car_jhon.frenar(tipo='fuerte')
    print(car_jhon.velocidad)
    print(car_jhon._motor._tanque.cantidad)
    



