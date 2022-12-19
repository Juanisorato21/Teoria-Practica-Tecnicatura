#Ejercicio 7: Juego adivina el numero.
#Realiza un juego para adivinar un numero. para ello se debe.
#generar un numero aleatorio entre 1 - 100, y luego ir pidiendo
#numeros indicando "es mayor" o "es menor" segun sea mayor o menor
#con respecto a N. El proceso termina cuando el usuario acierta.
#y alli se debe mostrar el numero de intento.

import random
print('\t Juego Adivina el numero')
aleatorio = random.randint(0,100) #Toma de 1 a 100 literal, generamos un numero aleatorio
contador = 0
while True: 
    numero = int(input("Digite un umero: "))
    contador += 1
    if numero > aleatorio:
        print('\t No es el numero, digite un numero menor')
    elif numero < aleatorio:
        print('\tNo es el numero, digite un numero Mayor')
    else:
        print(f'FELICITACION, ADIVINASTE, El numero era: {aleatorio}')
        break# Rompe el ciclo 

print(f'\n Numero de intentos: {contador}')
