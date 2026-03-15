#---------------------------------------------------
#      Problema 67: Funciones para listas
#---------------------------------------------------

print("Programa que crea diversas funciones para listas.")

      #Se crea una lista vacía.
lista = []

      #Se definen las dunciones.
#Función 1: Llenado
def llenado_lista():
    while True:
        num = float(input("Ingrese un número para agregarlo a la lista ó 0 para terminar de enlistar: "))
        if num == 0:
            break
        lista.append(num)
    return lista

#Función 2: Creciente
def lista_creciente(lista):
    if len(lista) == 0:                   #Para checar que la lista original no este vacía.
        print("La lista está vacía, llenela primero.")
        opcion = 1
    return sorted(lista)

#Función 3: Decreciente
def lista_decreciente(lista):
    if len(lista) == 0:                   #Para checar que la lista original no este vacía.
        print("La lista está vacía, llenela primero.")
        opcion = 1
    return sorted(lista, reverse=True)

#Función 4: Eliminar por posición
def eliminar_posicion(lista):
    print("El elemento a eliminar será de la lista original")
    if len(lista) == 0:                   #Para checar que la lista original no este vacía.
        print("La lista está vacía, llenela primero.")
        opcion = 1
    posicion = int(input("Ingrese el número de posición del elemento: "))
    i = posicion - 1
    eliminado = lista.pop(i)
    return eliminado

#Función 5: Eliminar por valor
def eliminar_valor(lista):
    print("El elemento a eliminar será de la lista original")
    if len(lista) == 0:                   #Para checar que la lista original no este vacía.
        print("La lista está vacía, llenela primero.")
        opcion = 1
    valor = float(input("Ingrese el valor a eliminar: "))
    lista.remove(valor)
    return lista

#Función 6: Sacar promedio, máximo y mínimo
def numeros(lista):
    if len(lista) == 0:                   #Para checar que la lista original no este vacía.
        print("La lista está vacía, llenela primero.")
        opcion = 1
    promedio = sum(lista) / len(lista)
    mayor = max(lista)
    menor = min(lista)
    return promedio, mayor, menor


#Se crea el ciclo para que el usuario pueda realizar cada operación.
while True:
    opcion = int(input("Ingrese:"
                       "\n1) Llenar la lista original."
                       "\n2) Crear una lista ordenada crecientemente y la muestra."
                       "\n3) Crear una lista ordenada decrecientemente y la muestra."
                       "\n4) Eliminar de la lista un elemento por su posición y regresar el valor eliminado."
                       "\n5) Eliminar un elemento de la lista por su valor."
                       "\n6) Calcular promedio, máximo y mínimo de la lista."
                       "\nCualquier otro número para salir."))

      #Opción de llenado de la lista.
    if opcion == 1:
        llenado_lista()

      #Opción para ordenadar la lista crecientemente.
    elif opcion == 2:
        datos_crecientes = lista_creciente(lista)
        print("La lista ordenada de manera creciente es:", datos_crecientes)

      #Opción para ordenadar la lista decrecientemente.
    elif opcion == 3:
        datos_decrecientes = lista_decreciente(lista)
        print("La lista ordenada de manera decreciente es:", datos_decrecientes)

      #Opción para eliminar un elemento por su posición.
    elif opcion == 4:
        eliminado = eliminar_posicion(lista)
        print("El elemento eliminado fue: ", eliminado)

      #Opción para eliminar un elemento por su valor.
    elif opcion == 5:
        eliminar_valor(lista)
        print("La nueva lista es: ", lista)

      #Opción para sacar el promedio, el valor máximo y el valor mínimo.
    elif opcion == 6:
        promedio, mayor, menor = numeros(lista)
        print("El promedio es:", promedio)
        print("El número mayor es:", mayor)
        print("El número menor es:", menor)

      #Opcion para salir.
    else:
        print("Ha finalizado el programa.")
        break










        
















