#Ejercicio 2: Operaciones de conjuntos con listas
#Escriba un programa que tenga 2 lineas y que a continuacion.
#Cree las siguientes listas(en las que no deben haber repeticiones).
#1 listas de numeros que aparecen en las listas.
#2 Listas de numeros que aparecen en la primera lista. pero no en la segunda.
#3 Lista de numeros que aparecen en la segunda lista, pero no en la primera.
#4 Lista de numeros que aparecen en ambas listas 

lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

#Eliminamos los elementos repetidos de ambas listas con conjuntos

conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2) #Unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2) #solo muestra el conjunto1
solo2 = list(conjunto2 - conjunto1) #solo muestra el conjunto2
intersection = list(conjunto1 & conjunto2) #muestra ambas Listas

print(f"listas de numeros que aparecen en las listas: {union}")
print(f"Listas de numeros que aparecen en la primera lista. pero no en la segunda: {solo1}")
print(f"Lista de numeros que aparecen en la segunda lista, pero no en la primera: {solo2}")
print(f"Lista de numeros que aparecen en ambas listas: {intersection}")