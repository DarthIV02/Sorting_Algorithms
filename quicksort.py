# QUICK SORT

# Realizar el algoritmo de ordenamiento por ordenación rápida
# Equipo 4: Ivannia Gomez, Alberto Ortega, Samuel Zazueta

# int cor = iterativo que marca el numero de corridas, l = índice del valor que inicia la sublista a ordenar,
# r = donde termina la sublista que se va a ordenar, m = regresa el valor del índice donde se encuentra el pivote ya ordenado,
# x = el valor del pivote de la sublista que se va a ordenar, j = último índice de los valores menores al pivote,
# i = índice del número que se va a ir comparando con el pivote, int start y stop = los bordes de tener para los números random,
# n = longitud del array con números random ingresada por el usuario
# array numberList = lista de números aleatorios entre 1 y 100, de longitud n que se va a ordenar,
# array = parámetro de array que se va a ordenar,

from random import randint

cor = 0

def QuickSort(array, l, r):
    global cor
    if l>=r: #Checa que la lista no sea de 1 valor, si es 1 implica que ya no hay subarreglo y se regresa
        return
    m = Partition(array, l, r) # Partition regresa el índice del pivote, y se guarda en m
    cor += 1 # Se le aumenta una corrida
    print(f"En la corrida {cor}: {array}, el pivote es {array[m]}")
    QuickSort(array, l, m) # Hace Quicksort de los números menores que el pivote
    QuickSort(array, m+1, r) # Hace Quicksort de los números mayores que el pivote

def Partition(array, l, r):
    x = array[l] # Valor del pivote
    j = l # Último índice de los valores menores al pivote
    for i in range(l+1, r):
        if array[i]<=x: # Checa si el número que se revisa (se revisan todos), es menor al x
            j += 1 # Si es así entonces el índice se recorre 1
            array[j], array[i] = array[i], array[j] # Se intercambia el array[i], con el número en el índice del límite de los menores
    array[l], array[j] = array[j], array[l] # Se intercambia el pivote con el valor que se encuentra en el límite de los menores
    return j # Regresar el índice del pivote

start = 0
stop = 101

# Se hace un ciclo infinito que pregunta por n, hasta que el número se encuentra entre el rango establecido (1 al 50)
# de ahí se rompe y sigue con el código

while True:
    n = int(input("Inserta el número de elementos: "))
    if n>50 or n<1:
        print("El número de elementos tiene que estar entre 1 y 50")
    else:
        break

# Explicación: Crea una lista random de n elementos entre el rango 1 y 100, se imprime la lista no ordenada,
# esa lista entra a la función de QuickSort, se ordena y se imprime esa lista ordenada

numberList = [randint(start, stop) for _ in range(n)]

print(f"Tu lista es: {numberList}")

QuickSort(numberList, 0, n)

print(f"Tu lista ordenada es: {numberList}")

# ÚLTIMA MODIFICACIÓN
# 9:45 el 26 de agosto de 2021, por Ivannia Gomez
# linea 60