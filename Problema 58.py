#--------------------------------------------
#      Problema 58: Lista de números.
#--------------------------------------------

print("Programa que permite al usuario agregar valores a una lista")

   #Se define la lista y la variable para agregar valores a la lista.
numeros = list()

   #Se define la función
def llenar_lista():
    while True:
        num = float(input("Ingrese el número para agregar a la lista ó 0 para salir: "))
        if num ==0:
            break
        numeros.append(num)
llenar_lista()
   #opcional
print(numeros)
