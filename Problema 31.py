#Problema 31: Evaluacion academica.
import sys
print("Programa que indica la situacion academica del alumno.")
CAL = float(input("Por favor ingrese su calificacion (0-10): "))
if CAL < 0 or CAL > 10:
    print("Valor invalido.")
    sys.exit()
elif CAL < 6:
    print("Situacion academica: IRREGULAR")
elif CAL <= 9.9:
    print("Situacion academica: REGULAR")
else:
    print("Situacion academica: EXCELENCIA")
