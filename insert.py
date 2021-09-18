# INSERTION SORT

# Realizar el algoritmo de ordenamiento por selección
# Equipo 7: Ivannia Gomez, Samuel Zazueta, Manuel Martín del Campo

# int start y stop = los bordes de tener para los números random, n = longitud del array con números random
# ingresada por el usuario, i = índice de la llave, aux = número de la llave, #a = índice del último número
# de la lista ordenada
# array numberList = lista de números aleatorios entre 1 y 100, de longitud n que se va a ordenar

from random import randint

def InsertSort(array,n):
    for i in range(1,n): # Va cambiando el índice de la llave que se va a ir insertando en su posición correcta
        aux = array.pop(i) # Se elimina ese índice, y se guarda en aux
        a = i-1 # Se establece a como el índice anterior a la llave como a, que indica donde termina la sublista ordenada
        while a >= 0 and array[a]>aux: # Se revisa que números son mayores a la llave para determinar en que posición
                                        # se va a insertar
            a-=1
        array.insert(a+1, aux) # Se inserta dicha llave en el arreglo
        print(f"Corrida {i}: {array}, con la llave {aux}")
    return array

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
# esa lista entra a la función de InsertSort, se ordena y se imprime

numberList = [randint(start, stop) for _ in range(n)]

print(f"Tu lista es: {numberList}")

print(f"Tu lista ordenada es: {InsertSort(numberList, n)}")

# ÚLTIMA MODIFICACIÓN
# 9:50 el 24 de agosto de 2021, por Ivannia Gomez
# linea 21