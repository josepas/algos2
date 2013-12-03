# Proyecto 2
#
# Clase Cola 
#
# Autores:
#   Jose Pascarella     11-10743
#   Amin Arria          11-10053
#
# Ultima Modificacion: 5 / 12 / 2013

class Nodo:
    def __init__(self, info):
        self.info = info
        self.sig = None
        
class Cola:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tam = 0
        
    def Tope(self):
        return self.cabeza.info
    
    def Encolar(self, nodo):
        nuevo = Nodo(nodo)
        if (self.tam == 0):
            self.cabeza = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.sig = nuevo
            self.ultimo = self.ultimo.sig
        self.tam += 1
    
    def Desencolar(self):
        assert(self.tam > 0)
        salida = self.cabeza.info
        if (self.tam == 1):
            self.cabeza = None
            self.ultimo = None
        else:
            self.cabeza = self.cabeza.sig
        self.tam -= 1
        return salida
            
    def Vacia(self):
        return (self.tam == 0)
        
    def Imprimir(self):
        print('------------------------- Hola entre a Cola.Imprimir() --------------------') #borrar
        aux = self.cabeza
        while (aux != None):
            print('------------------------- Hola mas adentro() --------------------') #borrar
            print(aux.info)
            aux = aux.sig
    
    def __str__(self):
        aux = ""
        i = self.cabeza
        while(i != None):
            aux += str(i.info)
            i = i.sig
        return aux
