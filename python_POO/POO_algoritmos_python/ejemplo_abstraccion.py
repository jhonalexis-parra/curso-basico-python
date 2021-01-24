class manana_milagrosa:

        
    def __init__ (self, nombre):
        self.nombre = nombre
        self.tiempo_ejercicio = 0
        self.tiempo_lectura = 0
        self.tiempo_escritura = 0
        self.tiempo_oracion = 0

    
    def fijar_alarma (self, hora_despertar):
        self.alarma = hora_despertar

    
    def ejercicio (self, tipo_ejercicio, tiempo):
        self.tipo_ejercicio = tipo_ejercicio
        self.tiempo_ejercicio = tiempo


    def lectura (self, libro, tiempo):
        self.libro = libro
        self.tiempo_lectura = tiempo


    def escritura (self, tiempo):
        self.tiempo_escritura = tiempo


    def oracion (self, oracion, tiempo ):
        self.tipo_oracion = oracion
        self.tiempo_oracion = tiempo


    def tiempo (self):
        self.tiempo_total = self.tiempo_ejercicio + self.tiempo_escritura + self.tiempo_lectura + self.tiempo_oracion
        return self.tiempo_total


    def informacion (self):
        return (f'El libro es {self.libro}, el ejercicio es {self.tipo_ejercicio} y la oracion es {self.tipo_oracion}')


if __name__ == "__main__":

    rutina_lunes = manana_milagrosa('jhon')
    rutina_lunes.fijar_alarma(6)
    rutina_lunes.ejercicio("yoga", 30)
    rutina_lunes.lectura("Sentido de la vida", 30)
    rutina_lunes.escritura(5)
    rutina_lunes.oracion("Oración de vida", 5)
    print(rutina_lunes.tiempo())
    print(rutina_lunes.informacion())



    


    