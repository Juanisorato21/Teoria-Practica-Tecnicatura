#Ejercicio 11: Agenda Telefonica
#Hacer un programa que simule una agenda de contactos. Crear un.
# diccionario donde la clave sea el nombre del usuario y el valor.
#sea el telefono, el programa tendra el siguiente menu de opciones:
#           1. Nuevo contacto.
#           2.Borrar contacto.
#           3.Ver contactos existente.
#           4.Salir.

agenda ={}
while True:
    print('\.:Menu:.')
    print('1.Nuevo contacto.')
    print('2.Borrar contacto.')
    print('3.Ver contacto existente.')
    print('4.Bsalir')
    opcion = int(input('Digite una opcion de menu: '))
    
    if opcion == 1:
        nombre = int(input('Digite el nombre del contacto: '))
        telefono = input("Digite el N° Telefonico: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente!')
        else: print('Este nombre de contacto ya existe!')
    elif opcion == 2:
        nombre = input('Cual es el nombre del contacto que desa borrar')
        if nombre in agenda:
            del(agenda[nombre])
            print('Contacto eliminado exitosamente!')
        else: print('Este nombre de contacto no existe')
    elif opcion == 3:
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Telefono: {valor}')
            break
    else: print('Se equivoco de opcion de menu')
    print()