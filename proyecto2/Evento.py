# Proyecto 2
#
# Clase Evento 
#
# Autores:
#   Jose Pascarella     11-10743
#   Amin Arria          11-10053
#
# Ultima Modificacion: 5 / 12 / 2013

from cola import *
from Estacionamiento import Estacionamiento
from Vehiculo import Vehiculo
    
class Evento:
    def __init__(self, string):
        self.string = string
        if (self.string != ''):
            self.Procesar() # Esto creo que dara problemas

    def ProcesarLlegadas(self, archivo):
        f = open(archivo, 'r')
        for i in f:
            h = Evento(i.strip())
        
    def Procesar(self):
        s = open('Traza.txt', 'a')
        codigo = self.string[0]
        
        if (codigo == 'C'):
            e = Estacionamiento()
            self.nombre = self.string.split()[-1].strip('.txt')
            s.write('--> Se crea Estacionamiento ' + self.nombre + '\n')
            s.close()
        elif (codigo == 'P'):
            # Lectura
            codigo, p, l, m, a, c = self.string.split()
            
            #
            #   Algoritmo para estacionar carros
            # 
            
            # Creacion del vehiculo desde el archivo
            nuevo = Vehiculo(p, l, m, a, c)
            s.write('--> Entra Vehiculo ' + p + ' de longitud ' + l + '\n')
            
            # Se verifica si el estacionamiento esta vacio
            if (e.cabeza == None):
                s.write('--> No existe Tubo disponible ' + '\n')
                aux = e.Generar()
                s.write('--> Se crea Tubo ' + aux.iden + ' de capacidad ' + aux.capacidad + ' y ocupacion ' + aux.ocupacion + '\n') 
                s.write('--> Se coloca Tubo ' + aux.iden + ' de ultimo en la cola de tubos de ' + self.nombre + '\n')
                s.write('--> Se corren los tubos hasta que el Tubo ' + aux.iden + ' es el Primero ' + '\n')
            
            # Intento estacionar el carro en el tubo actual
            estacionado = False
            if (e.ultimo.info.capacidad >= l):
                e.Estacionar(nuevo)
                estacionado = True
                s.write('--> Se Estaciona Vehiculo ' + nuevo.p + ' en Tubo ' + e.ultimo.info.iden + ' (ocupacion' + e.ultimo.info.ocupacion + ') ' + '\n')
            
            # Al no encontrar tubo con capacidad se crea uno nuevo
            if (not estacionado):
                s.write('--> Capacidad Tubo ' + e.ultimo.info.iden + ' Excedida' + '\n')
                aux = e.Generar()         
                s.write('--> Se crea Tubo ' + aux.iden + ' de capacidad ' + aux.capacidad + ' y ocupacion ' + aux.ocupacion + '\n') 
                s.write('--> Se coloca Tubo ' + aux.iden + ' de ultimo en la cola de tubos de '  +  self.nombre + '\n')
                s.write('--> Se corren los tubos hasta que el Tubo ' + aux.iden + ' es el Primero ' + '\n')
                s.write('--> Se Estaciona Vehiculo ' + nuevo.p + ' en Tubo ' + e.ultimo.info.iden + ' (ocupacion ' + e.ultimo.info.ocupacion + ') ' + '\n')
                
        
        elif (codigo == 'R'):
            ## Lectura
            codigo, p, t = self.string.split()
            
            #
            # Retirar Vehiculos
            #
            
            # Se verifica si el vehiculo existe en el Estacionamiento
            if e.Existe(p, t):
                s.write('--> Vehiculo ' + p + ' EXISTE en Tubo ' + t + '\n')
                s.write('--> Se corren los tubos hasta que el Tubo ' + t + ' sea el Primero ' + '\n')
                s.write('--> Se crea un Tubo auxiliar con capacidad de Tubo ' + t + ' (' + e.Tope().capacidad + ') y ocupacion 0' + '\n')

                # Se retira el vehiculo 
                e.Retirar(p, t)
                s.write('--> Se mueven Vehiculos del Tubo ' + t + ' al Tubo auxiliar ' + '\n')
                s.write('--> Sale Vehiculo ' + p + '\n')
                s.write('--> Se elimina Tubo ' + e.ultimo.info.iden + '\n')
                s.write('--> Tubo auxiliar es ahora Tubo ' + e.ultimo.info.iden + ' con ocupacion ' + e.ultimo.info.ocupacion + '\n')
                s.write('--> Se coloca Tubo ' + e.ultimo.info.iden + ' de ultimo en la cola de tubos de ' + self.nombre + '\n')
                s.write('--> Se corren los tubos hasta que el Tubo ' + e.ultimo.info.iden + ' sea el Primero ' + '\n')
                
            else:
                s.write('--> NO EXISTE Vehiculo ' + p + ' en Tubo ' + t + '\n')
                
                
        elif (codigo == 'E'):
            # Lectura
            codigo, p, t = self.string.split()

            if e.Existe(p, t):
                s.write('--> Vehiculo ' + p + ' EXISTE en Tubo ' + t + '\n')
            else:
                s.write('--> NO EXISTE Vehiculo ' + p + ' en Tubo ' + t + '\n')
        
        
        elif (codigo == 'B'):
            # Lectura
            codigo, selec, valor = self.string.split()

            salida = e.Busqueda(selec, valor)
            s.write('--> Vehiculos de ' + selec + ' ' + valor + '\n')
            salida.Imprimir()

            
        elif (codigo == 'K'):
            s.write('--> Se destruyen estacionamiento, tubos y vehiculos remanentes' + '\n')
            s.write('--> Adios' + '\n')
            s.close()

Evento('h').ProcesarLlegadas('casoDePrueba.txt')


            
        
        