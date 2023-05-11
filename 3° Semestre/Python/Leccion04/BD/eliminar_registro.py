import psycopg2
conexion = psycopg2.connect(user='postgres', password='root', host='127.0.0.1', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            entrada = input('Digite ID a eliminar: ')
            #valores = (4,) #sin la coma no es una tupla, es una tupla de valores
            valores = (entrada,)
            cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia.
            registros_eliminados = cursor.rowcount
            print(f'Los regitros aeliminados son: {registros_eliminados}')


except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
