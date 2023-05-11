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
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            # 'SELECT * FROM persona'
            # 'SELECT id_persona, nombre FROM persona'
            # 'SELECT * FROM persona WHERE id_persona = 1'
            # 'SELECT * FROM persona WHERE id_persona = %s' Placeholder
            id_persona = input('Ingrese número ID: ')
            cursor.execute(sentencia,(id_persona,)) # De esta manera ejecutamos la sentencia.
            registros = cursor.fetchone() # Recuperamos todos los registros que seran una lista.
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

# https://www.psycopg.org/docs/usage.html
