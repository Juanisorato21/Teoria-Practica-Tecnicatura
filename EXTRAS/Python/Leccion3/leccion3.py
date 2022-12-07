# Ciclo while (Mientras o durante)

"""
condicion = False
while condicion:
    print("Ejecutando el ciclo While")
else:
    print("Fin del ciclo While")

"""

"""
contador = 0
while contador < 78:
    print("Ejecutamos nuestro ciclo While",contador)
    contador += 1
else:
    print("Fin del ciclo While")

"""

# Imprimir numeros del 0 al 5 con el ciclo While
"""
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += +1
"""


# Imprimir numeros del 5 al 1 de manera descendente con el ciclo While
"""
mimimo = 1
contador = 5
while contador >= mimimo:
    print(contador)
    contador -= 1
"""

# Ciclo for
"""
cadena = "Hello"
for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo For")
"""

# Palabra reservada break
"""
for letra in "Alemania":
    if letra == "a":
        print(f"Letra encontrada: {letra}")
        break # Rompe cualquier tipo de estructura al encontrar el primer elemento que buscamos, y deja de buscar una vez que lo encontró
else:
    print("Fin del ciclo For")
"""

# Palabra reservada continue

for i in range(6):
    if i % 2 == 0: # Me va a mostrar los numeros pares, que divididos por 2 nos da igual 0
        print(f"Valor: {i}")

for i in range(6):
    if i % 2 !=0:
        continue
    print(f"Valor: {i}")

