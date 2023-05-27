#Ejercicio 8
#Entrada
num= float(input("Ingrese un numero:"))

#Proceso
if(num<0 and num >-100):
    for i in range (-1,-100,-2):
        print(i)
elif(num>0 and num < 100):
    j=2
    while  (j <= 100):
        print(j)
        j= j + 2
else:
    print("no valido")
