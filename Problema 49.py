#---------------------------------------------------
#        Problema 49: Diccionario
#---------------------------------------------------
print("Programa que adicional al anterior, muestra el catálogo ingresado.")
print("Programa que muestra la información del producto según el número de referencia.")
productos = []
codigos = []
cant = []
n = int(input("Ingrese la cantidad de productos que desea ingresar: "))
for i in range(n):
    nom = input("Ingrese el nombre del producto: ")
    productos.append(nom)
    barras = int(input("Ingrese el código de barras de dicho producto: "))
    codigos.append(barras)
    stock = int(input("Ingrese la cantidad de producto que hay: "))
    cant.append(stock)
ref = int(input("Ingrese el número de referencia del producto que busca: "))
print("\nInformación del producto:")
print("Nombre:", productos[ref-1])
print("Código:", codigos[ref-1])
print("Cantidad:", cant[ref-1])
print("\nCatálogo completo: ")
for a, b, c in zip(productos, codigos, cant):
    print("Producto:", a, "/", "Cógigo de barras: ", b, "/", "Cantidad disponible: ", c)
