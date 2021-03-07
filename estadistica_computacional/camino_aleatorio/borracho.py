import random


class Borracho:


    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional (Borracho):


    def __init__ (self, nombre):
        super().__init__(nombre)

    
    def camina (self):
        return random.choice([(0, 1), (0,-1), (1,0) , (-1,0)])


class BorrachoColombiano (Borracho):

    
    def __init__ (self, nombre):
        super().__init__(nombre)

    
    def camina (self):
        return random.choice([(0,random.randint(1,5)), (0,random.randint(-5,-1)), (random.randint(1,5), 0), (random.randint(-5,-1), 0 )])

    

