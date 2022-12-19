# Ejercicio 01: Creamos una variable para sumar los valores recibidos de tipo
# numericos, utilizamos argumentos variables *args como parametro
#de la funcion y agregamos como resultado la suma de todos los valores pasados
#como argumentos.

def sumar_valor(*args): #recibimos una cantidad de parametros indefinidos
    resultado = 0
    #iteramos cada elemnto
    for valor in args:
        resultado += valor
    return resultado
    
    
    #llamamos a la funcion
print(sumar_valor(3,5,9,9,8,5,3,4,7))

    