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
        return self.cabeza
    
    def Encolar(self, nodo):
        nuevo = Nodo(nodo)
        if (self.tam = 0):
            self.cabeza = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.sig = nuevo
            self.ultimo = self.ultimo.sig
        self.tam += 1
    
    def Desencolar(self):
        assert(self.tam > 0)
        if (self.tam = 1):
            self.ultimo = None
            self.cabeza = None
        else:
            self.cabeza = self.cabeza.sig
        self.tam -= 1
            
    def Vacia(self):
        return (self.tam == 0)
    
  
