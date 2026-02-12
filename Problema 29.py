#Problema 29: Division segura.
import sys
print("Programa que realiza divisiones.")
dividendo = float(input("Por favor, ingrese el dividendo: "))
divisor = float(input("Por favor, ingrese el divisor: "))
if divisor == 0:
    print("Error, el divisor no puede ser 0.")
    sys.exit()
else:
    print("El cociente es: ", dividendo/divisor)
