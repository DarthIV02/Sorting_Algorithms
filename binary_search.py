# Funcion para Binary Search
def BinarySearch(arr, target):
    # Variables para poder buscar el numero pedido que determinar los límites de arreglo a buscar
    min = 0
    max = len(arr) - 1

    # Funcion while para buscar el numero utilizando min y max
    # Se realiza un ciclo sin parada hasta que los min>=max, por lo tanto no se encontro o se llega al número buscado
    while True:

        # Creamos una variable con la posicion media del arreglo que es nuestro intento actual
        guess = (min + max) // 2

        # Si esta posicion resulta tener el numero buscado termina el programa
        if arr[guess] == target:
            break
        # Si el numero en la posicion de nuestro intento es menor que el numero
        # buscado se suma 1 al rango minimo y se intenta otra vez
        elif arr[guess] < target:
            min = guess + 1
        # Si el numero de nuestro intento es mayor, se resta 1 al rango
        # maximo y se intenta otra vez
        else:
            max = guess - 1
        # Si el numero no se encuentra y se regresa un "No"
        # como respuesta a la funcion
        if min > max:
            return "No"
    return guess