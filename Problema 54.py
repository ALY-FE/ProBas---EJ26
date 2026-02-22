#-------------------------------------------------------
#         Problema 54: Lista de ahorros
#-------------------------------------------------------
print("Programa que enlista ahorradores.")
nombres = []
ahorros = []
n = int(input("Ingrese la cantidad de personas que desee en la lista: "))
for i in range(n):
    nom = input("Ingrese el nombre completo del ahorrador: ")
    nombres.append(nom)
    cant = float(input("Ingrese su ahorro: "))
    if cant < 1000:
        ahorros.append("no tendrás para tú futuro.")
    elif cant > 1000000:
        ahorros.append("ya merito te retiras.")
    else:
        ahorros.append("vas bien.")
for a, b in zip(nombres, ahorros):
    print("\n", a, b)
