import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='root',
    host='127.0.0.1',
    database='test_bd'
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia) # De esta manera ejecutamos la sentencia.
registros = cursor.fetchall() # Recuperamos todos los registros que seran una lista.
print(registros)

cursor.close()
conexion.close()
