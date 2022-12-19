class Persona: #Creamos una clase
    def __init__(self):   #Se lo llama metodo Init Dunder
        self.nombre = 'Juan'
        self.apellido = 'Baldoza'
        self.edad = 22
        
persona1 = Persona()
    
#print(persona1.nombre) -> Juan
#print(persona1.apellido) -> Baldoza
#print(persona1.edad) -> 22

print(f'El nombre es {persona1.nombre}')
print(f'El apellido es {persona1.apellido}')
print(f'La edad es {persona1.edad}')
