#------------------------------------------------
#      Problema 62: Función parametrizada
#------------------------------------------------

print("Programa que crea una función promedio e indica en que oportunidad queda.")

   #Se llena una lista con las 3 calificaiones.
calificaciones = []
for i in range(3):
    cals = float(input("Ingrese una calificación: "))
    calificaciones.append(cals)

   #Se define la función.
def promedio(calificaciones):
    suma = sum(calificaciones)
    prom = suma / 3
    if prom >= 70:
        print("El alumno aprobó en primeras con", prom)
    else:
        print("Con", prom, "te vas a extras.")

   #Se llama a la función.
promedio(calificaciones)
