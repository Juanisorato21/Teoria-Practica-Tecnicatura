# Declaramos una variable 

try:
    archivo = open('prueba.txt', 'w',encoding = 'utf8') 
    # R: (read) Leer las linea del archivo por consola
    # A: (append) anexar al archivo
    # X: () utilizamos para crear el archivo, salta error si el archivo no existe
    # W (write) Utilizamos para escribir el archivo
    # T: es para texto o text
    # B: archivos binarios
    # W+: leer y escribir archivos
    # R+: Escribir y leer archivos 
    # encoding='utf8' usamos para que muestre los acentos
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('Como por ejemplo: acción, ejecución y producción\n')
    archivo.read('Saludos a todos los alumnos de la tecnicatura\n')
    archivo.write('Con esto terminamos\n')
except Exception as e:
    print(e)
finally: #siempre se ejecuta, es decir que siempre va a cerrar el archivo
    archivo.close() #con esto se debe cerrar el archivo
    
    #El archivo esta cerrado, no podemos manipularlo si el archivo esta cerrado
# -> -> archivo.write('todo ok') 
    