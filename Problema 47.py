#-----------------------------------------------
#       Problema 47: "n" Calificaciones
#-----------------------------------------------
print("Programa que recibe calificaciones, muestra el promedio y la calificación junto a su materia.")
materia = []
cals = []
suma = 0
n = int(input("Ingrese la cantidad de materias a ingresar: "))
for i in range(n):
    nombre = input("Ingrese el nombre de la materia: ")
    materia.append(nombre)
    cal = float(input("Ingrese la calificación de la materia: "))
    cals.append(cal)
for i in cals:
    suma = suma + i
prom = suma / len(cals)
print("\nMateria y calificación:")
for a, b in zip(materia, cals):
    print("Materia:",a,"/","Calificación: ",b)
print("\nEl promedio es: ", prom)
