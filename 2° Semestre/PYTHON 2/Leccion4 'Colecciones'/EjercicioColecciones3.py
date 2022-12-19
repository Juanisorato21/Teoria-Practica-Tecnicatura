#Ejercicio 3: Agregar personajes a una lista.

#Escriba un programa donde cree una lista con los siguientes personajes.
#Nombre:  Viserys I Targaryen
#Clase: Rey
#Alias: EL JOVEN REY

#Nombre: Corlys Velaryon
#Clase: Lord comandante de la guardia real
#Alias: LA SERPIENTE MARINA

#Nombre: Otto Hightower
#Clase: Mano del rey
#Alias: LA MANO

personajes = [] #Creamos una lista vacia.
P1 = {'Nombre': 'Viserys I Targaryen','Clase': 'Rey','Alias':'EL JOVEN REY'}
personajes.append(P1)#agregamos a la lista un personaje
P2 = {'Nombre': 'Corlys Velaryon','Clase': 'Lord comandante de la guardia real','Alias':'La serpiente marina'}
personajes.append(P2)
P3 = {'Nombre': 'Otto Hightower', 'Clase': 'Mano del rey','Alias':'La mano'}
personajes.append(P3)

#Agregar tres personajes mas.
P4 = {'Nombre': 'Rhaenyra Targaryen','Clase':'Primer heredera al trono de hierro','Alias':'La delicia del reino'}
personajes.append(P4)
P5= {'Nombre': 'Alicent Hightower','Clase':'Acompañante del rey','Alias': 'No tiene'}
personajes.append(P5)
P6= {'Nombre': 'Aegon II Targaryen','Clase':'Hijo mayor del rey y futuro rey','Alias': 'Aegon el Usurpador'}
personajes.append(P6)
print(personajes)