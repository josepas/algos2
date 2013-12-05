# Proyecto 2
#
# Clase Evento 
#
# Autores:
#   Jose Pascarella     11-10743
#   Amin Arria          11-10053
#
# Ultima Modificacion: 5 / 12 / 2013

from Vehiculo import Vehiculo
from cola import *
from Tubo import Tubo
from random import *

class Evento:
    E = None
    def __init__(self, string):
        self.string = string
        if (self.string != ''):
            self.Procesar()
        
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
                s.write('--> No existe Tubo disponible' + '\n')
                aux = e.Generar()
                s.write('--> Se crea Tubo ' + str(aux.iden) + ' de capacidad ' + str(aux.capacidad) + ' y ocupacion ' + str(aux.ocupacion) + '\n') 
                s.write('--> Se coloca Tubo ' + str(aux.iden) + ' de ultimo en la cola de tubos de ' + e.nombre + '\n')
                s.write('--> Se corren los tubos hasta que el Tubo ' + str(aux.iden) + ' es el Primero' + '\n')
                e.Iterar(aux.iden)
            
            # Intento estacionar el carro en el tubo actual
            if ( e.Tope().Cabe(nuevo) ):
                e.Estacionar(nuevo)
                s.write('--> Se Estaciona Vehiculo ' + nuevo.placa + ' en Tubo ' + str(e.Tope().iden) + ' (ocupacion ' + str(e.Tope().ocupacion) + ')' + '\n')
            # Al no encontrar tubo con capacidad se crea uno nuevo
            else:
                s.write('--> Capacidad Tubo ' + str(e.Tope().iden) + ' Excedida' + '\n')
                aux = e.Generar()         
                e.Iterar(aux.iden)
                e.Estacionar(nuevo)
                s.write('--> Se crea Tubo ' + str(aux.iden) + ' de capacidad ' + str(aux.capacidad) + ' y ocupacion ' + str(aux.ocupacion) + '\n') 
                s.write('--> Se coloca Tubo ' + str(aux.iden) + ' de ultimo en la cola de tubos de '  +  e.nombre + '\n')
                s.write('--> Se corren los tubos hasta que el Tubo ' + str(aux.iden) + ' es el Primero' + '\n')
                s.write('--> Se Estaciona Vehiculo ' + nuevo.placa + ' en Tubo ' + str(e.Tope().iden) + ' (ocupacion ' + str(e.Tope().ocupacion) + ')' + '\n')
            s.write('\n')
            
        elif (codigo == 'R'):
            ## Lectura
            codigo, p, t = self.string.split()
           
            t = int(t)
            #
            # Retirar Vehiculos
            # Se verifica si el vehiculo existe en el Estacionamiento
            #
            
            if e.Existe(p, t):
                s.write('--> Vehiculo ' + p + ' EXISTE en Tubo ' + str(t) + '\n')
                s.write('--> Se corren los tubos hasta que el Tubo ' + str(t) + ' sea el Primero' + '\n')
                s.write('--> Se crea un Tubo auxiliar con capacidad de Tubo ' + str(t) + ' (' + str(e.Tope().capacidad) + ') y ocupacion 0' + '\n')
                
                # Se retira el vehiculo 
                e.Retirar(p, t)
                s.write('--> Se mueven Vehiculos del Tubo ' + str(t) + ' al Tubo auxiliar' + '\n')
                s.write('--> Sale Vehiculo ' + p + '\n')
                s.write('--> Se elimina Tubo ' + str(e.Tope().iden) + '\n')
                
                
                if ( e.Tope().iden == t ):
                    s.write('--> Tubo auxiliar es ahora Tubo ' + str(e.Tope().iden) + ' con ocupacion ' + str(e.Tope().ocupacion) + '\n')
                    s.write('--> Se coloca Tubo ' + str(e.Tope().iden) + ' de ultimo en la cola de tubos de ' + e.nombre + '\n')
                    s.write('--> Se corren los tubos hasta que el Tubo ' + str(e.Tope().iden) + ' sea el Primero' + '\n')
            else:
                s.write('--> NO EXISTE Vehiculo ' + p + ' en Tubo ' + str(t) + '\n')

            s.write('\n')
        
        elif (codigo == 'E'):
            # Lectura
            codigo, p, t = self.string.split()

            actual = e.Tope().iden
            t = int(t)

            if e.Existe(p, t):
                s.write('--> Vehiculo ' + p + ' EXISTE en Tubo ' + str(t) + '\n')
            else:
                s.write('--> NO EXISTE Vehiculo ' + p + ' en Tubo ' + str(t) + '\n')
            s.write('\n')

            e.Iterar(actual)
        
        elif (codigo == 'B'):
            # Lectura
            codigo, selec, valor = self.string.split()

            salida = e.Busqueda(selec, valor)
            s.write('--> Vehiculos de ' + selec + ' ' + valor + '\n')
            s.write(str(salida) + '\n')
            
        elif (codigo == 'K'):
            s.write('--> Se destruyen estacionamiento, tubos y vehiculos remanentes' + '\n')
            s.write('--> Adios' + '\n')
        
        s.close()
        Evento.E = e    
            

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
        tope = self.tam
        while(self.Tope().iden != i and cota < tope):
            self.Encolar(self.Tope())
            self.Desencolar()
            cota += 1
            
    def Estacionar(self, v):
        self.Tope().Estacionar(v)
        return self.Tope().iden

    def Existe(self, placa, ticket):
        self.Iterar(ticket)
        tubo = self.Tope()
        return tubo.Existe(placa)

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
                valor = float(valor)
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
    
    def ProcesarLlegadas(archivo):
        f = open(archivo, 'r')
        for i in f:
            h = Evento(i.strip())
        f.close()

Estacionamiento.ProcesarLlegadas("prueba.txt")
