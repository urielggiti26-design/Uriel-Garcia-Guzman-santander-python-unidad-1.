# 8. Importación de módulos - ejemplos del curso
import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

# from ... import
from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0

# Módulos de la biblioteca estándar
import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10

fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual
