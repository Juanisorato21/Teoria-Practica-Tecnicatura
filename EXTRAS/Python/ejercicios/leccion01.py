"""
miVariable = 3
print(miVariable)
miVariable = 'Hola a toda la gente'
print(miVariable)
miVariable = 'a'
print(miVariable)
miVariable = 3.5
print(miVariable)
miVariable = 'a b,c/d,2,3'
print(miVariable)
# mivariable lo usamos para definir 
# print() es una funcion para imprimir lo que esta entre parentesis
x = 10
y = 2
z = x+y
print (z)
# cuando queremos imprimir una operacion no ponemos las ""
#para saber la direccion de las literales, en que casilla de la ram esta, usamos la funcion ID  
print (id(x))
#las literales se escriben x mas los 3 ultimos numeros ej: x792, unque el numero cmabia permanente mente 
print(id(y))
print(id(z))
#las literales serian x= x688 y= x848 z= x752
#pero siempre que ejecutemos de nuevo el programa las ubicaciones van a cambiar


#Tipos int, float, string, bool

# tipo str
a = "Hola Profesor"
print(type(a))

# tipo flotante o float
a = 10.78
print(type(a))

# Tipo booleanos o bool
a = True
print(type(a))

# Tipo Numericas
a = 10
print(type(a))

# Manejos de cadenas (String)
# si queremos hacer una concatenacion usamos el +
migrupofavorito = "Soda Stereo"+" y "+"BZRP"
print("Mi grupo favorito es: "+migrupofavorito)

numero1= "7"
numero2="8"

print(int(numero1)+ int(numero2))

#Tipos booleanos (bool)
#permite saber si un valor es verdadero o falso
mibooleano = True
print(mibooleano)

mibooleano = 1>2
print(mibooleano)
"""
""""
# si es mayor dice algo y si es menor dice otra cosa
if mibooleano:
    print("El resultado es: verdadero")
else: 
    print("El resultado es Falso")

    #Procesar la entrada de usuarios
    #funcion input
    resultado = Input("Digite un numero")
    Print(resultado)

#Conversasion 
numero1= int(input("Escribe el primer numero: "))
numero2= int(input("Escribe el segundo numero: "))
resultado = numero1+numero2
print("El resultado de lsa suma es: ",resultado)5
"""
'''
altura = int(input("Proporciona la altura del rectangulo: "))
ancho = int(input("Proporciona el ancho del rectangulo: "))

area = altura * ancho
perimetro = (altura + ancho)*2

print(f"El area del rectangulo es de: {area}")
print(f"El perimetro del rectangulo es de: {perimetro}")
'''
"""""
miVariable3 = 10
print(miVariable3)
# Operadores de reasignación
miVariable3 = miVariable3 +1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)
"""""
'''
#Operadores de comparacion
d = 4
b = 2
resultado = d == b #Comprobamos si son iguales
print(resultado)
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
# print("Resultado de la suma:",suma)
print(f"Resultado de la suma es:,{suma}")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")
modulo = operandoA % operandoB
print(f"El resultado de la division o residuo (modulo) es: {modulo}")
exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")

"""
"""
altura = int(input("Proporciona la altura del rectangulo: "))
ancho = int(input("Proporciona el ancho del rectangulo: "))

area = altura * ancho
perimetro = (altura + ancho)*2

print(f"El area del rectangulo es de: {area}")
print(f"El perimetro del rectangulo es de: {perimetro}")
'''
'''
miVariable3 = 10
print(miVariable3)
# Operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

# Operadores de Comparación

d = 4
b = 4
resultado = d == b # Comprobamos si son iguales
print(resultado)

# Operador diferente
resultado = d != b
print(resultado)

# Operador MAYOR que
resultado = d > b
print(resultado)

# Operador MENOR que
resultado = d < b
print(resultado)

# Operador MENOR o IGUAL que
resultado = d <= b
print(resultado)

# Operador MAYOR o IGUAL que
resultado = d >= b
print(resultado)

'''
#Numero par o impar
nro = int(input("ingrese un numero: "))
if nro % 2 == 0: print(f"El numero {nro} es par")
else: print(f"El numero {nro} es impar")

#Determina si es mayor de edad
edad = int(input("Ingrese su edad: "))
if edad > 18: print("Usted es mayor de edadd")
else: print("Usted es menor de edad")