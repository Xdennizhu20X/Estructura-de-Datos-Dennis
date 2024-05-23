class Stack:
    def __init__(self):
        # Inicializa una pila vacía.
        self.items = []

    def push(self, item):
        # Agrega un elemento al final de la pila.
        self.items.append(item)

    def pop(self):
        # Elimina y devuelve el elemento en la cima de la pila.
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def is_empty(self):
        # Verifica si la pila está vacía.
        return len(self.items) == 0

    def peek(self):
        # Devuelve el elemento en la cima de la pila sin removerlo.
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

def evaluate_postfix(expression):
    # Evalúa una expresión matemática en notación postfix utilizando una pila.
    stack = Stack()
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            # Si el token es un número, lo convierte a entero y lo agrega a la pila.
            stack.push(int(token))
        else:
            try:
                # Si el token es un operador, saca los dos últimos elementos de la pila.
                b = stack.pop()
                a = stack.pop()
            except IndexError:
                raise ValueError("La expresión postfix es inválida.")
            
            # Realiza la operación correspondiente y agrega el resultado a la pila.
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            else:
                raise ValueError(f"Operador desconocido: {token}")
            
            stack.push(result)

    # Al final, si la pila está vacía, devuelve el resultado.
    if stack.is_empty():
        raise ValueError("La expresión postfix es inválida.")
    
    result = stack.pop()

    # Si hay más de un elemento en la pila, la expresión es inválida.
    if not stack.is_empty():
        raise ValueError("La expresión postfix es inválida.")

    return result

if __name__ == "__main__":
    # Solicita al usuario que ingrese una expresión postfix.
    expr = input("Ingrese una expresión postfix: ")
    try:
        # Evalúa la expresión y muestra el resultado.
        result = evaluate_postfix(expr)
        print(f"Resultado: {result}")
    except ValueError as e:
        # Si hay un error, muestra un mensaje de error.
        print(f"Error: {e}")
