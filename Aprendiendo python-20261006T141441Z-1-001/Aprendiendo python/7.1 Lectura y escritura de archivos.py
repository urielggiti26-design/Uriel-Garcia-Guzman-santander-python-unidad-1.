# 7.1 Lectura y escritura de archivos - ejemplos del curso

# Escritura (modo "w" crea/sobrescribe el archivo)
archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

# Lectura (modo "r")
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

# Con with el archivo se cierra solo
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
