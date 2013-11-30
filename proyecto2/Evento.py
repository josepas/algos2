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
            s.write('--> Se crea Estacionamiento', nombre)
        
        elif (codigo == 'P'):
            #
            #   Algoritmo para estacionar carros
            #   
            
            # Creacion del vehiculo desde el archivo
            codigo, p, l, m, a, c = self.string.split()
            nuevo = Vehiculo(p, l, m, a, c)
            s.write('--> Entra Vehiculo', p, 'de longitud', l)
            
            # Se verifica si el estacionamiento esta vacio
            if (e.cabeza == None):
                s.write('--> No existe Tubo disponible')
                aux = e.Generar()
                s.write('--> Se crea Tubo', aux.iden ,'de capacidad', aux.capacidad, ' y ocupacion', aux.ocupacion) 
                s.write('--> Se coloca Tubo', aux.iden, 'de ultimo en la cola de tubos de', nombre)
                s.write('--> Se corren los tubos hasta que el Tubo', aux.iden, 'es el Primero')
            
            # Intento estacionar el carro en el tubo actual
            estacionado = False
            if (e.ultimo.info.capacidad >= l):
                e.Estacionar(nuevo)
                estacionado = True
                s.write('--> Se Estaciona Vehiculo' nuevo.p, 'en Tubo' e.ultimo.info.iden, '(ocupacion', e.ultimo.info.ocupacion, ')')
            
            # Al no encontrar tubo con capacidad se crea uno nuevo
            if (not estacionado):
                s.write('--> Capacidad Tubo', e.ultimo.info.iden, 'Excedida')
                aux = e.Generar()         
                s.write('--> Se crea Tubo', aux.iden ,'de capacidad', aux.capacidad, ' y ocupacion', aux.ocupacion) 
                s.write('--> Se coloca Tubo', aux.iden, 'de ultimo en la cola de tubos de', nombre)
                s.write('--> Se corren los tubos hasta que el Tubo', aux.iden, 'es el Primero')
                s.write('--> Se Estaciona Vehiculo' nuevo.p, 'en Tubo' e.ultimo.info.iden, '(ocupacion', e.ultimo.info.ocupacion, ')')
                
        
        elif (codigo == 'R'):     
            
        elif (codigo == 'E'):
        
        elif (codigo == 'B'):
        
        elif (codigo == 'K'):
            

            
        
        