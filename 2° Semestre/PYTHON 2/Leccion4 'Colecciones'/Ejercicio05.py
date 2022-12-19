#Ejercicio 5: Factorial de un numero positivo
#Hacer un programa para calcular el factorial de un numero positivo

numero =int(input('Digite un numero positivo: '))
while numero <0: #Mientras numero sea negativo
    print('ERROR -> EL NUMERO DEBE SER POSITIVO')
    numero = int(input('Digite un numero positivo: '))

factorial = 0 #variable para calcular el factorial.
for i in range(1, numero+1):
    factorial += i
    print(f'\n El factorial del numero {numero} positivo ingresado es: {factorial}')
    