#Problema 30: Analisis de beneficios.
print("Programa que define si una empresa tiene perdidas, ganancias o un equilibrio.")
PUP = float(input("Ingrese el precio unitario por producto: "))
C = float(input("Ingrese la cantidad vendida: "))
E = float(input("Ingrese el total de egresos de la empresa: "))
IT = PUP*C
if IT < E:
    print("La empresa sufre perdidas.")
elif IT == E:
    print("La empresa esta en un punto de equilibrio.")
else:
    print("La empresa esta generando ganancias.")
