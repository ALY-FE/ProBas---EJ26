#---------------------------------------------------
#      Problema 65: Función factorial
#---------------------------------------------------

print("Programa que muestra la cantidad total de números ingresados y sus factoriales.")

   #Se crea la lista original vacía y se define el contador.
lista_original = []
contador = 0

   #Se define una función para el ingreso de números a la lista_original.
def llenado_lista():
    while True:
        num = int(input("Ingrese el número para agregarlo a la lista o 0 para sacar los factoriales: "))
        if num == 0:
            break
        lista_original.append(num)

   #Se llama a la función llenado_lista.
llenado_lista()

   #Se realiza el conteo de los números ingresados.
contador = len(lista_original)

   #Se crea la lista donde iran los factoriales.
lista_factorial = []

   #Se crea la función para llena la lista_factorial.
factorial = 1
def factoriales():
    for num in lista_original:
        factorial = 1
        for i in range(1, num+1):
            factorial = factorial * i
        lista_factorial.append(factorial)

   #Se llama a la función factoriales.
factoriales()

   #Se imprimen ambas listas.
print("La lista original era: ", lista_original)
print("Los factoriales son: ", lista_factorial)
        
