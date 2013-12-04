# Proyecto 2
#
# Clase Tubo
#
# Autores:
#   Jose Pascarella     11-10743
#   Amin Arria          11-10053
#
# Ultima Modificacion: 5 / 12 / 2013


from cola import *
from pila import *
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
        vtmp = self.Tope()
        self.Desempilar()
        self.ocupacion -= vtmp.longitud
        
    def Cercano(self):
        return self.Tope()

    def Existe(self, valor):
        aux = Pila()
        esta = False
        while not (self.Vacia() or esta):
            tmp = self.Tope()
            if(tmp.placa == valor):
                esta = True
            else:
                aux.Empilar(tmp)
                self.Desempilar()
        while not aux.Vacia():
            tmp = aux.Tope()
            self.Empilar(tmp)
            aux.Desempilar()
        return esta
            
    def GetColor(self, salida, valor):
        i = self.cabeza
        while (i != None):
            if (i.info.color == valor):
                salida.Encolar(i.info)
            i = i.sig
        return salida
            
    def GetAnyo(self, salida, valor):
        i = self.cabeza
        while (i != None):
            if (i.info.anyo == int(valor)):
                salida.Encolar(i.info)
            i = i.sig
        return salida
    
    def GetModelo(self, salida, valor):
        i = self.cabeza
        while (i != None):
            if (i.info.modelo == valor):
                salida.Encolar(i.info)
            i = i.sig
        return salida
    
    def GetLongitud(self, salida, valor):
        i = self.cabeza
        while (i != None):
            if (i.info.longitud == valor):
                salida.Encolar(i.info)
            i = i.sig
        return salida
    
    
    
    
    
    
    
    
    
    
