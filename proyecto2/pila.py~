class Nodo:
    def __init__(self, info):
        self.info = info
        self.sig = None


class Pila:
    def __init__(self):
        self.cabeza = None
        self.tam = 0
        
    def Tope(self):
        return self.cabeza.info
        
    def Empilar(self, nodo):
        nuevo = Nodo(nodo)
        if (self.tam == 0):
            self.cabeza = nuevo 
        else:
            nuevo.sig = self.cabeza
            self.cabeza = nuevo
        self.tam += 1
        
    def Desempilar(self):
        assert(self.tam > 0)    
        salida = self.cabeza.info
        self.cabeza = self.cabeza.sig
        self.tam -= 1
        return salida
            
    def Vacia(self):
        return (self.tam == 0)

    def Imprimir(self):
        aux = self.cabeza
        while (aux != None):
            print(aux.info)
            aux = aux.sig