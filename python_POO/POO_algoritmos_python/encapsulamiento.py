class CasillaDeVotacion:

    def __init__ (self, identificador, pais):
        self.__indentificador = identificador
        self.__pais = pais
        self.__region = None


    @property
    def pais(self):
        return self.__pais
    
    
    @property
    def region(self):
        return self.__region


    @region.setter
    def region (self, region):
        if region in self.__pais:
            self.__region = region

        raise ValueError (f'La region {region} no es valida en {self.__pais}')

if __name__ == "__main__":
    casilla = CasillaDeVotacion(123, ['Ciudad de Mexico',' Morelos'])
    print(casilla.pais)
    print(casilla.region)
    casilla.region = 'Morelos'
    print(casilla.region)