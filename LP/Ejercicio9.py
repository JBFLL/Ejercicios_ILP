#Ejercicio 9
#Entrada
dias_trabajados = float(input("Ingrese la cantidad de días trabajados en el mes de mayo: "))
pago_por_dia = 500

#Proceso
pago_bruto = dias_trabajados * pago_por_dia
iva_trasladado = pago_bruto * 0.16
subtotal= pago_bruto + iva_trasladado
iva_retenido = iva_trasladado * 2/3
isr_retenido = pago_bruto *0.1
salario = round (subtotal - iva_retenido - isr_retenido,2)

#Salida
print("El salario del empleado para el mes de mayo de 2023 es de:", salario, "pesos.")