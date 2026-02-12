#Prroblema 19: Promedio y datos del alumno
print("Programa que calcula el promedio de 5 calificaciones del alumno.")
nombre = input("Inserte su nombre completo: ")
boleta = int(input("Ingrese su número de boleta: "))
cal1 = float(input("Ingrese su primera calificación: "))
cal2 = float(input("Ingrese su segunda calificación: "))
cal3 = float(input("Ingrese su tercera calificación: "))
cal4 = float(input("Ingrese su cuarta calificación: "))
cal5 = float(input("Ingrese su quinta calificación: "))
prom = (cal1 + cal2 + cal3 + cal4 + cal5)/5
print("El alumno(a)", nombre, "con la boleta No.", boleta, "tiene el promedio de: ", prom)
