# 5. Funciones - ejemplos del curso

# Función simple
def saludo():
    print("¡Hola, mundo!")

saludo()  # Imprime "¡Hola, mundo!"

# Función con parámetros
def saludo(nombre):
    print(f"¡Hola, {nombre}!")

saludo("Juan")   # Imprime "¡Hola, Juan!"
saludo("María")  # Imprime "¡Hola, María!"

# Función con return
def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(resultado)  # Imprime 7

# Función lambda
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25

# Alcance de variables
def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función

variable_global = 20

def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar

funcion()   # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
try:
    print(variable_local)  # Genera un error, la variable no está definida en este alcance.
except NameError as e:
    print("NameError:", e)

# Docstrings
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área del rectángulo.
    """
    return base * altura

print(area_rectangulo(3, 4))

# Número variable de argumentos
def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(suma_variable(1, 2, 3))     # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22
