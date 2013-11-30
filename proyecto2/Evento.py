from Estacionamiento import Estacionamiento
from cola import Cola
from Tubo import Tubo
from Evento import Evento
from Vehiculo import Vehiculo
from random import *

f = open('casoDePrueba.txt', 'r')
s = open('salida.txt'. 'w')

for i in f:
    print(i.strip())
    h = Evento(i.strip())



class Evento:
    def __init__(self, string):
        self.string = string
        self.Procesar()

    def Procesar(self):
        codigo = self.string[0]
        
        if (codigo == 'C'):
            e = Estacionameinto()
            s.write('--> Se crea Estacionamiento')
        
        elif (codigo == 'P'):
            codigo, p, l, m, a, c = self.string.split()
            nuevo = Vehiculo(p, l, m, a, c)
            s.write('--> Entra Vehiculo', p, 'de longitud', l)
            
            
            
            
            
        elif (codigo == 'B'):     
        
        elif (codigo == 'E'):
        
        elif (codigo == 'R'):
        
        elif (codigo == 'K'):

            
        
        