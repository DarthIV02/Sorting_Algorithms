# SELECTION SORT

# Realizar el algoritmo de ordenamiento por selección
# Equipo 5: Ivannia Gomez, David Roldan, Michelle Muñiz

# int start y stop = los bordes de tener para los números random, n = longitud del array con números random
# ingresada por el usuario, i = Número que va ir intercambiandolo con el menor, va a ir camiando cada pasada
# minIndex = Variable que guarda el índice del menor número
# j = El número con el cual se va a ir comparando el minIndex
# array numberList = Lista con los números random

from random import randint

def SelectionSort(A, n):
    for i in range(n-1):    # Se hace un ciclo para identificar la posición del número con la que se va a cambiar el menor
        minIndex = i    # Inicializa minIndex como i
        for j in range(i+1, n):
            if A[j]<A[minIndex]:    # Compara si hay algún número menor que el que se encuentra en la posición del
                                    # minIndex después de i
                minIndex = j    # Si existe un número menor se establece su índice como el nuevo minIndex
        A[i], A[minIndex] = A[minIndex], A[i]   # Una vez revisados todos los números se cambian el menor con el
                                                # que esta en la posición de i
        print(f"Corrida {i+1}: {A}")
    return A

start = 0
stop = 101
n = int(input("Inserta el número de elementos: "))

# Explicación: Crea una lista random, se imprime la lista no ordenada, esa lista entra a la función de SelectionSort,
# se ordena y se imprime

numberList = [randint(start, stop) for _ in range(n)]

print(f"Tu lista es: {numberList}")

print(f"Tu lista ordenada es: {SelectionSort(numberList, n)}")

#Indices importantes = i, k, min

# ÚLTIMA MODIFICACIÓN
# 4:52 el 19 de agosto de 2021, por Ivannia Gomez
# linea 23

