#---------------------------------------------------
#      Problema 66: Función reprobados
#---------------------------------------------------

print("Programa que de una lista, genera una función que regresa la lista de los reprobados.")

   #Se crea la lista de aprobados y la de reprobados.
lista_reprobados = []

   #Se crea una función para llenar las listas.
def llenado_lista():
    while True:
        nombre = input("Ingrese el nombre completo del alumno o 'fin' para terminar: ")
        if nombre == "fin":
            break
        calif = float(input("Ingrese la calificación del alumno: "))
        if calif < 70:
            lista_reprobados.append(nombre)
    return lista_reprobados

   #Se llama a función llenado_listas.
reprobados = llenado_lista()

   #Se muestra la lista de los reprobados.
print("Los reprobados son: ", reprobados)
