from cola import cola
from Tubo import Tubo
from random import *

class Estacionamiento(cola):
    i = 0
    def __init__(self):
        seed()
        self.iden = Estacionamiento.i
        Estacionamiento.i += 1 
        super().__init__() #inicializa la cola

    def Generar(self):
        aux = Tubo()
        self.Encolar(aux)
        return aux

    def Estacionar(self, v):
        espacio = False
        for i in range(0,len(self.cont)):
            if(self.Tope().Cabe(v)):
                self.Tope().Estacionar(v)
                espacio = True
                break
            else:
                self.Encolar(self.Tope())
                self.Desencolar()
        if not espacio:
            tmp = self.Generar()
            tmp.Estacionar(v)

