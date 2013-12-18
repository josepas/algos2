#!/usr/bin/python3
# Proyecto 3
#
# Algoritmo de Ordenamiento QuickSort 
#
# Autores:
#   Jose Pascarella     11-10743
#   Amin Arria          11-10053
#
# Ultima Modificacion: 19 / 12 / 2013

from random import *
import time

def Particionar(A, izq, der):
    # Seleccion aleatoria del pivote
    pivot = der
    valorP = A[pivot]
    # Paso el pivot a la posicion final para que no estorbe
    m = izq
    for i in range(izq, der):
        if (A[i] <= valorP):
            A[i], A[m] = A[m], A[i]
            m += 1
    # Coloco el pivote en su posicion final
    A[der], A[m] = A[m], A[der]
    return m
    
def QuickSort(A, izq, der):
    if (izq < der):
        pivot = Particionar(A, izq, der)
        QuickSort(A, izq , pivot - 1)
        QuickSort(A, pivot + 1, der)

A = [randint(0,10) for i in range(100)]
start_time = time.time()
QuickSort(A, 0, len(A)-1)
print(A)
print(time.time() - start_time)



