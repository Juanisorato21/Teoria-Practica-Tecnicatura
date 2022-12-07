"""
Ejercicio 3: Calcular la estación del año

Pedir al usuario que ingrese un mes del año, el valor debe ser entre 1 y 12,
luego le decimos en que estación del año está:

Verano: 1,2,3 ------------- 21/12 al 21/03
Otoño: 4,5,6 -------------- 21/03 al 21/06
Invierno: 7,8,9 ----------- 21/06 al 21/09
Primavera: 10,11,12 ------- 21/09 al 21/12

"""

"""
mes = int(input("Digite el mes del año que desea saber la estación: "))

if mes <= 3 :
    print("Verano")
elif mes > 3 and mes < 7:
    print("Otoño")
elif mes >= 7 and mes < 10:
    print("Invierno")
elif mes >= 10 and mes < 13:
    print("Primavera")
elif mes > 12:
    print("No hay un mes para esa estación, de hecho ese mes no existe.")
"""


# Hecho por el Profe
# Ejercicio calcular la estación del año

mes = int(input("Digite un mes del año (1 - 12): "))
estacion = None

if mes == 1 or mes == 2 or mes == 3:
    estacion = "Verano"
elif mes == 4 or mes == 5 or mes == 6:
    estacion = "Otoño"
elif mes == 7 or mes == 8 or mes == 9:
    estacion = "Invierno"
elif mes == 10 or mes == 11 or mes == 12:
    estacion = "Primavera"
else:
    estacion = "Error, no hay número para ese mes"
print(f"Para el mes {mes} la estación es: {estacion}")
