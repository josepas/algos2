from cola import Cola
from Tubo import Tubo
from random import *

class Estacionamiento(cola):
    i = 0
    def __init__(self):
        seed()
        self.iden = Estacionamiento.i
        Estacionamiento.i += 1 
        super().__init__() #inicializa la cola

    def Generar(self, iden=-1, capacidad=-1):
        aux = Tubo(iden, capacidad)
        self.Encolar(aux)
        return aux
    
    def Destruir(self):
            self.Desencolar()
    
    def Estacionar(self, v):
        for i in range(0, self.tam):
            if(self.Tope().Cabe(v)):
                self.Tope().Estacionar(v)
                return self.Tope().iden
            else:
                self.Encolar(self.Tope())
                self.Desencolar()
        tmp = self.Generar()
        tmp.Estacionar(v)
        return tmp.iden

    def Existe(self, placa, ticket):
        i = self.Tope()
        while(i.iden != ticket):
            self.Encolar(i)
            self.Desencolar()
            i = self.Tope()
        return i.Existe("Placa", placa)

    def Retirar(self, placa, ticket):
        if(self.Existe(placa, ticket)):
            tubo = self.Tope()
            tmp = self.Generar(tubo.iden, tubo.capacidad)
            while(tubo.ocupacion > 0):
                vtmp = tubo.Cercano()
                tubo.Retirar()
                if(vtmp.placa == placa):
                    v = vtmp
                else:
                    tmp.Estacionar(vtmp)
            self.Destruir()
            return v
