class pila:
    def __init__(self,m):
        self.cont = []
        self.tam = 0
        self.MAX = m
        
    def vacia(self):
        return (self.tam == 0)
    
    def empilar(self, nodo):
        if (self.tam < self.MAX):
            self.cont.append(nodo)
            self.tam += 1
        else:
            print('La pila esta llena')
   
    def desempilar(self):
        if not self.vacia():
            self.tam -= 1
            return self.cont.pop()
        print('La pila esta vacia')
    