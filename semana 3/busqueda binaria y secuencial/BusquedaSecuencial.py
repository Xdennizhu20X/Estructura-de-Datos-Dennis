def bubble_sort(arr):   #Definimos el metodo de burbuja para ordenar el arreglo
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr  #

def sequential_search(arr, key): # Definimos la función de búsqueda secuencial.
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

elements = []

print("Ingrese los 20 elementos del arreglo") #Pedimos al usuario que ingrese los elementos del arreglo
for i in range(20):
    element = int(input("Element # " + str(i+1) + ": "))
    elements.append(element)


elements = bubble_sort(elements)  # Asigna el resultado de bubble_sort de nuevo a elements

print("Arreglo Ordenado")
for i in range(len(elements)):
    print("Posición #", i + 1, "=", elements)

key = int(input("Ingrese la clave: "))
index = sequential_search(elements, key)
if index == -1:
    print(key, "Clave no encontrada")
else:
    print(key, "Clave encontrada en la posición #", index + 1)
