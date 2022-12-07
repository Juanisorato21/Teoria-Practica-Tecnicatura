#Calcular el factoria de un numero mayor o igual a 0
numero=int(input("Ingrese un numero: "))
factorial=1 
if numero!=0:
    for i in range (1,numero+1):
        factorial=factorial*i
print("factorial: ",factorial)
