#Problema 33: Evaluacion de vendedor segun volumen de ventas.
print("Programa que muestra la situacion laboral.")
NOM = input("Ingrese su nombre completo: ")
V = float(input("Ingrese su volumen de ventas en pesos: "))
if V < 1000:
    print(NOM, "situacion: DESPEDIDO(A).")
elif V <= 4999.99:
    print(NOM, "situacion: EN PERIODO DE PRUEBA.")
elif V <= 9999.99:
    print(NOM, "situacion: BONO DEL 5%")
else:
    print(NOM, "situacion: BONO DEL 10%")
