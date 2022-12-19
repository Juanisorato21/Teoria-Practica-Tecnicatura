#Ejercicio 10: no repetir caracteres.
#Hacer un programa que pida cadena de caracteres por teclado, luego   
#meter los caracteres en una lista sin repetir caracteres.

cadena = input('Digite una cadena: ')
lista = []
for i in cadena:
    if i not in lista: #Si el caracter aun no esta en la lista
        lista.append(i)#Agregamos a la lista.
print(f'\n Lista de caracter sin repetir ninguno: \n {lista}')