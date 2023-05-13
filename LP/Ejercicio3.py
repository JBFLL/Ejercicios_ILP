# EJERCICIO 3

import datetime
# # #ENTRADA

fecha_actualL = datetime.datetime.now()
año_Actual= fecha_actualL.year
año_nacimiento=int(input("Ingrese el año de su nacimiento:"))


# # #PROCESO

edad= (año_Actual-año_nacimiento)

# # #SALIDA
print ("Usted tiene",edad,"años")