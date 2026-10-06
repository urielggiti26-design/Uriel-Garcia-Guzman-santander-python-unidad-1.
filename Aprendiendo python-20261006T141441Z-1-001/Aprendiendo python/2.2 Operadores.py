# 2.2 Operadores - ejemplos del curso

# Operadores aritméticos
a = 10
b = 3

suma = a + b                  # 13
resta = a - b                 # 7
multiplicacion = a * b        # 30
division = a / b              # 3.333333333
division_entera = a // b      # 3
modulo = a % b                # 1
exponenciacion = a ** b       # 1000
print(suma, resta, multiplicacion, division, division_entera, modulo, exponenciacion)

# Operadores de comparación
igual = a == b                # False
diferente = a != b            # True
mayor_que = a > b             # True
menor_que = a < b             # False
mayor_o_igual = a >= b        # True
menor_o_igual = a <= b        # False
print(igual, diferente, mayor_que, menor_que, mayor_o_igual, menor_o_igual)

# Operadores lógicos
resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)    # True
resultado_not = not (a > 5)           # False
print(resultado_and, resultado_or, resultado_not)
