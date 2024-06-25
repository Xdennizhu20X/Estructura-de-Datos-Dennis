class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.cursor = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        if not self.cursor:
            self.cursor = nuevo_nodo

    def eliminar(self):
        if not self.cursor:
            return
        if self.cursor == self.cabeza and self.cursor == self.cola:
            self.cabeza = self.cola = self.cursor = None
        elif self.cursor == self.cabeza:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
            self.cursor = self.cabeza
        elif self.cursor == self.cola:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            self.cursor = self.cola
        else:
            self.cursor.anterior.siguiente = self.cursor.siguiente
            self.cursor.siguiente.anterior = self.cursor.anterior
            self.cursor = self.cursor.siguiente

    def mover_cursor_izquierda(self):
        if self.cursor and self.cursor.anterior:
            self.cursor = self.cursor.anterior

    def mover_cursor_derecha(self):
        if self.cursor and self.cursor.siguiente:
            self.cursor = self.cursor.siguiente

    def mostrar(self):
        nodo = self.cabeza
        texto = ''
        while nodo:
            if nodo == self.cursor:
                texto += f'[{nodo.valor}]'
            else:
                texto += nodo.valor
            nodo = nodo.siguiente
        return texto

class EditorTexto:
    def __init__(self):
        self.texto = ListaDoblementeEnlazada()

    def insertar(self, caracter):
        self.texto.insertar(caracter)

    def eliminar(self):
        self.texto.eliminar()

    def mover_cursor_izquierda(self):
        self.texto.mover_cursor_izquierda()

    def mover_cursor_derecha(self):
        self.texto.mover_cursor_derecha()

    def mostrar_texto(self):
        return self.texto.mostrar()

def menu_editor():
    editor = EditorTexto()
    while True:
        print("\n********************Editor de Texto********************")
        print("Texto actual: ", editor.mostrar_texto())
        print("Opciones:")
        print("1. Insertar carácter")
        print("2. Eliminar carácter")
        print("3. Mover cursor a la izquierda")
        print("4. Mover cursor a la derecha")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            caracter = input("Ingrese el carácter a insertar: ")
            editor.insertar(caracter)
        elif opcion == "2":
            editor.eliminar()
        elif opcion == "3":
            editor.mover_cursor_izquierda()
        elif opcion == "4":
            editor.mover_cursor_derecha()
        elif opcion == "5":
            print("Saliendo del editor.")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el menú interactivo
menu_editor()
