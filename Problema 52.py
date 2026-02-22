#-------------------------------------------------------
#          Problema 52: Productos
#-------------------------------------------------------
print("Programa que imprime información de 5 productos.")
productos = ["Papel", "Jabón", "Detergente", "Desinfectante", "Shampoo"]
precios = [34.90, 46.50, 57.50, 42.50, 74.99]
ventas = [45, 69, 49, 50, 102]
print("Reporte de ventas:")
for a, b, c in zip(productos, precios, ventas):
    print("\nProducto:", a, "/ Precio: $", b, "/ Ventas por día: ", c, "unidades")
