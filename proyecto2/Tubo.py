from pila import Pila
import random

random.seed()

class Tubo(Pila):
    i = 0 
    def __init__(self, iden=-1, c=-1):
        if(iden == -1):
            self.iden = Tubo.i
            Tubo.i += 1
        else:
            self.iden = iden

        if(c == -1):
            self.capacidad = random.randint(5,25)
        else:
            self.capacidad = c

        super().__init__() #inicializa la pila
        self.ocupacion = 0

    def Cabe(self, v):
        ocupara = self.ocupacion + v.longitud
        return (ocupara <= self.capacidad)

    def Estacionar(self, v):
        if (self.Cabe(v)):
            self.Empilar(v)
            self.ocupacion += v.longitud

    def Retirar(self):
        self.Desempilar()
        
    
    def Cercano(self):
        return self.Tope().placa

    def Existe(self):
        return None
