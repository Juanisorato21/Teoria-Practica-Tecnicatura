import psycopg2
conexion = psycopg2.connect(user='postgres', password='root', host='127.0.0.1', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Digite los ID´s a eliminar (separados por comas): ')
            valores = (tuple(entrada.split(',')),) #Tuplas de tuplas
            cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia.
            registros_eliminados = cursor.rowcount
            print(f'Los regitros aeliminados son: {registros_eliminados}')


except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()