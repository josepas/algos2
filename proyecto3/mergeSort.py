#!/usr/bin/python3
# Proyecto 3
#
# Algoritmo de Ordenamiento MergeSort 
#
# Autores:
#   Jose Pascarella     11-10743
#   Amin Arria          11-10053
#
# Ultima Modificacion: 19 / 12 / 2013

from random import *
import time





# Casos de prueba
for i in range(5):
    A = [randint(0,x) for x in range(1000000)]   
    x = time.time()
   
   
    print(time.time() - x)