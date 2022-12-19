#Ejercicio 03: Funcion Recursiva
#Imprimir numeros de 5 a 1 de manera desendente usando la funcion recursiva
#puede ser cualquier valor positivo, por ejemplo si pasamos el 
#valor de 5, debe imprimir:
#5
#4
#3
#2
#1
#En caso de ser el numero 3 debe imprimir:
#3
#2
#1
#Si ingresan un numero negativo no imprime nada

def imprimir_numeros_recursivos(numero):
    if numero >= 1: #caso base
        print(numero)
    imprimir_numeros_recursivos(numero-1) #caso recursivo
    elif numero <=0:
        print('El valor es incorrecto....')

imprimir_numeros_recursivos(5)
    