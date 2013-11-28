from pila import pila
import random

random.seed()

class Tubo(pila):
   i = 0 
   def __init__(self, iden=-1, c=-1):
      if(iden == -1):
         self.iden = Tubo.i
         Tubo.i += 1
      else:
         self.iden = iden
      
      if(c == -1):
         self.capacidad = random.randint(5,25)
      else:
         self.capacidad = c

      super().__init__() #inicializa la pila
      self.ocupacion = 0
      
   def Cabe(self):
      return None

   def Estacionar(self, v):
      if (self.ocupacion < self.capacidad):
         self.Empilar(v)
         self.ocupacion += v.longitud

    def Retirar(self, v):
    
    
    def Cercano(self):
	self.Tope
    
    def Existe(self):