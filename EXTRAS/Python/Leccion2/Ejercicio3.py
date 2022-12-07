# Ejercicio 3:
# Intercambiar el valor de dos variables.
# Por ejemplo:
# a = 10       a = 5
# b = 5         b = 10

a = input("ingrese el valor de A: ")
b = input("ingrese el valor de B: ")
a,b = b,a

print(f"el nuevo valor de A es: {a}")
print(f"el nuevo valor de B es: {b}")