# 6.1 Manejo de excepciones - ejemplos del curso

# try / except
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")

# Varios except
try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")

# try / except / finally
try:
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    # El curso usa archivo.close(); aquí se protege por si open() falló
    if "archivo" in locals():
        archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción
