# Sistema de Calificaciónes

"""
calificacion = int(input(f"Digite una calificación entre 0 y 10: "))

if calificacion >=9 and calificacion <=10:
    print("A")
elif calificacion >=8 and calificacion <9:
    print("B")
elif calificacion >= 7 and calificacion < 8:
    print("C")
elif calificacion >= 6 and calificacion < 7:
    print("D")
elif calificacion >= 0 and calificacion < 6:
    print("F")
else:
    print("No hay una calificación para ese puntaje. ")
"""

calificacion = int(input(f"Digite una calificación entre 0 y 10: "))

if 9 <= calificacion <= 10:
    print("A")
elif 8 <= calificacion < 9:
    print("B")
elif 7 <= calificacion < 8:
    print("C")
elif 6 <= calificacion < 7:
    print("D")
elif 0 <= calificacion < 6:
    print("F")
else:
    print("No hay una calificación para ese puntaje. ")
