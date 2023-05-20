#Entrada de Datos
calificacion1=float(input("Ingresa calificacion 1:"))
calificacion2=float(input("Ingresa calificacion 2:"))
calificacion3=float(input("Ingresa calificacion 3:"))

#Proceso

promedio=round((calificacion1+calificacion2+calificacion3)/3,2)

if (promedio >6 and promedio <= 10):
    print("el promedio es", promedio,"Aprobado")
elif (promedio >= 0 and promedio < 6):
    print("el promedio es", promedio, "Reprobado")
elif(promedio == 6):
    print("el promedio es", promedio,"Aprobado de panzaso")
elif(promedio <0 or promedio>10):
    print("el promedio es", promedio,"Promedio Invalido")
