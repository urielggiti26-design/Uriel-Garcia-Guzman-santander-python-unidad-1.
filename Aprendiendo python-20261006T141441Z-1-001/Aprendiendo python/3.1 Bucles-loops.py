# 3.1 Bucles/loops - ejemplos del curso

# for
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)

# while
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# break: sale del bucle
contador = 0

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break

# continue: salta a la siguiente iteración (imprime solo impares)
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# pass: instrucción que no hace nada
for i in range(5):
    pass
