#------------------------------------------------------------
#      Problema 50: Más opciones de búsqueda
#------------------------------------------------------------
print("Programa que adicional al anterior, tiene mas formas de busqueda.")
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
    
r = int(input("Si busca el producto por el número de referencia ingrese 1, si lo busca por nombre ingrese 2, si lo busca por su código de barras ingrese 3: "))

if r == 1:
    ref = int(input("Ingrese el número de referencia del producto que busca: "))
    if ref >= 1 and ref <= len(productos):
        print("\nInformación del producto:")
        print("Producto:",productos[ref-1], "/", "Código de barras: ",codigos[ref-1], "/", "Cantidad disponible: ",cant[ref-1])
    else:
        print("Referencia no encontrada")
        
elif r == 2:
    buscar = input("Ingrese el nombre del producto: ")
    for a, b, c in zip(productos, codigos, cant):
        if a == buscar:
            print("\nInformación del producto:")
            print("Producto:",a, "/", "Código de barras: ",b, "/", "Cantidad disponible: ",c)

elif r == 3:
    bar = int(input("Ingrese el código de barras del producto que busca: "))
    for a, b, c in zip(productos, codigos, cant):
        if b == bar:
            print("\nInformación del producto:")
            print("Producto:",a, "/", "Código de barras: ",b, "/", "Cantidad disponible: ",c)

else:
    print("Opción inválida")
    

print("\nCatálogo completo: ")
for a, b, c in zip(productos, codigos, cant):
    print("Producto:", a, "/", "Código de barras: ", b, "/", "Cantidad disponible: ", c)
