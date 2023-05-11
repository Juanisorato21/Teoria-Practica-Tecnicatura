import psycopg2
conexion = psycopg2.connect(user='postgres', password='root', host='127.0.0.1', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Julian', 'Alvarez', 'araña@mail.com', 6)
            cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia.
            registros_actualizados = cursor.rowcount
            print(f'Los regitros actualizados son: {registros_actualizados}')


except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()