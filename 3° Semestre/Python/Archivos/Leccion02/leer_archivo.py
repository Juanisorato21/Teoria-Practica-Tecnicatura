
#archivo = open('c: \\usuario\\juani\\Teoria-Practica-Tecnicatura\\3° Semestre\\Python\\Archivos\\Leccion02\\prueba.txt' , 'r' , ' a')
try:
    archivo = open('prueba.txt','r',encoding = 'utf-8')
# print(archivo.read())
# print(archivo.read(5))
# print(archivo.read(10)) #continuamos desde la linea anterior
# print(archivo.readLine())
# print(archivo.readLine())
except Exception as e:
    print(e)
# Vamos a iterar el archivo, cada una de las lineas
# for linea in archivo:
    # print(linea) #iteramos todos los elementos del archivo
    # print(archivo.readline()) #accedemos al archivo como si fuera una lista
# print(archivo.readline()[17])

# Anexamos informacion, copiamos a otro
finally: 
    archivo2 = open('copia.txt','a',encoding='utf-8')  
    archivo2.write(archivo.read())
    archivo.close() #cerramos el primer archivo
    archivo2.close() #cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')

#Las veces que ejecutemos el programa va a copiar en el archivo: copia.txt
# para que no copie mas info debemos cambiar la (A) por la (W)
