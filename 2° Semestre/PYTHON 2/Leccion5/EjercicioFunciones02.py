#Ejercicio 2: Funcion con * args para multiplicar
#Crear una funcion para multiplicar los valores recibidos
#de tipo numerico, utilizando argumentos variables *args
#como parametro de la funcion y regresamos como resultado
#la multiplicacion de todos los valores pasados como argumentos

def multiplicar_valores(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado

#llamamos a la funcion
print(multiplicar_valores(8*9)) #pasamos los argumentos
    
