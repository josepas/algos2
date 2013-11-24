class cola:
    def __init__(self,m):
        self.cont = []
   
    def Tope(self):
        return self.cont[0]
    
    def Encolar(self, nodo):
        self.cont.append(nodo)

    def Desencolar(self):
        self.cont.remove(self.cont[0])
    
    
  