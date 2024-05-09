def find_min_max(arr):

    if len(arr) == 0:   # Verificamos si el arreglo está vacío
        return None, None

    # Inicializamos min_value y max_value con el primer elemento del arreglo
    min_value = arr[0]
    max_value = arr[0]

    # Iteramos sobre cada elemento del arreglo
    for num in arr:
        
        if num < min_value: # Comprobamos si el elemento actual es menor que min_value, si es así, actualizamos min_value
            min_value = num
        
        elif num > max_value:# Comprobamos si el elemento actual es mayor que max_value, si es así, actualizamos max_value
            max_value = num

    
    return min_value, max_value # Devolvemos el valor mínimo y máximo encontrados en el arreglo

arr = []

# Solicitamos al usuario que ingrese el número de elementos del arreglo
n = int(input("Ingrese el número de elementos del arreglo: "))

# Iteramos sobre el rango especificado por el usuario para ingresar los elementos del arreglo
for i in range(n):
    # Solicitamos al usuario que ingrese el valor del elemento
    num = int(input("Ingrese el valor del elemento " + str(i + 1) + " : "))

    arr.append(num)   # Agregamos el elemento a la lista

# Llamammos a la función find_min_max para encontrar el valor mínimo y máximo del arreglo 
min_value, max_value = find_min_max(arr)

# Imprimimos el valor mínimo y máximo encontrados
print("Elemento menos", min_value)
print("Elemento mayor", max_value)
