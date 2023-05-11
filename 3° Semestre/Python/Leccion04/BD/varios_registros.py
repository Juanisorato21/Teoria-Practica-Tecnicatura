import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='root',
    host='127.0.0.1',
    database='test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' #Placeholder
            entrada = input('Digite el ID a buscar (separado por comas): ')
            llaves_primarias = (tuple(entrada.split(', ')),)
            cursor.execute(sentencia, llaves_primarias) # De esta manera ejecutamos la sentencia.
            registros = cursor.fetchall() # Recuperamos todos los registros que seran una lista.
            for registros in registros:
                print(registros)


except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()