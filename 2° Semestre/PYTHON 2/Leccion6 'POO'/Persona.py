class Persona: #Creamos una clase
    def __init__(self,nombre,apellido,edad):   #Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self): # Self: su sintaxis es identica a this
        print(f'Persona: {self.nombre}, {self.apellido}, {self.edad}')
        
persona1 = Persona()
    
#print(persona1.nombre) -> Juan
#print(persona1.apellido) -> Baldoza
#print(persona1.edad) -> 22

persona1 = Persona('Juani','Sorato',19) #Necesitamos enviar argumentos
print(f'El nombre es {persona1.nombre}')
print(f'El apellido es {persona1.apellido}')
print(f'La edad es {persona1.edad}')

persona2 = Persona('Matias','Funes',24)
print(f'El objeto de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Leonel'
persona1.apellido = 'Messi'
persona1.edad = 35
print(f'El obejto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

#*****************************************************************************************************************************
#Los atributos son: caracteristicas
#Los metodos son: el comportamiento que van a tener los objetos (acciones)

Persona.mostrar_detalle(persona1)#La referencia se pasa de manera automatica



