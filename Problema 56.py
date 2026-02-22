#---------------------------------------------------------------
#         Problema 56: Lista de números o de nombres
#---------------------------------------------------------------
print("Programa que agrega 10 números concecutivos al último valor de la lista.")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
ultimo = lista[-1]
for n in range(1, 11):
    lista.append(ultimo + n)
print(lista)
