# BUBBLE SORT

# Realizar el algoritmo de bubble sort
# Ivannia Gomez Moreno, Stephanie González, Michelle Muñiz
# int n = longitud de la lista, x = contador para agregar lista, num_int = cada número agregado en la lista,
#       pasada = contador de la pasada, j = contador de cambios de esa línea
# list a = lista de los números
# bool interruptor = Si ha hecho un cambio reciente es True, en cambio es False

n = int(input("Inserte cuántos números quiere ordenar: ")) # Pedir cuántos números hay en la lista
a = []
for x in range(n): # Hacer un ciclo for para ir guardandolos
    num_int = int(input(f"{x+1}. Num: "))
    a.append(num_int)

interruptor = True
pasada = 0

# Explicación: Hace una primera pasada, y va cambiando en caso de que se necesite (así aseguramos que el último número
# este en la última posición. Para la siguiente pasada, se realizan menos loops porque por cada pasada aseguramos que
# la últimas posiciones estén en su lugar, de modo que se le resta n-1-pasada.
# En caso de que se haga algún cambio el interruptor se vuelve True para que haga otra pasada, si en una pasada
# completa no se hizo ningún cambio entonces se termina el ciclo.

while pasada < n-1 and interruptor == True:
    interruptor = False
    for j in range(n-pasada-1):
        if (a[j]>a[j+1]):
            interruptor = True
            aux = a[j]
            a[j] = a[j+1]
            a[j+1] = aux
            print(a)
    pasada += 1

print("La lista ordenada es:", a)

# ÚLTIMA MODIFICACIÓN
# 9:40 el 17 de agosto de 2021, por Ivannia Gomez
# linea 25