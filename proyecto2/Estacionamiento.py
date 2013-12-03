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
from random import *

class Estacionamiento(Cola):
    i = 0
    def __init__(self, nombre):
        seed(0.101101)
        self.nombre = nombre
        self.iden = Estacionamiento.i
        Estacionamiento.i += 1 
        super().__init__() #inicializa la cola

    def Generar(self, iden=-1, capacidad=-1):
        aux = Tubo(iden, capacidad)
        self.Encolar(aux)
        return aux
    
    def Destruir(self):
            self.Desencolar()
    
    def Iterar(self, i):
        cota = 0 
        while(self.Tope().iden != i and cota < self.tam):
            self.Encolar(self.Tope())
            self.Desencolar()
            cota += 1
            
    def Estacionar(self, v):
        if(self.Vacia()):
            self.Generar()
            self.Tope().Estacionar(v)
        elif(self.Tope().Cabe(v)):
            self.Tope().Estacionar(v)
        else:
            aux = self.Generar()
            self.Iterar(aux.iden)
            self.Tope().Estacionar(v)
        return self.Tope().iden

    def Existe(self, placa, ticket):
        self.Iterar(ticket)
        tubo = self.Tope()
        return tubo.Existe("Placa", placa)

    def Retirar(self, placa, ticket):
        if(self.Existe(placa, ticket)):
            tubo = self.Tope()
            aux = Tubo(tubo.iden, tubo.capacidad)
            while(tubo.ocupacion > 0):
                vtmp = tubo.Cercano()
                tubo.Retirar()
                if(vtmp.placa == placa):
                    v = vtmp
                else:
                    aux.Estacionar(vtmp)
            self.Destruir()
            if not aux.Vacia():
                self.Encolar(aux)
                self.Iterar(aux.iden)
            return v
            

    def Busqueda(self, selec, valor):
        salida = Cola()        
        i = self.cabeza
        while (i != None):
            
            if (selec == 'Color'):
                salida = i.info.GetColor(salida, valor)
                
            elif (selec == 'Longitud'):
                salida = i.info.GetLongitud(salida, valor)
                
            elif (selec == 'Anyo'):
                salida = i.info.GetAnyo(salida, valor)
                
            elif (selec == 'Modelo'):
                salida = i.info.GetModelo(salida, valor)

            i = i.sig
        return salida

    def Vaciar(self, etiqueta):
        self.Iterar(etiqueta)
        self.Destruir()
        