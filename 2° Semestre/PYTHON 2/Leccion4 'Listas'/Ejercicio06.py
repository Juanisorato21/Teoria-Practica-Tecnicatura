#Ejercicio 06: Tabla de multiplicar 
#Hacer un programa que pida un numero por tclado y guarde 
#en una lista su tabla de multiplicar hasta el 10. por ejemplo:
#Si digita el 5 de la lista tendra: 5,10,15,20,25,30,35,40,45,50

numero = int(input('Digite un  numero: '))
lista = []#creamos una lista vacia.
for i in range(1,11):
    lista.append(i+numero)
print(f'\Tabla de multiplicar del {numero}: \n {lista}')
