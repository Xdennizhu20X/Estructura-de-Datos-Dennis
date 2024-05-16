class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo elemento al final de la lista
    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    # Eliminar el elemento en el índice especificado
    def eliminar_por_indice(self, indice):
        if self.cabeza is None or indice < 0:
            return
        actual = self.cabeza
        if indice == 0:
            self.cabeza = actual.siguiente
            return
        contador = 0
        anterior = None
        while actual and contador < indice:
            anterior = actual
            actual = actual.siguiente
            contador += 1
        if actual:
            anterior.siguiente = actual.siguiente

    # Obtener los datos del elemento en un índice específico
    def obtener_por_indice(self, indice):
        if indice < 0 or self.cabeza is None:
            return None
        actual = self.cabeza
        contador = 0
        while actual and contador < indice:
            actual = actual.siguiente
            contador += 1
        if actual:
            return actual.dato
        else:
            return None

    # Imprimir el contenido de la lista
    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

def main():
    lista_enlazada = ListaEnlazada()

    # Insertar elementos
    lista_enlazada.insertar_al_final("10")
    lista_enlazada.insertar_al_final("20")
    lista_enlazada.insertar_al_final("30")
    lista_enlazada.insertar_al_final("40")
    lista_enlazada.insertar_al_final("50")

    # Imprimir la lista inicial
    print("Lista Inicial:")
    lista_enlazada.imprimir_lista()

    # Solicitar al usuario que elija un índice para eliminar
    indice_a_eliminar = int(input("\nIngrese el índice del elemento que desea eliminar: "))
    lista_enlazada.eliminar_por_indice(indice_a_eliminar)

    # Imprimir la lista después de la eliminación
    print("\nLista después de eliminar el índice '{}':".format(indice_a_eliminar))
    lista_enlazada.imprimir_lista()

    # Solicitar al usuario que elija un índice para obtener el valor
    indice = int(input("\nIngrese el índice del elemento que desea obtener: "))
    elemento = lista_enlazada.obtener_por_indice(indice)
    if elemento is not None:
        print("Elemento obtenido en el índice {}: {}".format(indice, elemento))
    else:
        print("Índice {} fuera de rango.".format(indice))

if __name__ == "__main__":
    main()
