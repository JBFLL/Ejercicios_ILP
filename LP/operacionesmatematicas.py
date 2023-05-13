# Ejmplo 2. Operaciones Mteamaticas: 
#Suma, resta Mult, Div,  Potencia, Raiz, Modulo

#Importar una librearia de fucniones matematecas
import math

# ENTRADA DE DATOS
#declarar Variables
numero_1=float(input("escribe el 1er numero: "))
numero_2=float(input("Escribe el 2d0 numero: "))


# PROCESOS (Operaciones o calculos matematicos y/o logicos)

suma = numero_1+ numero_2
resta = numero_1-numero_2
multiplicacion=numero_1*numero_2
division =numero_1/numero_2
potencia_1= numero_1** numero_2
potencia_2= pow(numero_1,numero_2)
cuadrado = numero_1 ** 2
cubo = pow(numero_2,3)
raiz_cuadrada_1= math.sqrt(9)
raiz_cuadrada_2= pow(9,1/2)
raiz_cubica = pow (27,1/3)
modulo_residuo= 20 % 6


# SALIDA DE DATOS
print("la suma es =",round(suma,2))
print("la resta es =",round(resta,2))
print("la multiplicacion es =",round(multiplicacion,2))
print("la division es =", division)
#print("La suma es"+ suma) #concatenacion (union de 2 o mas textos) aqui marca error, se soluciona con un casteo
#CASTEO
print("la suma es =", str(suma))
print(f"la suma es = {suma}")
print("la potencia es =",potencia_1)
print("la potencia es =",potencia_2)
print("el cuadrado es =",cuadrado)
print("el cubo es =",cubo)
print("El resultado del modulo o residuo de 20%6 es =",modulo_residuo)

