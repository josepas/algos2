# Descripción: Módulo con la implementación de algoritmos de ordenamientos
#              que son aplicados sobre listas de elementos que son comparables
#              entre sí. Al aplicar algún algoritmo de ordenamiento, la lista a ordenar
#              es copiada y se retorna una nueva lista con los elementos ordenados.
# Autor: Guillermo Palma
# email: gvpalma@usb.ve
# version 0.1


# Todos los algoritmos de ordenamiento tienen los siguentes parámetros
# Parámetros: seq: objeto lista de python que contiene elementos comparables
#
#             cmpf: Función que compara dos elementos de la lista.
#             Esta función es llamada repetidamente por los algoritmos de ordenamiento
#             para comparar dos elementos. La función cmpf toma como argumento
#             dos elementos de la lista, y retorna un número entero. Su prototipo es:
#             cmpf(x, y) --> int
#             El  número entero  define el orden
#             de los elementos de la siguiente manera:
#                 cmpf(x, y) < 0 : significa que el elemento x va antes del elemento y
#                 cmpf(x, y) > 0 : significa que el elemento x va después del elemento y
#                 cmpf(x, y) = 0 : significa que los elementos x, y son equivalentes

from random import *

def cmpf(x,y):
    return (x - y)


# Ordenamiento por Inserción
def insertion(seq, cmpf):
    n = len(seq)
    for i in range(1, n) :
        value = seq[i]
        pos = i
        while pos > 0 and cmpf(value, seq[pos - 1]) < 0 :
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value

# Ordenamiento por Quicksort
def Particionar(A, izq, der, cmpf):
    # Seleccion aleatoria del pivote
    pivot = randint(izq, der)
    valorP = A[pivot]
    # Paso el pivot a la posicion final para que no estorbe
    A[pivot], A[der] = A[der], A[pivot]
    m = izq
    for i in range(izq, der):
        if(cmpf(A[i], valorP) <= 0):
            A[i], A[m] = A[m], A[i]
            m += 1
    # Coloco el pivote en su posicion final
    A[der], A[m] = A[m], A[der]
    return m
    
def quicksort(seq, cmpf, izq=-1, der=-1):
    A = seq
    if(der==-1 and izq==-1):
        quicksort(A, cmpf, 0, len(A)-1)
    if (izq < der):
        pivot = Particionar(A, izq, der, cmpf)
        quicksort(A, cmpf, izq , pivot - 1)
        quicksort(A, cmpf, pivot + 1, der)
    return A

# Ordenamiento por Mergeort
def mergesort(seq, cmpf):
    A = seq
    if(len(A) == 1):
        return A
    m = len(A) // 2
    izq = mergesort(A[:m], cmpf)
    der = mergesort(A[m:], cmpf)
    i, j = 0, 0
    final = []
    while(i < len(izq) and j < len(der)):
        if(cmpf(izq[i],der[j]) <= 0):
            final.append(izq[i])
            i += 1
        else:
            final.append(der[j])
            j += 1
    if(i < len(izq)):
        final += izq[i:]
    if(j < len(der)):
        final += der[j:]
    return final

# Ordenamiento por Heapsort
def Heapify(A, i, n, cmpf):
    if (2 * i + 1 > n):
        return
    if (2 * i + 2 > n):
        k = 2 * i + 1
    else:
        if(cmpf(A[2*i + 1], A[2*i + 2]) > 0):
            k = 2 * i + 1
        else:
            k = 2 * i + 2
    
    if(cmpf(A[k],A[i]) > 0):
        A[k], A[i] = A[i], A[k]
        Heapify(A,k,n,cmpf)
        
def ConstruirHeap(A,n,cmpf):
    for i in range(n // 2, -1, -1):  
        Heapify(A,i,n,cmpf)
    
def heapsort(seq, cmpf):
    A = seq
    n = len(A)-1
    ConstruirHeap(A,n,cmpf)
    print(A) # borrar
    for i in range(n, 0, -1):
        A[0], A[i] =  A[i], A[0]
        Heapify(A, 0, i - 1, cmpf)
    print(A) # borrar
    return A

# Ordenamiento por Bubblesort0
def bubblesort0(seq, cmpf):
    A = seq
    n = len(A)
    cambio = True
    while cambio:
        cambio = False
        for i in range(n-1):
            if(cmpf(A[i],A[i+1]) > 0):
                A[i], A[i+1] = A[i+1], A[i]
                cambio = True
    return A

# Ordenamiento por Bubblesort1
def bubblesort1(seq, cmpf):
    A = seq
    n = len(A)
    cambio = True
    while cambio:
        cambio = False
        for i in range(n-1):
            if (cmpf(A[i],A[i+1]) > 0): 
                A[i], A[i+1] = A[i+1], A[i]
                cambio = True
        n -= 1
    return A

    
a = [randint(0,20) for x in range(20)]
print(a)
quicksort(a,cmpf)   
print(a)
    
    