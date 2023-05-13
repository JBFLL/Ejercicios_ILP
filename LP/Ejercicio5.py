#Ejercicio 5

#Entrada
a=int(input("Ingrese el valor de a:"))
b=int(input("Ingrese el valor de b:"))
c=int(input("Ingrese el valor de c:"))

#Proceso

x1=(-b-(pow((b**2)-(4*(a*c)),1/2)))/(2*a)
x2=(-b+(pow((b**2)-(4*(a*c)),1/2)))/(2*a)

#Salid
print(x1)
print(x2)