import psycopg2 as bd

conexion =bd.connect(user='postgres',password='root',host='127.0.0.1',database='test_bd')

try:
    conexion.autocommit = False # no deberia estar, inicia la transacción
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido,email)VALUES(%s, %s, %s)'
    valores = ('Marcelo', 'prol45612355', 'prol.marcelo@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Armando','Soratto','armanditosoratto01@mail.com',14)
    cursor.execute(sentencia, valores)

    conexion.commit()  #Hacemos el commit manualmente, se cierra la transacción
    print('Termina la transacción')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}') #rollback (retrae todos los cambios realizados)
finally:
    conexion.close()