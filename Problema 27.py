#Problema 27: Area o perimetro de un cuadrado
import sys
print("Programa que saque el area o el perimetro de un cuadrado segun lo que quiera el usuario.")
L = float(input("Por favor, ingrese la medida de uno de los lados: "))
if L < 0:
    print("Error, has ingresado una medida negativa.")
    sys.exit()
A = L**2
P = L*4
R = int(input("Presione 1 para sacar el area o 2 para sacar el perimetro: "))
if R == 1:
    print("El area es: ", A)
elif R == 2:
    print("El perimetro es: ", P)
else:
    print("Error, opcion invalida.")
    
