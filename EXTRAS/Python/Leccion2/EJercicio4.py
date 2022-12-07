"""
Ejercicio 4: Area y longitud de un circulo
Hacer un programa para ingresar el radio de un
circulo y se repotte su area y la longitud de la circunferencia

Área = Pi*r2
Longitud= 2*Pi*r

En este ejercicio vamos a necesitar importar
el modulo math porque tiene el valor de Pi

Se escribe: import math
"""
import math

radio = float(input("Digite valor del Radio: "))
pi = math.pi
area = pi * radio ** 2
Long = 2 * pi * radio

print(f"El Área del circulo es:  {area}")
print(f"La longitud del circulo es: {Long}")