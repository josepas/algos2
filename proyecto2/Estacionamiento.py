# Proyecto 2
#
# Clase Estacionamiento 
#
# Autores:
#   Jose Pascarella     11-10743
#   Amin Arria          11-10053
#
# Ultima Modificacion: 5 / 12 / 2013

from cola import *
from Tubo import Tubo
from Evento import Evento
from random import *

class Estacionamiento(Cola):
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
            self.Generar(tubo.iden, tubo.capacidad)
            while(tubo.ocupacion > 0):
                vtmp = tubo.Cercano()
                tubo.Retirar()
                if(vtmp.placa == placa):
                    v = vtmp
                else:
                    # tmp.Estacionar(vtmp) ---- esto no se si funcionaria :0
                    self.ultimo.info.Estacionar(vtmp)
            self.Destruir()
            return v
            

    def Busqueda(self, selec, valor):
        salida = Cola()        
        i = self.cabeza
        while (i != None):
            if (selec == 'color'):
                salida = i.GetColor(salida, valor)
                
            elif (selec == 'longitud'):
                salida = i.GetLongitud(salida, valor)
                
            elif (selec == 'anyo'):
                salida = i.GetAnyo(salida, valor)
                
            elif (selec == 'modelo'):
                salida = i.GetModelo(salida, valor)

            i = i.sig
        return salida
        
    def ProcesarLlegadas(self, archivo):
        f = open(archivo, 'r')
        for i in f:
            print(i.strip()) # flag
            h = Evento(i.strip())
            
            
            
            
            
            
            
            
            
            
            
            