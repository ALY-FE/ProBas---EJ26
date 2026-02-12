#Problema 17: Cálculo de beneficio.
print("Programa que calcula y muestra el beneficio total.")
PV = float(input("Ingrese el precio de venta: "))
N = float(input("Ingrese la cantidad vendida: "))
CF = float(input("Ingrese el costo fijo: "))
CV = float(input("Ingrese el costo variable por pieza: "))
BT = (PV * N) - (CF + (CV *N))
print("El beneficio total es: ", BT)
