#!/usr/bin/env python3
# coding=utf-8

# Descripción: Cliente que prueba algoritmos de ordenamiento
#     	       con listas de enteros con valores aleatorios
# Autor: Guillermo Palma
# email: gvpalma@usb.ve
# version 0.1

import sys, traceback, random, time
from ordenamiento import *

# Descripción: Procesa la línea de comandos del programa
# Parametros: args: Arreglo de strings con los argumentos de la línea de comando
# La sipnosis de la línea de comandos es:
#
# pruebaOrdenamiento [all|nlgn] <numero de pruebas> <numero de elementos>
#
# donde  [all|nlgn] es el tipo de algoritmos a ejecutar. Con la opción "nlgn" se ejecutaran
# los algoritmos de orden de ejecución O(nlogn)  y con "all" todos los algoritmos. Se tiene
# que <numero de pruebas> es el número de pruebas que se realizan sobre los algoritmos de
# ordenamiento. El <numero de elementos> indica el número de elementos que va a tener el
# arreglo a ordenar
#
# Pre: Deben ser 3 argumentos y tienen el orden: [all|nlgn] <numero de pruebas> <numero de elementos>.
#
# Retorna: La tubla ("tipo de algoritmos a correr", "numero de pruebas", "numero de elementos")

def parseArgs(args):
    msg = "Error en la linea de comando:\npruebaOrdenamiento [all|nlgn] <numero de pruebas> <numero de elementos>"
    if len(args) != 4:
        print(msg)
        sys.exit(1)

    if (args[1] != "all" and args[1] != "nlgn"):
        print(msg)
        sys.exit(1)

    return args[1], int(args[2]), int(args[3])

# Descripción: Crea arreglo con n valores enteros
#     	       que son generados de forma aleatoria
# Parametros: n: Número de elementos del arreglo
# Retorna: Un objeto lista con n valores enteros aleatorios entre 0 y 1000000

def obtenerArregloEnteros(n):
    A = [random.randint(0, 1000000) for x in range(n)]
    return A

# Descripción: Comprueba si un arreglo esta ordenado.
# Parametros: a: objeto lista
# Retorna: True si el arreglo está ordenado, False en caso contrario.

def estaOrdenado(a):
    n = len(a)
    for i in range(n-1):
        if (a[i] > a[i+1]):
            return False
    return True

# Descripción: Prueba los algoritmos de ordenamientos con una lista de elementos.
# Se crea un objeto Ordenamiento y se luego se ejecutan que se hayan indicado
#
# Parametros: datos: objeto lista con elementos de un tipo determinado
#             fcmp: función que compara dos elementos del tipo lista
#             tipo: indica el tipo de algoritmos que se van a correr.
#             si tipo = "all" se ejecutan todos los algoritmos que son
#             proporcionados por el módulo ordenamiento, si tipo = "nlgn"
#             se ejecutan los algoritmos con tiempo de ejecución promedio O(nlgn)
#
# Retorna: Una tupla con los tiempos de ejecución, en segundos, de los algoritmos.
# Se retorna una tupla de pares, donde el el primer par
# es una etiqueta con nombre del algoritmo y el segundo es el tiempo de ejecución en segundos.
# Por ejemplo si tipo = "nlgn", entonces la tupla tiene la forma:
# (("QuickSort", tiempo-QS), ("MergeSort", tiempo-MS) ("HeapSort", tiempo-HS))
# Las etiquetas utilizadas son: "IsertionSort", "BubbleSort0", "BubbleSort1", "QuickSort", "MergeSort" y "HeapSort"

def probarAlgoritmos(datos, fcmp, tipo):

    if tipo == "all" :
        print("Comenzando InsertionSort")
        start_time = time.time()
        arrayResult = list(datos)
        insertion(arrayResult, fcmp)
        assert(estaOrdenado(arrayResult))
        timeIsertion = time.time() - start_time

        print("Comenzando BubbleSort0")
        start_time = time.time()
        arrayResult = list(datos)
        bubbleSort0(arrayResult, fcmp)
        assert(estaOrdenado(arrayResult))
        timeBubbleSort0 = time.time() - start_time

        print("Comenzando BubbleSort1")
        start_time = time.time()
        arrayResult = list(datos)
        bubbleSort1(arrayResult, fcmp)
        assert(estaOrdenado(arrayResult))
        timeBubbleSort1 = time.time() - start_time

        time_N_2 = (("IsertionSort", timeIsertion), ("BubbleSort0", timeBubbleSort0), ("BubbleSort1", timeBubbleSort1))
    else :
        time_N_2 = ()

    print("Comenzando QuickSort")
    start_time = time.time()
    arrayResult = list(datos)
    quickSort(arrayResult, fcmp)
    assert(estaOrdenado(arrayResult))
    timeQuickSort = time.time() - start_time

    print("Comenzando MergeSort")
    start_time = time.time()
    arrayResult = list(datos)
    mergeSort(arrayResult, fcmp)
    assert(estaOrdenado(arrayResult))
    timeMergeSort = time.time() - start_time

    print("Comenzando HeapSort")
    start_time = time.time()
    arrayResult = list(datos)
    heapSort(arrayResult, fcmp)
    assert(estaOrdenado(arrayResult))
    timeHeapSort = time.time() - start_time

    time_N_lg_N = (("QuickSort", timeQuickSort), ("MergeSort", timeMergeSort), ("HeapSort", timeHeapSort))

    # print(time_N_lg_N + time_N_2)  Solo como muestra, eliminar para la entrega

    return time_N_lg_N + time_N_2

