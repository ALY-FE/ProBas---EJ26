#Problema 22: Calificación de examen.
print("Programa que calcula la calificación final en escala de 0 a 10.")
cant = int(input("Ingrese la cantidad total de preguntas: "))
corr = float(input("Ingrese la cantidad de respuestas correctas: "))
val = 10/cant
cal = corr*val
print("La calificación final es: ", cal)
