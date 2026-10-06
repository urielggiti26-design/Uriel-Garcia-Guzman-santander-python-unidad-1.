# 6.2 Excepciones personalizadas - ejemplo del curso

condicion = True  # el curso la usa sin definirla

def funcion():
    # Código que puede generar una excepción personalizada
    if condicion:
        raise Exception("Descripción del error")

try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")
