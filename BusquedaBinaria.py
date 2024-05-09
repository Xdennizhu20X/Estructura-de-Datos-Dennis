def bubble_sort(arr): #Definimos el metodo de burbuja para ordenar el arreglo
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, key): # Definimos la función de búsqueda binaria.
    inicio = 0
    fin = len(arr) - 1
    medio = 0

    while inicio <= fin:
        medio = (fin + inicio) // 2
        if arr[medio] < key:
            inicio = medio + 1
        elif arr[medio] > key:
            fin = medio - 1
        else:
            return medio
    return -1

elements = []

print("Ingrese los 20 elementos del arreglo") #Pedimos al usuario que ingrese los elementos del arreglo
for i in range(20):
    element = int(input("Element # " + str(i+1) + ": "))
    elements.append(element)

elements = bubble_sort(elements)  # Ordenamos los elementos utilizando el algoritmo de ordenamiento de burbuja

print("Arreglo Ordenado") #Imprimimos el arreglo ordenado
for i in range(len(elements)):
    print("Posición #", i + 1, "=", elements[i])

key = int(input("Ingrese la clave: "))

index = binary_search(elements, key)  # Realizamos la búsqueda binaria sobre el arreglo ordenada

#imprimimos si la clave a sido encontrada o no
if index == -1:
    print(key, "Clave no encontrada")
else:
    print(key, "Clave encontrada en la posición #", index + 1)
