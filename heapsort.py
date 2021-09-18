# HEAP SORT

# Copiar el algoritmo de heap sort y documentarlo
# Ivannia Gomez #27814

def heapsort(a):
    "Ordenar por montículo"
    heapify(a, len(a)) # Se acomoda la primera vez en montículo, para esto se checan todos los nodos que son padres
    end = len(a)-1 # Se establece el final del arreglo a acomodar como el final del array
    # end es un marcador que marca el índice del fin de la sublista de números no ordenados
    while end > 0: # Mientras que haya algún número que falte de acomodar al final
        a[end], a[0] = a[0], a[end] # Se intercambia el primer término (que tiene el mayor número de los números
        # no arreglados) con el último no acomodado
        end -= 1 # Ya que se agrego otro número arreglado al final, el fin de la lista de números no acomodados se reduce
        sift_down(a, 0, end) # Se acomoda el primer término en el lugar correcto para que el mayor número
                             # de los no ordenados esté nuevamente al principio

def heapify(a, count):
    "Función que ordena en montículo, asegurandose que los padres siempre sean mayores que los hijos al principio"
    start = int((count-2)/2) # Start es la variable que va a empezar a recorrer el array del medio para arriba,
    # en otras palabras del penúltimo nivel del árbol binario y todos los nodos de arriba

    while start >= 0: # Mientras que haya nodos que no se hayan revisado del start al índice 0
        sift_down(a, start, count-1) # Se verifica que todos los hijos de start sean menores o se hacen los cambios
                                     # necesarios
        start -= 1 # Se reduce en 1 para que se pueda checar otro padre

def sift_down(a, start, end):
    """Revisa que los hijos de un nodo 'root' sean menores a este, en caso de que no lo sea, hace los cambios
    pertinentes y se aseguran que los nodos abajo de donde se hizo el cambio también sean menores"""
    root = start # Se establece 'root' como start, donde se empieza a revisar que este en montículo

    while (root*2+1) <= end: # Mientras root tenga por lo menos un hijo
        # (ya que si su "hijo" es mayor del end, no es su hijo, si no fue un root anterior que ya se ordenó)
        child = root * 2 + 1 # Establecer el índice del hijo de la izquierda del root
        swap = root # Se guarda el nodo principal que se esta revisando en una variable temporal

        if a[swap] < a[child]: # Si el número en el índice del 'root' a checar es menor a su hijo,
            # entonces se cambia el índice al del hijo
            swap = child

        if (child + 1) <= end and a[swap] < a[child+1]: # En caso de que exista el hijo de la derecha
            # y no sea uno de los números ya acomodados (denotado por el menor al end)
            # y que este sea mayor que el valor del swap (ya sea root o el hijo anterior) se hace un cambio a índice del swap
            swap = child+1

        if swap != root: # Para que swap y root sean diferentes, implica que hubo un cambio
            a[root], a[swap] = a[swap], a[root] # Se hace el cambio para que el mayor sea el padre
            root = swap # Ahora se toma como root el índice del hijo donde se hizo el cambio para reiniciar el ciclo y
            # volver a revisar que los hijos de este nuevo 'root' sean menores
        else:
            return # En caso donde no se hayan hechos cambios se regresa a la función principal

    print(a) # Si en algunos de los casos se hicieron varios cambios de padres con hijos,
    # y se llego a revisar un nodo que no es padre (esta en el último nivel) si imprime el proceso

#a =[13,6,45,10,3,22,5]
a =[10, 1, 7, 2, 5]
print(a)
heapsort(a)

# ÚLTIMA MODIFICACIÓN
# 10:06 el 2 de septiembre de 2021, por Ivannia Gomez
# linea 58