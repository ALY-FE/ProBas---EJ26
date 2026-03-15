#--------------------------------------------
#      Problema 59: Función sumatoria
#--------------------------------------------

print("Programa que crea una función que calcula la sumatoria.")

   #Se crea una lista donde se guardaran los datos a sumar.
numeros = []
while True:
    num = float(input("Ingrese el número a sumar ó 0 para salir: "))
    if num ==0:
        break
    numeros.append(num)

   #Se define la funcion de la sumatoria.
def sumatoria(numeros):
    suma = sum(numeros)
    return suma

   #Muestra de la sumatoria
print("La suma de los números ingresados es: ", sumatoria(numeros))
