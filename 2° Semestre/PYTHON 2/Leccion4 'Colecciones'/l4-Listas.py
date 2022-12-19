#lista = Ariel, Liliana, Natalia, Osvaldo

#Colecciones en python (arreglos)

nombres = ['Naty','Osvaldo','Liliana','Juani']
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
print(nombres)
print(nombres[0]) #muestra el primer nombre
print(nombres[1])
print(nombres[-1]) #muestra el ultimo nombre
print(nombres[-2])#muestra el penultimo nombre

#mostramos un rango de la lista.
print(nombres[0:2]) #muestra las primeras tres posisiones de la lista.

#vamos del inicio al indice de la lista
print(nombres[ :3])

#Modficar un valor dentro de la lista
nombres[3] = 'Lily'
print(nombres)

#Iterar nuestra lista 
for nombre in nombres: #nombre es singular, la lista es plural.
    print(nombre)
else: print('Se acabaron los elementos de la lista')

#Preguntamos cuantos elementos tiene la lista.
print(len(nombres))

    #*********************************************
#Tipo set. //no mantiene indice.
planetas = {'Martes','Jupiter','Venus'}
print(planetas)
print(len(planetas))#usamos len para saber el largo.

print('Martes' in planetas)#pregunta ¿elemprint('jupiter' in planetas)ento martes esta en planetas? se debe respetar todos los elementos. 
print('jupiter' in planetas) #False (no tiene mayuscula)
print('jupiter' in planetas)#true esta en la lista del jupiter

#Agregamos un elemento
planetas.add('Tierra') # add es una funcion
print(planetas)

#Eliminar elementos 
planetas.remove('Jupiter')
print(planetas)

#limpiar set
planetas.clear() 
print(planetas)

# 'Maradona': 10
diccionario ={
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada Objeto',
    'SABD':'Sistema de Administracion de Base de Datos'
}
#verificamos la cantidad de elementos del diccionario
print(diccionario)
print(len(diccionario))

#acceder a un dicionario con la llave (key)
print(diccionario['IDE'])

#otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#como recorrer los elementos/ nos muestra las llaves
for termino in diccionario:
    print(termino)

#vemos las llaves y sus valores
for termino, valor in diccionario.items():
    print(termino, valor)
    
#otra manera de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) #muestra solo las llaves

for valor in diccionario.values():
    print(valor)
    
#Comprobamos la existencia de algun elemento
print('IDE' in diccionario)#devuelve un booleano

#agregamos un elemento
diccionario['PK']= 'Primariry Key'
print(diccionario)

#Eliminamos un elemento
diccionario.pop('SABD')
print(diccionario)

#Conectamos listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1+lista2
print(lista3)

lista3.extend({7,8,9,1})
print(lista3)

print(lista3.index(5))

#Como saber cuantos valores repetidos hay en una lista
print(lista3.count(1))#cuenta cuantos valores iguales hay dentro de una lista

#para que una lista se multiplique repitiendo sus elementos
lista = [1,2,3,4] *2
print(lista)

lista3 = lista3 * 2
print(lista3)

#Metodos de ordenamiento.
#Orden de menor a mayor
lista3.sort()
print(lista3)
#Orden de mayor a menor
lista3.sort(reverse=True)
print(lista3)

#Repaso de tupla
#La tupla muestra todos los elementos
tupla = (4, 'HOLA', 6.27, [1,5,8], 4, 'HOLA')
print(tupla)
print(4 in tupla)

#Repaso de set o conjuntos / dentro de un conjuntos hay valores unicos
conjunto =set()
conjunto1 = {'Bye',}
conjunto.add(7)
conjunto.add('HOLA')
conjunto.add('ESTO ESTA EN PYTHON')
print(conjunto)
conjunto1.add('Adios')
print(conjunto1)
