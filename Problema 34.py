#Problema 34: Clasificacion por edad.
import sys
print("Programa que clasifica al usuario segun su edad.")
edad = int(input("Ingrese su edad: "))
if edad < 0 or edad > 120:
    print("Edad invalida.")
    sys.exit()
elif edad < 10:
    print("NIÑO")
elif edad <= 17:
    print("ADOLESCENTE")
elif edad <= 29:
    print("MAYOR DE EDAD")
    print("JOVEN")
elif edad <= 59:
    print("MAYOR DE EDAD")
    print("ADULTO")
else:
    print("MAYOR DE EDAD")
    print("ADULTO MAYOR")
