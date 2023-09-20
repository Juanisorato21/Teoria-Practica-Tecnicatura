import psycopg2

# Conectarse a la base de datos PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="nombre_basedatos",
    user="usuario",
    password="contraseña"
)

# Crear la tabla en la base de datos si no existe
def crear_tabla():
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(50),
                apellido VARCHAR(50),
                telefono VARCHAR(15),
                email VARCHAR(50),
                direccion VARCHAR(100)
            );
        ''')
        conn.commit()
        cursor.close()
        print("Tabla creada exitosamente.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Insertar un nuevo usuario en la base de datos
def insertar_usuario(nombre, apellido, telefono, email, direccion):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nombre, apellido, telefono, email, direccion)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id;
        ''', (nombre, apellido, telefono, email, direccion))
        id_usuario = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        print("Usuario insertado exitosamente. ID:", id_usuario)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Obtener y mostrar todos los usuarios guardados
def mostrar_usuarios():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios;")
        usuarios = cursor.fetchall()
        cursor.close()
        if usuarios:
            print("Usuarios:")
            for usuario in usuarios:
                print(usuario)
        else:
            print("No se encontraron usuarios.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Ejecutar el programa principal
if __name__ == '__main__':
    # Pedir los datos al usuario
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    telefono = input("Ingrese su número de teléfono: ")
    email = input("Ingrese su correo electrónico: ")
    direccion = input("Ingrese su dirección: ")

    # Crear la tabla si no existe
    crear_tabla()

    # Insertar el usuario en la base de datos
    insertar_usuario(nombre, apellido, telefono, email, direccion)

    # Mostrar los usuarios guardados
    mostrar_usuarios()

    # Cerrar la conexión a la base de datos
    conn.close()
