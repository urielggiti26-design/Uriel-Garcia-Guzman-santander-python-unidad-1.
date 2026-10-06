# 6. Manejo de errores y excepciones - tipos de errores del curso
# Cada error se provoca dentro de try/except para poder ver su tipo.

# SyntaxError: falta los dos puntos (def mi_funcion()  <- sin ":")
try:
    compile("def mi_funcion()\n    print('Hola')", "<ejemplo>", "exec")
except SyntaxError as e:
    print("SyntaxError:", e)

# NameError: variable no definida
try:
    print(variable_no_definida)
except NameError as e:
    print("NameError:", e)

# TypeError: operación con tipos incompatibles
try:
    resultado = 5 + "10"
except TypeError as e:
    print("TypeError:", e)

# IndexError: índice fuera de rango
try:
    lista = [1, 2, 3]
    print(lista[3])  # El índice 3 está fuera del rango
except IndexError as e:
    print("IndexError:", e)
