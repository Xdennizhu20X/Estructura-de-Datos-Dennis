def selection_sort(arr): # Definición de la función selection_sort 
    # Obtenemos la longitud del arreglo
    n = len(arr)

    
    for i in range(n): # Iteramos sobre el arreglo
        
        min_index = i   # En cada iteración, asumimos que el elemento actual es el mínimo
        
        for j in range(i + 1, n): # Iteramos sobre los elementos restantes del arreglo para encontrar el mínimo
            # Si encontramos un elemento menor que el mínimo actual, actualizamos min_index
            if arr[j] < arr[min_index]:
                min_index = j

        # Después de encontrar el mínimo, intercambiamos el elemento actual con el mínimo encontrado
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Se crea un arreglo vacío para almacenar los elementos
arr = []

# Solicitamos al usuario que ingrese el número de elementos del arreglo
n = int(input("Ingrese el número de elementos del arreglo: "))

for i in range(n): # Iteramos sobre el rango especificado por el usuario para ingresar los elementos del arreglo
    # Solicitamos al usuario que ingrese el valor del elemento
    num = int(input("Ingrese el valor del elemento " + str(i + 1) + " : "))
    
    arr.append(num)  # Agregamos el elemento a la lista

# Llamamos a la función selection_sort para ordenar el arreglo ingresado 
selection_sort(arr)

# Imprimimos el arreglo ordenado
print("Arreglo ordenado:")
print(arr)
