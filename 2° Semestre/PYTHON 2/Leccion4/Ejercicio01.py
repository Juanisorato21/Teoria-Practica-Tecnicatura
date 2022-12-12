#Ejercicio 01: Llenar una lista.
#Llenar una lista con los numeros del 1 al 50, luegomostrar.
#La lista con el bucle for, los elementos denen mostrarse  de la siguiente forma:
# 1-2-3-4-5-6...50.

#lista = []
#i = 1
#while i <=50:
    #lista.append(i)
    #i += 1


lista =list(range(1,51))
for i in lista:
    print(i, end='-')