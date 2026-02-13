#-----------------------------------------------------------
#        Problema 43: Acumulador de abonos.
#-----------------------------------------------------------
print("Programa que acumula abonos hasta $100,000 en total.")
total = 0
monto = 0
while monto >= 0 and total <= 100000:
    monto = float(input("¿Cantidad a abonar?: "))
    if monto < 0:
        print("ERROR, caracter '-' invalido.")
        monto = float(input("¿Cantidad a abonar?: "))
        total = total + monto
        print("Cantidad actual: $", total)
    else:
        total = total + monto
        print("Cantidad actual: $", total)
print("Ha excedido el límite de $100,000.00")
