#Problema 28: Mayoria de edad.
import sys
print("Programa que muestra si el usuario es mayor de edad o no.")
edad = int(input("Por favor, ingrese su edad: "))
if edad < 0:
    print("Error, caracter '-' invalido")
    sys.exit()
elif edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
