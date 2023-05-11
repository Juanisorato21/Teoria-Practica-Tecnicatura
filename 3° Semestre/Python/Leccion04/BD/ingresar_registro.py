import psycopg2
conexion = psycopg2.connect(user='postgres', password='root', host='127.0.0.1', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)'
            valores = ('Carlos', 'Lara', 'carlitosL@mail.com')
            cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia.
            # conexion.commit() --> se utiliza para guardar cambios en la base de datos
            registros_insertados = cursor.rowcount
            print(f'Los regitros insertados son: {registros_insertados}')


except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()