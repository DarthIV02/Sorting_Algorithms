# MERGE SORT

# Realizar el algoritmo de ordenamiento por mezcla
# Equipo 4: Ivannia Gomez, Alex Machado, Carlos Rincón

# Int inversion: Número de cambios que se tienen que hacer para que este ordenado el array, m= índice del corte del array
# b = el primer número del array B que se va a comparar con c, c = el primer número del array C que se va a comparar con b
# num = Variable de iteración que va tomando los valores que faltan agregar al array E, n = longitud del array a ordenar
# Arrays A: array a separar en subarreglos, B: primera parte del subarreglo, C: segunda parte de los subarreglos
# D: Guarda las lista/sublista ordenadas, E: lista nueva para ir agregando valores ordenados, datos = array ingresado
# por el usuario, array: array ordenado final

inversion = 0

def MergeSort(A):
    if len(A)==1: # Si A tiene longitud 1 regresa ese array, porque ya se dividió en 1
        return A
    m = len(A)//2 # Estableces tu corte
    B = MergeSort(A[:m]) # Sublista de lado izquierdo
    C = MergeSort(A[m:]) # Sublista de la derecho
    print(B, C) # Imprimir B y C para ver las corridas
    D = Merge(B, C) # Juntas ambas sublistas y las ordenas
    return D

def Merge(B, C):
    E = [] # Lista a la que se van a agregar los números ordenados
    global inversion
    while len(B)!=0 and len(C)!=0: # Revisar que ambos arrays tienen algún elemento
        b = B[0]
        c = C[0] # Se establecen los primeros elementos de cada sublista
        if b<=c: # Si b es el menor se agrega a E y se elimina de B
            B.pop(0)
            E.append(b)
        else: # Si c es el menor, implica que hay algún cambio, por eso es inversion +1, se agrega a E y se elimina de C
            inversion += 1
            C.pop(0)
            E.append(c)
    for num in B+C: # Los números restantes se agregan a E porque ya estan ordenados
        E.append(num)
    return E

# Explicación: Se pide la longitud del arreglo y el arreglo separado con espacios (esto se guarda como lista en datos),
# se ingresa los datos a MergeSort para ser ordenados, la lista ordenada se guarda en array y se imprime.

n = int(input("Arreglo tiene longitud: ")) # Pedir cuántos números hay en la lista
datos = list(map(int,input("Arreglo: ").split()))

array = MergeSort(datos)

print(f"Núm de inversiones: {inversion}\nArreglo ordenado: {array}")

# ÚLTIMA MODIFICACIÓN
# 9:55 el 31 de agosto de 2021, por Ivannia Gomez
# linea 21