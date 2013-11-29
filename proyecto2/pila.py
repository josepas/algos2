class Pila:
    def __init__(self):
        self.cont = []
        self.tam = 0
        
    def Tope(self):
        return self.cont[-1]
    
    def Empilar(self, nodo):
        self.cont.append(nodo)
        self.tam += 1
        
    def Desempilar(self):
        if (self.tam > 0):
            self.cont.remove(self.cont[-1])
            self.tam -= 1
            
    def Vacia(self):
        return self.tam == 0
