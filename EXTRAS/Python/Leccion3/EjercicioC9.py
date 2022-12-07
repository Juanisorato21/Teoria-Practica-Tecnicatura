#Diseñar un programa que ingresado un año, nos devuelva
#por consola si es un año bisiesto o no, repetir la accion de/hasta que el usuario lo desidades

año = int(input('Introduce un año: '))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print('El año es bisiesto')
        else:
            print('El año no es bisiesto')
    else:
        print('El año es bisiesto.')
else:
    print('El año no es bisiesto.')




