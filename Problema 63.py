#---------------------------------------------------
#      Problema 63: Función para listas.
#---------------------------------------------------

print("Programa que llena una lista y regresa otra con sus cuadrados con funciones.")

   #Se crea la primera lista.
lista1 = []

   #Se define la función para crear la lista.
def lista():
    while True:
        num = float(input("Ingrese un número para agregar a la lista o 0 para finalizar: "))
        if num == 0:
            break
        lista1.append(num)

   #Se llama a la función que crea una lista.
lista()

   #Se crea la segunda lista.
lista2 = []

   #Se define la función para la lista con los cuadrados.
def lista_cuadrados(lista1):
    for i in lista1:
        cuadrado = i**2
        lista2.append(cuadrado)

   #Se llama a la segunda función.
lista_cuadrados(lista1)

   #Se imprimen las listas.
print("La lista original: ", lista1)
print("Sus cuadrados: ", lista2)
