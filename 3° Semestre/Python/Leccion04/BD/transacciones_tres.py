import psycopg2 as bd

conexion =bd.connect(user='postgres',password='root',host='127.0.0.1',database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido,email)VALUES(%s, %s, %s)'
            valores = ('Nilda', 'Rojas', 'rojasnilda@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Rodolfo','Roldan','roldanrodo@mail.com', 14)
            cursor.execute(sentencia, valores)

except Exception as e:

    print(f'Ocurrió un error, se hizo un rollback: {e}') #rollback (retrae todos los cambios realizados)
finally:
    conexion.close()
print('Termina la transacción')