# Descripción: Compara dos números enteros.
#              Con esta función se quiere ordenar los elementos
#              de una lista ascendentemente.
# Parametros: x, y: Elementos de tipo numérico
# Retorna: El valor de (x-y)

def comparadorNumerico1(x, y):
    return x - y

# Descripción: Compara dos números enteros.
#              Con esta función se quiere ordenar los elementos
#              de una lista descendentemente.
# Parametros: x, y: Elementos de tipo numérico
# Retorna: El valor de (y-x)

def comparadorNumerico2(x, y):
    return y - x

# Descripción: Ejecuta o prueba los algoritmos de ordenamiento un número
#              de veces determinado.
# Parametros: numPruebas: Número de veces que se van a ejecutar los algoritmos
#                         de ordenamiento.
#              numElems: Número de elementos numéricos que contiene la lista a generar
#              tipo: string con el tipo de algoritmos a ejecutar. Puede ser "all" o "nlgn"
# Retorna: Retorna una lista cuyos elementos son tuplas de pares con los nombres y tiempo de ejecución
# de los algoritmos de ordenamiento. Cada elemento de la lista corresponde a los resultados de una prueba

def realizarPruebas(numPruebas, numElems, tipo):
    datos = []
    resultadosPruebas = []
    for i in range(numPruebas) :
        print("\nComenzando la prueba: "+str(i+1))
        datos = obtenerArregloEnteros(numElems)
        r = probarAlgoritmos(datos, comparadorNumerico1, tipoDeCorrida)
        # r = probarAlgoritmos(datos, comparadorNumerico1, tipoDeCorrida) # Probar
        resultadosPruebas.append(r)
    return resultadosPruebas

# Descripción: Dado una serie de resultados de pruebas sobre
# algoritmos de ordenamientos, calcula e imprime por la salida
# estándar, el tiempo promedio de ejecución de cada algoritmo
# y el valor de su desviación estándar.
#
# Parametros: results: lista con los resultados de cada una de
#             las pruebas o ejecuciones hechas a los algoritmos de ordenamiento.
#             Cada una de las pruebas es una tupla con los resultados de una
#             ejecución de varios algoritmos.
#
# Retorna: Imprime por la salida estándar el tiempo promedio de ejecución de cada
#           uno de los algoritmos probados, junto con la desviación estándar.

def procesarResultados(results):
    
    print("")
    quick = [0.0, 0.0]
    merge = [0.0, 0.0]
    heap = [0.0, 0.0]
    bubble0 = [0.0, 0.0]
    bubble1 = [0.0, 0.0]
    insert = [0.0, 0.0]
    
    # Promedio
    for i in results:
        quick[0] += i[0][1]
        merge[0] += i[1][1]
        heap[0] += i[2][1]
        if len(i) > 3:
            insert[0] += i[3][1]
            bubble0[0] += i[4][1]
            bubble1[0] += i[5][1]

    quick[0] /= len(results)
    merge[0] /= len(results)        
    heap[0] /= len(results)
    insert[0] /= len(results)
    bubble0[0] /= len(results)
    bubble1[0] /= len(results)
    
    # Desviacion estandar
    for i in results:
        quick[1] += (quick[0] - i[0][1]) ** 2
        merge[1] += (merge[0] - i[1][1])
        heap[1] += (heap[0] - i[2][1]) ** 2
        if len(i) > 3:
            insert[1] += (insert[0] -  i[3][1]) ** 2
            bubble0[1] += (bubble0[0] -  i[4][1]) ** 2
            bubble1[1] += (bubble1[0] - i[5][1]) ** 2

    quick[1] = ( quick[1] / (len(results) - 1) ) ** (1/2)
    merge[1] = ( merge[1] / (len(results) - 1) ) ** (1/2)
    heap[1] = ( heap[1] / (len(results) - 1) ) ** (1/2)
    insert[1] = ( insert[1] / (len(results) - 1) ) ** (1/2)
    bubble0[1] = ( bubble0[1] / (len(results) - 1) ) ** (1/2)
    bubble1[1] = ( bubble1[1] / (len(results) - 1) ) ** (1/2)
    
    print('QuickSort\t | Tiempo promedio:', round(quick[0],2), '  \tDesviacion Estandar:', round(quick[1],2))
    print('MergeSort\t | Tiempo promedio:', round(merge[0],2), '  \tDesviacion Estandar:', round(merge[1],2))
    print('HeapSort\t | Tiempo promedio:', round(heap[0],2), '  \tDesviacion Estandar:', round(heap[1],2))
    print('InsertionSort\t | Tiempo promedio:', round(insert[0],2), ' \tDesviacion Estandar:', round(insert[1],2))
    print('BubbleSort(0)\t | Tiempo promedio:', round(bubble0[0],2), ' \tDesviacion Estandar:', round(bubble0[1],2))
    print('BubbleSort(1)\t | Tiempo promedio:', round(bubble1[0],2), '  \tDesviacion Estandar:', round(bubble1[1],2))
    
################################
## Inicio de la Aplicación    ##
################################

if __name__ == "__main__":
    tipoDeCorrida, numPruebas, numElems = parseArgs(sys.argv)
    results = realizarPruebas(numPruebas, numElems, tipoDeCorrida)
    procesarResultados(results)

