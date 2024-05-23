# Calculadora Postfix: ¡Operaciones al Estilo Polaco Inverso!
Aquí tenemos una pequeña herramienta que hace cálculos de manera un poco inusual, usando algo llamado notación postfix. ¿Qué es eso? ¡No te preocupes! Te lo explicaremos en un momento.

# ¿Qué es una Pila?
Piensa en una pila como una torre de platos. Puedes agregar uno encima del otro, y cuando necesitas sacar uno, siempre tomas el que está en la cima.

# ¿Cómo funciona esto?
Lo que hacemos aquí es tomar una serie de números y operadores y trabajar con ellos de manera inversa a lo que estás acostumbrado. Por ejemplo, si tienes la operación "3 4 + 2 *", primero sumas 3 y 4, luego multiplicas el resultado por 2.

## Descripción del TDA
La pila es una estructura de datos LIFO (Last In, First Out). Las operaciones básicas incluyen:
- `push`: Insertar un elemento en la pila.
- `pop`: Remover y retornar el elemento superior de la pila.
- `is_empty`: Verificar si la pila está vacía.
- `peek`: Obtener el elemento superior sin removerlo.

# ¿Cómo usar esto?
Simplemente escribe tu expresión postfix cuando se te pida. Por ejemplo, podrías escribir "3 4 + 2 *" como en el ejemplo anterior. Luego, la calculadora hará su magia y te mostrará el resultado.

# ¿Listo para probar?

```bash
Copiar código
$ python3 CalculadoraPostfix.py
Ingresa una expresión postfix: 3 4 + 2 *
Resultado: 14
¡Así de fácil! Ahora es tu turno. Experimenta con algunas operaciones y sorpréndete con lo que esta calculadora puede hacer.