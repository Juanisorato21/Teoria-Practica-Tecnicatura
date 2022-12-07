"""
# Ejercicio Etapas de vida según la edad:

Haremos un programa que cuando el usuario ingrese su edad le diga,
o imprima la etapa de su vida en una breve oración:

0 a 10 = La infancia es increíble y bella
10 a 19 = Tienes muchos cambios, mucho que estudiar
20 a 29 = Amor y comienza el trabajo
Para las siguientes etapas, deberas completarlo...
"""

edad = int(input("Digite su edad y conocerá la etapa que esta atravesando en su vida: "))
etapa = None

if edad <= 10:
    etapa = "La infancia es increíble y bella"
elif edad >= 11 and edad <= 19:
    etapa = "Tienes muchos cambios, mucho que estudiar"
elif edad >= 20 and edad <= 29:
    etapa = "Amor y comienza el trabajo"
elif edad >= 30 and edad <= 39:
    etapa = "Nueva etapa, grandes cambios y mayores responsabilidades, vienen nuevas y grandes experiencias "
elif edad >= 40 and edad <= 49:
    etapa = "Aun esta mas cerca de la Guitarra que del Arpa "
elif edad >= 50 and edad <= 59:
    etapa = "Etapa en la que se tiene que ir mentalizando para afrontar el examen de próstata :O "
elif edad >= 60 and edad <= 69:
    etapa = "Sientese y disfrute de los frutos de su jubilación"
elif edad >= 70 and edad <= 79:
    etapa = "Va aprendiedo a tocar el Arpa :o "
print(f"Tu edad es: {edad}, {etapa}")