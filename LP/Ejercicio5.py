#Ejercicio 5

#Entrada
a=int(input("Ingrese el valor de a:"))
b=int(input("Ingrese el valor de b:"))
c=int(input("Ingrese el valor de c:"))

#Proceso

x1=round((-b-(pow((b**2)-(4*(a*c)),1/2)))/(2*a),2)
x2=round((-b+(pow((b**2)-(4*(a*c)),1/2)))/(2*a),2)

#Salida
print("x1=",x1)
print("x2=",x2)