#pedir al usuario que ingrese un mes del año, el valor debe ser entre 1 y 12, luego decimos en que estacion del año esta
mes = int(input("Ingrese un mes del año en forma de N° (1 al 12): "))

if mes <= 3:
    print("Usted esta en Verano")
elif 3< mes <7:
    print("Usted esta en Otoño")
elif 7< mes <10:
    print("Usted esta en Invierno")
elif 9 < mes <13 : 
    print("Usted esta en Primavera")
