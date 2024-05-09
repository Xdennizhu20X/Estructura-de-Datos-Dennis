
def bubble_sort(arr): # Definición de la función bubble_sort 

    n = len(arr) # Obtenemos la longitud del arreglo
    
    for i in range(n):# Iteramos sobre cada elemento del arreglo
        
        for j in range(0, n - i - 1): # El rango se reduce en cada iteración para evitar comparaciones innecesarias
            if arr[j] > arr[j + 1]:# Ordenamos el arreglo verificando cual elemento es mayor
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not any(arr[i] > arr[i + 1] for i in range(n - 1)): # Verificar si el arreglo está ordenado, si lo está, salir del bucle
            break
        
    return arr  # Devolvemos el arreglo ordenado

# Se crea un arreglo vacío para almacenar los elementos
arr = []

n = int(input("Ingrese el número de elementos del arreglo: ")) # Solicitar al usuario que ingrese el número de elementos del arreglo

for i in range(n): # Iteramos sobre el rango especificado por el usuario 

    x = int(input("Ingrese el valor del elemento " + str(i + 1) + ": ")) # Solicitamos al usuario que ingrese el valor del elemento

    arr.append(x) # Agregamos el elemento a la lista


arr = bubble_sort(arr)# Llamamos a la función bubble_sort para ordenar el arreglo ingresado 

print("Arreglo ordenado:", arr)# Imprimir el arreglo ordenado
