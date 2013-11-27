class pila:
    def __init__(self):
        self.cont = []
        
    def Tope(self):
        return self.cont[-1]
    
    def Empilar(self, nodo):
        self.cont.append(nodo)
           
    def Desempilar(self):
        self.cont.remove(self.cont[-1])
    
