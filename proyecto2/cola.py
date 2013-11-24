class cola:
    def __init__(self,m):
        self.cont = []
        self.tam = 0
        
    def vacia(self):
        return (self.tam == 0)
    
    def tope(self):
        if (self.tam > 0):
            return self.cont[0]
        print('Cola vacia')
    
    def encolar(self, nodo):
            self.cont.append(nodo)
            self.tam += 1
   
    def desencolar(self):
        if not self.vacia():
            self.tam -= 1
            self.cont.remove(self.cont[0])
            return
        print('Cola vacia')
    
    
  