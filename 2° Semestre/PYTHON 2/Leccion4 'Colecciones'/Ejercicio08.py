#Ejercicio 08: Menu interactivo - cajero automatico
#Hacer un programa que simule un cajero automatico con un.
#inicial de 1000$ y tendra la siguientes opciones:
#               1. Ingresar dinero en la cuenta.
#               2. Retirar dinero de la cuenta.
#               3. Mostrar dinero disponible.
#               4. salir

saldo = 1000
while True:
    print('\t.MENU:.')
    print('1. Ingresar dinero en la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    opcion = int(input('Digite el numero de la opcion a elegir: '))
    if opcion == 1:
        extra = float(input('Cuanto dinero desea ingresar -> '))
        saldo += extra
        print(f'Dinero en la cuenta al momento: ${saldo}')
    elif opcion == 2:
        retirar = float(input('Cuando dinero desea retirar->'))
        if retirar > saldo: print('No tiene esa cantidad de dinero')
        else:
            saldo -= retirar
            print(f'Dinero en la cuenta al momento: ${saldo}')
    elif opcion == 3:
        print(f'Dinero en la cuenta al momento: ${saldo}')
    elif opcion == 4:
        print("MUCHAS GRACIAS POR USAR J.PAY")
        break
    else: print("El numero ingresado no exite, intente nuevamente")
    print()
    