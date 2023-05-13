# EJERCICIO 4

#ENTRADA


grados_c= float(input("Igrese grados C:"))
grados_k= float(input("Igrese grados K:"))
grados_f= float(input("Igrese grados F:"))

# PROCESO
#°C
k = round(grados_c + 273.15,2)
f = round(((9 * grados_c) / 5) + 32,2)

#°K
kc = round(grados_k - 273.15,2)
kf = round(((9 * (grados_k - 273.15) / 5) + 32),2)

    
#°F
fc = round((5 * (grados_f - 32) / 9),2)
fk = round((5 * (grados_f - 32) / 9) + 273.15,2)

# SALIDA
print(grados_c,"°C EQUIVALEN A", k,"°K") 
print(grados_c,"°C EQUIVALEN A", f,"°F")
print(grados_k,"°K EQUIVALEN A", kc, "°C") 
print(grados_k,"°K EQUIVALEN A", kf, "°F")
print(grados_f,"°F EQUIVALEN A", fc,"°C") 
print(grados_f,"°F EQUIVALEN A", fk,"°K")