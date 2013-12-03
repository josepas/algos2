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
    E = None
    def __init__(self, string):
        self.string = string
        if (self.string != ''):
            self.Procesar()

    def ProcesarLlegadas(self, archivo):
        f = open(archivo, 'r')
        for i in f:
            h = Evento(i.strip())
        
    def Procesar(self):
        e = Evento.E
        s = open('Traza.txt', 'a')
        codigo = self.string[0]
        
        if (codigo == 'C'):
            nombre = self.string.split()[-1].strip('.txt')
            e = Estacionamiento(nombre)
            s.write('--> Se crea Estacionamiento ' + e.nombre + '\n')
            s.write('\n')

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
            if ( e.Vacia() ):
                s.write('--> No existe Tubo disponible ' + '\n')
                aux = e.Generar()
                s.write('--> Se crea Tubo ' + str(aux.iden) + ' de capacidad ' + str(aux.capacidad) + ' y ocupacion ' + str(aux.ocupacion) + '\n') 
                s.write('--> Se coloca Tubo ' + str(aux.iden) + ' de ultimo en la cola de tubos de ' + e.nombre + '\n')
                s.write('--> Se corren los tubos hasta que el Tubo ' + str(aux.iden) + ' es el Primero ' + '\n')
                e.Iterar(aux.iden)
            
            # Intento estacionar el carro en el tubo actual
            if ( e.Tope().Cabe(nuevo) ):
                e.Estacionar(nuevo)
                s.write('--> Se Estaciona Vehiculo ' + nuevo.placa + ' en Tubo ' + str(e.Tope().iden) + ' (ocupacion' + str(e.Tope().ocupacion) + ') ' + '\n')
            # Al no encontrar tubo con capacidad se crea uno nuevo
            else:
                s.write('--> Capacidad Tubo ' + str(e.Tope().iden) + ' Excedida' + '\n')
                aux = e.Generar()         
                e.Iterar(aux.iden)
                e.Estacionar(nuevo)
                s.write('--> Se crea Tubo ' + str(aux.iden) + ' de capacidad ' + str(aux.capacidad) + ' y ocupacion ' + str(aux.ocupacion) + '\n') 
                s.write('--> Se coloca Tubo ' + str(aux.iden) + ' de ultimo en la cola de tubos de '  +  e.nombre + '\n')
                s.write('--> Se corren los tubos hasta que el Tubo ' + str(aux.iden) + ' es el Primero ' + '\n')
                s.write('--> Se Estaciona Vehiculo ' + nuevo.placa + ' en Tubo ' + str(e.Tope().iden) + ' (ocupacion ' + str(e.Tope().ocupacion) + ') ' + '\n')
            s.write('\n')
            
        elif (codigo == 'R'):
            ## Lectura
            codigo, p, t = self.string.split()
            
            #
            # Retirar Vehiculos
            # Se verifica si el vehiculo existe en el Estacionamiento
            #
            
            if e.Existe(p, t):
                s.write('--> Vehiculo ' + p + ' EXISTE en Tubo ' + str(t) + '\n')
                s.write('--> Se corren los tubos hasta que el Tubo ' + str(t) + ' sea el Primero ' + '\n')
                s.write('--> Se crea un Tubo auxiliar con capacidad de Tubo ' + str(t) + ' (' + str(e.Tope().capacidad) + ') y ocupacion 0' + '\n')
                
                # Se retira el vehiculo 
                e.Retirar(p, t)
                s.write('--> Se mueven Vehiculos del Tubo ' + str(t) + ' al Tubo auxiliar ' + '\n')
                s.write('--> Sale Vehiculo ' + p + '\n')
                s.write('--> Se elimina Tubo ' + str(e.Tope().iden) + '\n')
                
                
                if ( e.Tope().iden == t ):
                    s.write('--> Tubo auxiliar es ahora Tubo ' + str(e.Tope().iden) + ' con ocupacion ' + str(e.Tope().ocupacion) + '\n')
                    s.write('--> Se coloca Tubo ' + str(e.Tope().iden) + ' de ultimo en la cola de tubos de ' + e.nombre + '\n')
                    s.write('--> Se corren los tubos hasta que el Tubo ' + str(e.Tope().iden) + ' sea el Primero ' + '\n')
            else:
                s.write('--> NO EXISTE Vehiculo ' + p + ' en Tubo ' + str(t) + '\n')

            s.write('\n')
        
        elif (codigo == 'E'):
            # Lectura
            codigo, p, t = self.string.split()

            if e.Existe(p, t):
                s.write('--> Vehiculo ' + p + ' EXISTE en Tubo ' + str(t) + '\n')
            else:
                s.write('--> NO EXISTE Vehiculo ' + p + ' en Tubo ' + str(t) + '\n')
            s.write('\n')
        
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
        
        Evento.E = e    
            
Evento('h').ProcesarLlegadas('casoDePrueba.txt')


            
        
        