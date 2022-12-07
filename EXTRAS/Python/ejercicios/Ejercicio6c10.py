#Ingresar N° enteros, visualizar la suma de los numeros pares de la lista, cuantos numeros pares existen y cual es el promedio de los numeros impares
i = 1
sumapares=0
sumaimpares=0
conteopar=0
conteoimpar=0
promedioimpares=0

while i <= n_elementos:
    num = int(input(f"{i} Digite un numero: "))
    if num % 2 ==0: 
        sumapares += num
        conteopar += 1
    else: 
        sumaimpares += num
        conteoimpar += 1
        promedioimpares= sumaimpares/conteoimpar
    i += 1 
print(f"La suma de los Numeros pares es: {sumapares}")
print(f"La suma de los Numeros impares es: {sumaimpares}")
print(f"La cantidad de N° pares son: {conteopar}")
print(f"La cantidad de N° impares son: {conteoimpar}")
Print(f"EL promedio de los N° impares son: {promedioimpares}")
