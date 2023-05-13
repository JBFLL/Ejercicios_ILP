# EJERCICIO 3

import datetime
# # #ENTRADA

FECHA_ACTUAL = datetime.datetime.now()
AÑO_ACTUAL= FECHA_ACTUAL.year
AÑO_NACIMIENTO=int(input("Ingrese el año de su nacimiento:"))


# # #PROCESO

EDAD= (AÑO_ACTUAL-AÑO_NACIMIENTO)

# # #SALIDA
print ("Usted tiene",EDAD,"años")