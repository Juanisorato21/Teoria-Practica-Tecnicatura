#error o excepcion es cuando nuestro programa termina cuando se encontro con un error.

#////////////////////////////////////////////////////////////////////////////////////////////////////////

#error: no puede dividir 10/0
"""
try:
    10/0
except Exception as e:
    print(f'Ocurrio un error: {e}')
"""
#////////////////////////////////////////////////////////////////////////////////////////////////////////

# error: he puesto un str y tendria que ser int
"""
resultado = None
a = '10'
b = 0
try:
    resultado = a/b #modificamos 
except Exception as e:
    print(f'Ocurrio un error: {e}')
    print(f'El resultado es: {resultado}')
    print('seguimos...')
"""
#////////////////////////////////////////////////////////////////////////////////////////////////////////

#procesamos la excepciones mas especificas
"""
resultado = None
a=10
b=0
try:
    resultado = a/b #modificamos
except TypeError as e:
    print(f'TypeError - ocurrio un error {tupe(e)}')
    
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - ocurrio un error {e}')
    
except Exception as e:
    print(f'Exception - ocurrio un error {e}')
    
print(f'El resultado es: {resultado}')
print('seguimos...')
    
"""
#////////////////////////////////////////////////////////////////////////////////////////////////////////

# las variables dentro del try son exclusivas del mismo
#Pedimos al usuario que ingrese los numeros 
"""
resultado = None

try:
    a = int(input('Ingrese el primer numero: '))
    b= int(input('Ingrese el segundo numero: '))
    resultado = a/b #modificamos
except TypeError as e:
    print(f'TypeError - ocurrio un error {tupe(e)}')
    
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - ocurrio un error {e}')
    
except Exception as e:
    print(f'Exception - ocurrio un error {e}')
    
print(f'El resultado es: {resultado}')
print('seguimos...')
"""
#////////////////////////////////////////////////////////////////////////////////////////////////////////
#----------------------------------------------------------------------------------
#podems agregar dos bloques mas:  
# A = (else) se ejecuta si no lanzo ninguna excepcion
#solo aparece si no sale ninguna excepcion
#----------------------------------------------------------------------------------

resultado = None
"""
try:
    a = int(input('Ingrese el primer numero: '))
    b= int(input('Ingrese el segundo numero: '))
    resultado = a/b #modificamos
except TypeError as e:
    print(f'TypeError - ocurrio un error {tupe(e)}')
    
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - ocurrio un error {e}')
    
except Exception as e:
    print(f'Exception - ocurrio un error {e}')
    
else: #solo aparece si no sale ninguna excepcion
    print("No se arrojo ninguna excepcion")
    
print(f'El resultado es: {resultado}')
print('seguimos...')
"""
#----------------------------------------------------------------------------------
# B = (finally) siempre se va a ejecutar
#siempre se va a ejecutar
#----------------------------------------------------------------------------------
from NumerosIgualesException import NumerosIgualesException
resultado = None
try:
    a = int(input('Ingrese el primer numero: '))
    b= int(input('Ingrese el segundo numero: '))
    if a == b: 
        raise NumerosIgualesException('Son numeros iguales') #permite arrojar una exception 
        
    resultado = a/b #modificamos
except TypeError as e:
    print(f'TypeError - ocurrio un error {tupe(e)}')
    
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - ocurrio un error {e}')
    
except Exception as e:
    print(f'Exception - ocurrio un error {e}')
    
finally: #Siempre se va a ejecutar
    print('Ejecucion de este bloque finally')
    
print(f'El resultado es: {resultado}')
print('seguimos...')

#////////////////////////////////////////////////////////////////////////////////////////////////////////

