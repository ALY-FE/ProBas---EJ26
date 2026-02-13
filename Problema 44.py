#--------------------------------------------------------------------
#        Problema 44: Calculadora básica con repetición
#--------------------------------------------------------------------
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
                  "5) Exponente\n"
                  "6) Módulo\n"
                  "Cualquier otra opción para salir."))
    if c == 1:
        print("El resultado de la suma es:", num1+num2)
    elif c == 2:
        print("El resultado de la resta es:", num1-num2)
    elif c == 3:
        print("El resultado de la multiplicación es:", num1*num2)
    elif c == 4:
        if num2 != 0:
            print("El resultado de la división es:", num1/num2)
        else:
            print("ERROR, no se puede dividir entre 0.")
    elif c == 5:
        print("El resultado de la exponenciación es:", num1**num2)
    elif c == 6:
        if num2 != 0:
            print("El residuo de la división es:", num1%num2)
        else:
            print("ERROR, no se puede dividir entre 0.")
    else:
        print("Ha finalizado el programa.")
        sys.exit() 
    print("¿Desea realizar otra operación?")
    R = int(input("Seleccione (1) para continuar o cualquier otro número para finalizar: "))
