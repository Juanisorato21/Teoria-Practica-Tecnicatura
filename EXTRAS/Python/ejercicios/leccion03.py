


























#Imprimir numeros del 0 al 15 con ciclo while
'''
Maximo = 15
contadir = 0
while contador <= maximo:
    print(contador)
    contador +=1
'''
'''
minimo = 1
contador = 15
while contador >= minimo:
    print(contador)
contador -=1
'''
#Ciclo For
'''
cadena = "Hello"
for letra in cadena:
    print(letra)
else: print("Fin del ciclo for")
'''
'''
for letra in "Alemania":
    if letra == "a":
        print(f'letra encontrada: {letra}')
    else: print('Fin del ciclo for')
    '''
#Palabra reservada continue
for i in range (6):
    if i % 2 == 0: 
        print(f'Valor: {i}')

for i in range (6):
    if i % 2 !=0: 
        continue
        print(f'Valor: {i}')
        