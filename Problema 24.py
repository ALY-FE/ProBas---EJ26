#Problema 24: Interés simple y compuesto.
print("Programa que calcula y muestra el capital final usando interés simple y compuesto.")
CI = float(input("Ingrese el capital inicial: "))
TI = float(input("Ingrese la tasa de interés (porcentaje anual en decimal): "))
NP = float(input("Ingrese el número de periodos (en años): "))
IS = CI*TI*NP
MS = CI + IS
MC = CI*(1+TI)**NP
IC = MC - CI
print("El interés simple es de ", IS, "y su monto es", MS)
print("El interés compuesto es de ", IC, "y su monto es", MC)


