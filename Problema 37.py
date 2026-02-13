#------------------------------------------------------------
#    Problema 37: Interes compuesto con repetición
#------------------------------------------------------------
print("Programa que calcula el interes compuesto hasta que el usuario quiera.")
R = 1
while R == 1:
    C = float(input("Ingrese el capital inicial: "))
    i = float(input("Ingrese la tasa de interes: "))
    n = int(input("Ingrese el numero de periodos: "))
    M = C * (1 + i) ** n
    print("El monto final es de", M)
    R = int(input("Presione 1 para sacar otro monto, cualquier otro numero para finalizar: "))
print("Programa finalizado.")
