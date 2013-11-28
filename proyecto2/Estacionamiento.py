from cola import cola
from random import *

class Estacionamiento(cola):
   i = 0
   def __init__(self):
      random.seed()
      self.iden = Estacionamiento.i
      Estacionamiento.i += 1 
      super().__init__() #inicializa la cola
