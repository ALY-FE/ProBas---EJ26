#-------------------------------------------------------
#          Problema 51: Asistencia
#-------------------------------------------------------
print("Programa que registra y muestra la asistencia de n trabajadores.")
nombres = []
asistencia = []
n = int(input("Ingrese la cantidad de personas que desea agregar a la lista: "))

for i in range(n):
    nom = input("Ingrese el nombre completo: ")
    nombres.append(nom)
    while True:
        res = int(input("Ingrese 0 si no asistio o 1 si lo hizo: "))
        if res == 0:
            asistencia.append("no asistio")
            break
        elif res == 1:
            asistencia.append("asistio")
            break
        else:
            print("ERROR, intentelo de nuevo.")

print("\nLista completa: ")
for a, b, in zip(nombres, asistencia):
    print("Nombre: ", a, b, "a trabajar.")
