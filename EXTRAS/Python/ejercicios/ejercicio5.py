calificacion = int(input("Ingrese un numero del 0 al 10: "))

if 9 <= calificacion <=10:
    print("Su calificacion es A")
elif 8 <= calificacion < 9:
    print("Su calificacion es B")
elif 7 <= calificacion < 8:
    print("su calificacion es C")
elif  6 <= calificacion <7:
    print("su calificacion es D")

elif 0<= calificacion <6:
    print ("Su calificacion es F")

else: print("Lo siento ese numero no es una calificacion")
