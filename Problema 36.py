#------------------------------------------------------------
#    Problema 36: Repetir elevación al cuadrado.
#------------------------------------------------------------
print("Programa que muestre el cuadrado de un numero hasta que el usuario quiera.")
R = 1
while R == 1:
    num = float(input("Ingrese el número que quiere elevar al cuadrado: "))
    c = num**2
    print("El cuadrado de", num, "es:", c)
    R = int(input("Presione 1 para elevar otro número, cualquier otro número para salir: "))
print("Programa finalizado.")
