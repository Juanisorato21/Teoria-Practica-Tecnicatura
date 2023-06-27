import psycopg2 as bd

conexion =bd.connect(user='postgres',password='root',host='127.0.0.1',database='test_bd')

try:
    #  conexion.autocommit = True # no deberia estar
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido,email)VALUES(%s, %s, %s)'
    valores = ('Marta', 'Marcuzzi', 'mmarcuzzi@mail.com')
    cursor.execute(sentencia, valores)
    conexion.commit()  #Hacemos el commit manualmente
    print('Termina la transacción')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}') #rollback (retrae todos los cambios realizados)
finally:
    conexion.close()