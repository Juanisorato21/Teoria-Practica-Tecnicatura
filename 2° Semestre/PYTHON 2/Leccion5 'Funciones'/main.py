#Comenzamos con funciones.
#@Autor: Juani Sorato
#Definimos una funcion
def mi_funcion(): #para identificar a la funcion utilizamos parentesis
    print('Saludos a todos que miran el archivo desde githb')
    print('No te olvides de darle una estrella a mi repositorio :)')
mi_funcion() #Estamos llamando a la funcion.
mi_funcion() #Se puede llamar a una funcion N cantidad de veces.

#Desempaquetado de la listas o list unpacking
def show(name, lastname):
    print(name+' '+lastname)
person = ['Ariel' , 'Moyano']
show(person[0], person[1]) #pasamos uno por uno los datos de la lista a la funcion.
# vemos como pasarle todo junto
show(*person)#esto es lo mismo que lo anterior pero le pasamos todo junto
#intentamos desempaquetar tuplas
person2 = ('Julian' , 'Alvarez') #desempaquetamos a travez de una tupla.
show(*person2)
#intentamos desempaquetar diccionario
person3 = {"LastName": "Guzman", "name": "Lautaro"}
#show(**person3)


#Repaso de ciclo for  else

numbers = [1,2,3,4,5,6,7,8,9]
for n in numbers:
    print(n)
else: print('Esto se termina')

#List comprehesion, lista de comprension
names = ['Polo', 'Maria', 'Juan','Martina','Marcos','Daniela','Paolo','Patricio','Jaime','Damian','Jacinto']
print(names)
#creamos una lista donde se guarden los nombres con p
alongP = [p for p in names if p[0]=='P'] #esto regresa una nueva lista
print(alongP)
#Creamos una nueva lista donde guardamos los nombres con M
alongM = [m for m in names if m[0]=='M']
print(alongM)
#Creamos una nueva lista donde guardamos los nombres con D
alongD = [d for d in names if d[0]=='D']
print(alongD)
#Creamos una nueva lista donde guardamos los nombres con J
alongJ = [j for j in names if j[0]=='J']
print(alongJ)

#Hacemos lo mismo de arriba pero con diccionarios
bottleC= [{"Name": "Quilmes","Country": "Arg"},
          {"Name": "Corona", "Country": "Mx"},
          {"Name": "Stella Artois","Country": "Belgium"},
          ]

Arg = [b for b in bottleC if b['Country']=='Arg']
print(Arg)
print(bottleC)

#Paso de Argumentos (funciones).
def mi_funcion2(name, lastName):
    print('Saludos a todos los que me ven a traves de github')
    print(f'Nombres: {name}, Apellido: {lastName}')
mi_funcion2('Jorge','Lucero')
mi_funcion2('Ariel','Montoro')
mi_funcion2('Mateo','Aguirre')

#La palabra return en funciones
#Creamos una funcion para sumar
def sumar(a,b):
    return a + b
resultado = sumar(10, 10)
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55 , 45)} ')

def sumar2(a=0 , b=0): #Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'El resultado de la suma: {sumar2(22, 66)}')

#Argumentos, variables en funciones
def listarNombres(*nombres): #Normalmente se utiliza: *args
    for nombre in nombres:
        print(nombre)
listarNombres('lucas','Jose','Martin','Rosa','Nacho')
listarNombres('Marcos','Manuel','Claudia','Clarita')

#def listaTerminos(**terminos): #Lo mas utilizado es **Kwargs para recibir los argumentos3
# for llaves, valor in terminos.iteritems(): #Kwargs significa: key arguments
 #       print(f'{llaves}:{valor}')
#listaTerminos() #No recibe nada, nada se va a mostrar
#listaTerminos(IDE = 'Integrated Develoment Enviroment',px = 'Primariuy Key')
#listaTerminos(Nombre='Leonel Messi')


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Mariana','Manuel','Marcos']
desplegarNombres(nombres2)
desplegarNombres('Carla')

#Funciones recursivas
def factorial(numero):
    if numero ==1: #caso base
        return 1
    else:
        return numero * factorial(numero-1) #Caso recursivo
    
resultado = factorial(5)#LO hacemos en codigo duro
print(f'El factorial del numero 5 es: {resultado}')
    


    
