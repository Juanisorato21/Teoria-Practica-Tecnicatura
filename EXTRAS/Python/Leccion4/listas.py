nombres= ['Julian','Maria','Tomas','Ariel','Facundo']
print(nombres)
#para imprimir un solo nombre
print(nombres[1])
#para leer el ultimo nombre
print(nombres[-1])

#Recuperar un rango de la lista 
#Vemos las 2 primera posiciones
print(nombres[0:2])
#Ir del inicio hasta el indice 
print(nombres[ :3])
#desde el indice indicado hasta el final
print(nombres[1: ])
#modificamos un valor de la lista
nombres[3]='Thomas'
print(nombres)
#Insertar una lista
for nombre in nombres:
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

#Preguntamos cuantos elementos tiene la ista
print(len(nombres))

#Agregamos un elemento a la lista
nombres.append('Marcelo')
print(nombres)
#Insertamos un elemento en un indice especifico
nombres.insert(1, 'Lucio')
print(nombres)


#Tuplas
#Definimos una Tupla
cocina=('cuchara','cuchillo','tenedor')
print(cocina)

#Tipo set
planetas = {'Marte','Jupiter','Venus'}
print (planetas)
print(len(planetas)) #Usamos len para contar cuantos elementos hay
print('Marte'in planetas)
print('tierra'in planetas)

#Agregamos un elemento
planetas.add('Tierra')
print(planetas)

#Eliminamos un elemento
planetas.remove('Marte')
print(planetas)

#Limpiar set
planetas.clear()
print (planetas)

#eliminar set
del planetas
#print(planetas)

diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos',

}
print(diccionario)