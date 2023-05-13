# EJERCICIO 4

#ENTRADA


GRADOS_C= float(input("Igrese grados C:"))
GRADOS_K= float(input("Igrese grados K:"))
GRADOS_F= float(input("Igrese grados F:"))

# PROCESO
#°C
K = GRADOS_C + 273.15
F = ((9 * GRADOS_C) / 5) + 32

#°K
KC = GRADOS_K - 273.15
KF = ((9 * (GRADOS_K - 273.15) / 5) + 32)

    
#°F
FC = (5 * (GRADOS_F - 32) / 9)
FK = (5 * (GRADOS_F - 32) / 9) + 273.15

# SALIDA
print(GRADOS_C,"°C EQUIVALEN A", K,"°K") 
print(GRADOS_C,"°C EQUIVALEN A", F,"°F")
print(GRADOS_K,"°K EQUIVALEN A", KC, "°C") 
print(GRADOS_K,"°K EQUIVALEN A", KF, "°F")
print(GRADOS_F,"°F EQUIVALEN A", FC,"°C") 
print(GRADOS_F,"°F EQUIVALEN A", FK,"°K")