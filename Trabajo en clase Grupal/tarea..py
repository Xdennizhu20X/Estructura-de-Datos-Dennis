import random
import timeit

def generar_lista(tamano):
    return [random.randint(1, 100) for _ in range(tamano)]

def enc_maximo(lista):
    return max(lista)

def sum_elementos(lista):
    return sum(lista)

if __name__ == "__main__":
    tamano_lista = 1000
    lista = generar_lista(tamano_lista)
    maximo = enc_maximo(lista)
    suma = sum_elementos(lista)

    print(f"Lista: {lista}")
    print(f"Máximo: {maximo}")
    print(f"Suma: {suma}")
    

setup_code = """
import random

def generar_lista(tamano):
    return [random.randint(1, 100) for _ in range(tamano)]

def encontrar_maximo(lista):
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo

def sumar_elementos(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

tamano_lista = 1000
lista = generar_lista(tamano_lista)
"""

original_sum = timeit.timeit(stmt="sumar_elementos(lista)", setup=setup_code, number=1000)
optimized_sum = timeit.timeit(stmt="sum(lista)", setup=setup_code, number=1000)
original_max = timeit.timeit(stmt="encontrar_maximo(lista)", setup=setup_code, number=1000)
optimized_max = timeit.timeit(stmt="max(lista)", setup=setup_code, number=1000)

print("Tiempo de ejecución de la suma en el codigo original:", original_sum)
print("Tiempo de ejecución de la suma en el codigo optimizado:", optimized_sum)
print("Tiempo de ejecución de encontrar el número maximo codigo original:", original_max)
print("Tiempo de ejecución de encontrar el número maximo codigo optimizado:", optimized_max)

