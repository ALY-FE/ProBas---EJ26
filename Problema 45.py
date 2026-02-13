#---------------------------------------------------------------------
#      Problema 45:Calculadora con repetición por operación.
#---------------------------------------------------------------------
import sys
print("Programa que simula una calculadora básica.")
R = 1
while R == 1:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    c = int(input("Seleccione la operación a realizar:\n"
                  "1) Suma\n"
                  "2) Resta\n"
                  "3) Multiplicación\n"
                  "4) División\n"
                  "5) Exponenciación\n"
                  "6) Módulo\n"
                  "Cualquier otro número para salir.\n"))
    r = 1
    while r == 1:
        if c == 1:
            print("El resultado de la suma de", num1, "+", num2, "es:", num1+num2)
        elif c == 2:
            print("El resultado de la resta de", num1, "-", num2, "es:", num1-num2)
        elif c == 3:
            print("El resultado de la multiplicación de", num1, "x", num2, "es:", num1*num2)
        elif c == 4:
            if num2 != 0:
                print("El resultado de la división de", num1, "/", num2, "es:", num1/num2)
            else:
                print("ERROR, no se puede dividir entre 0.")
        elif c == 5:
            print("El resultado de la exponenciación de", num1, "**", num2, "es:", num1**num2)
        elif c == 6:
            if num2 != 0:
                print("El residuo de la división de", num1, "/", num2, "es:", num1%num2)
            else:
                print("ERROR, no se puede dividir entre 0.")
        else:
            print("Ha finalizado el programa.")
            sys.exit()
        r = int(input("Presione (1) para repetir o (2) para cambiar la operación: "))
    R = int(input("Seleccione (1) para realizar otra operación o cualquier otro número para salir: "))

print("Ha finalizado el programa.")
