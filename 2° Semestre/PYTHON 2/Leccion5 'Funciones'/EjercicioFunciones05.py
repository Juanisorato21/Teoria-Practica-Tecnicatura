#Ejercicio 05: Convertidor de temperatura
#Realizar don funciones para convertir de grado a celcius
#a fahrenheint y visevera
#investigar las formulas

#Funcion que convierte de celsius a fahrenheint
def celsius_fahrenheint(celsius):
    return celsius*9 /5 + 32 #la presedencia: multiplicacion *. division /, suma +

#Funcion que convierte de fahrenheint a celsius
def fahrenheint_celsius(fahrenheint):
    return (fahrenheint -32) * 5 / 9 #Respetamos la presedencia utilizando parentesis


celsius = float(input('Digite el valor de celsius: '))
resultado = celsius_fahrenheint(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

fahrenheint = float(input('Digite el valor de fahrenheint: '))
resultado = fahrenheint_celsius(fahrenheint)
print(f'{fahrenheint} F a C -> {celsius}')

