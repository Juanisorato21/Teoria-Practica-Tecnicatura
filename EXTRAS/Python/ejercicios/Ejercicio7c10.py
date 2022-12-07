#Dadas las horas trabajadas y la tarifa de pago, calcula es salario y la sumatoria de cada salario
#Dadas las horas trabajadas de 5 personas y la tarifa de pago. Calcula el salario y la sumatoria de todos los salarios en python
nombre = input("Ingrese el nombre del operario: ")
horas = int(input("Ingrese las horas trabajadas: "))
pago = float(input("Ingrese el precio de la hora trabajada: "))

if horas > 48: 
    extras = horas - 48
    sueldo = (48*pago)+(extra*(pago+pago*.5))

