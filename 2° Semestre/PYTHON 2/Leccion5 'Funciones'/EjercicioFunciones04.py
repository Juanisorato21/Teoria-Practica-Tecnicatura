#Ejercicio 4: Calculadora de impuestos
#Crear una funcion para calcular el total de un pago incluyendo 
#El impuesto al valor agregado (IVA)
#formula: pago_total = pago_sin_impuestos + pago_sin_impuestos*(impuesto/100)
#proporcione el pago sin p¿impuestos: 1000
#proporcione el pago con impuesto: 21%
#pago con impuesto: xxxxx

#Creamos la funcion 
def pagar_impuestos(pago_sin_impuestos, impuesto):
    pago_total = pago_sin_impuestos + pago_sin_impuestos*(impuesto/100)
    return pago_total
#Ejecutamos la funcion
pago_sin_impuestos = float(input('Digite el pago sin impuestos: '))
impuesto = float(input('Digite el monto del impuesto a aplicar: '))

pago_con_impuestos = pagar_impuestos(pago_sin_impuestos,impuesto)
print(f'El pago con impuesto es {pago_con_impuestos}')