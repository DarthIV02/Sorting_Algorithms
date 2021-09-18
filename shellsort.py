# SHELL SORT + BÚSQUEDA BINARIA

# Realizar el algoritmo de ordenamiento por shell sort, y realizar una búsqueda binaria
# Equipo 7: Ivannia Gomez, Axel Cruz, Iram Abbud

def Shell(A):
    jump = len(A)+1
    while jump>1:
        jump = jump//2
        flag = True
        while flag:
            flag = False
            i = 0
            while i+jump<=len(A)-1:
                #print(f"Corrida: {A}, revisando {A[i]}, {A[i + jump]}")
                if A[i]>A[i+jump]:
                    A[i], A[i+jump] = A[i+jump], A[i]
                    flag = True
                i = i+1
    return A

def BinarySearch(A, target):
    min = 0
    max = len(A)-1
    while True:
        guess = (min+max)//2
        if A[guess]==target:
            break
        elif A[guess]<target:
            min = guess+1
        else:
            max = guess-1

        if min>max:
            return "Not Found"
    return guess

n = int(input("Arreglo tiene longitud: ")) # Pedir cuántos números hay en la lista
while True:
    datos = list(map(int,input("Arreglo: ").split()))
    if len(datos)!=n:
        print("Número de datos incorrectos")
    else:
        break

print(f"Lista ordenada: {Shell(datos)}")

target = int(input("Inserte número a buscar: "))

busqueda = BinarySearch(datos, target)

if busqueda == "Not Found":
    print(busqueda)
else:
    print(f"Números anteriores a ese número: {busqueda}")
