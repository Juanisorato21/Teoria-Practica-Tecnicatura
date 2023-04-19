from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp
opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar pelicula')
        print('2. Ver catalogo')
        print('3. Eliminar catalogo')
        print('4. Salir')
        opcion = int(input('Digite una opcion de Menú (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Digite el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_peliculas(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'¡¡ERROR!!: {e}')
        opcion = None

    else:
       print('Salimos del programa')
       print('©Juan Sorato')
