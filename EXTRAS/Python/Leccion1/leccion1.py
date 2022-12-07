"""
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# Las literales se escriben x656, la variable y = 400 , la variable z = 720
print(id(y))
print(id(z))
# Literal Booleana
a = False
print(type(a))

# tipos int, Float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(type(x))
x = True
print(x)
print(type(x))


# Manejo de Cadenas(String)
miGrupoFavorito = "Linkin Park"
caracteristicas = "The Best Punk Band"
print("Mi Grupo favorito es:", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# Tipos Boleanos (bool) verdadeo o falso

miBooleno = 3 > 2
print(miBooleno)

if miBooleno:
    print("El Resultado es Verdadero")
else:
    print("El Resultado es Falso")
# Procesar la entrada del usuario
# Funcion imput
resultado = input("Digite un Numero: ")  # Regresa un dato tipo String
print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero"))
numero2 = int(input("Escribe el segundo numero"))
resultado = int(numero1) + int(numero2)
print("el resultado de la suma es: ", resultado)
"""
"""
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
"""
"""
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
"""
"""
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
"""
"""
#Numero par o impar
nro = int(input("ingrese un numero: "))
if nro % 2 == 0: print(f"El numero {nro} es par")
else: print(f"El numero {nro} es impar")

#Determina si es mayor de edad
edad = int(input("Ingrese su edad: "))
if edad > 18: print("Usted es mayor de edadd")
else: print("Usted es menor de edad")
"""
"""

#Operadores Logicos

a = False
b = False
resultado = a and b
print(resultado)

#operador or
resultado = a or b
print(resultado)

#operador not
resultado = not a
print(resultado)
"""
"""
#Ejercicio; Valor dentro de un rango
valor = int(input("Digite un numero"))
valorMinimo = 0
valorMaximo = 5
demtrpRamgp = (valor >= valorMinimo and valor <- valorMaximo)
if dentroRango:
    print(f"El valor {valor} esta dentro del rango ")
else:
    print("f El valor{valor} No esta dentro del rango")
"""
"""
# Ejercicio con el operador or, operador not
vacaciones = False
diaDescanso = True
if not vacaciones or diaDescanso :
    print("Tiene trabajo que hacer")
else:
    print("Puede asistir al juego")

# Ejercicio: Rango entre 20 y 30
edad = input(input("Digite su edad: "))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)
"""
"""
#if veinte or treinta:
if (20 <= edad < 30 ) or (30 <= edad < 40 ): # sintaxis simplificada del operados and
    print("Estas dentro del rango de los (20'0) a (30'0) años")
#   if veinte:
#       print("Estas dentro del rango de los (20\'0) años")
#    elif treinta:
#        print("Estas dentro del rango de los (30\'0) años")
#    else:
#        print("No estas dentro del rango")
else:
    print("No estas dentro del rango de los (20'0) a (30'0) años ")
"""
"""
#Ejercicio: el mayor de dos numeros

numero1 = int(input("Digite el valor para el numero1: "))
numero2 = int(input("Digite el valor para el numero2: "))

if numero1 > numero2:
    print("El numero 1 es mayor")
else:
    print("El numero2 es mayor")
"""

#Ejercicio: Tienda de Libros
print("Digite los siguientes datos del libro")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el id del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indicar si el libro es gratuito (True/False: ")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto, debe escribir True/False"
print(f'''
    Nombre: {nombre}
    Id: {id}
    precio: {precio}
    EnvioGratuito?: {envioGratuito}
''')







