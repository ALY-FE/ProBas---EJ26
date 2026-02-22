#----------------------------------------------------------
#         Problema 46: Elevaciones
#----------------------------------------------------------
print("Programa que recibe 10 números y los eleva al cuadrado.")
lista = []
resultado = []
for n in range(10):
    num = int(input("Ingrese un número: "))
    lista.append(num)
print("Los numeros elevados al cuadrado son: ")
for n in lista:
    print(n**2)
