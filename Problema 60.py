#--------------------------------------------
#      Problema 60: Función promedio
#--------------------------------------------

print("Programa que crea una función que calcula el promedio en base a la función sumatoria.")

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

   #Se define la función del promedio.
def promedio(numeros):
    if len(numeros) != 0:
        prom = sumatoria(numeros) / len(numeros)
        return prom
    else:
        print("No se agregó ningún número.")

   #Se muestra el resultado tanto de la sumatoria como del promedio.
print("La suma de los números ingresados es: ", sumatoria(numeros))
print("El promedio de los números ingresados es: ", promedio(numeros))
