#---------------------------------------------------------------
#         Problema 55: Lista de números o de nombres
#---------------------------------------------------------------
import sys
print("Programa que genera cierto tipo de lista segun desee el usuario.")
lista = []
tipo = int(input("Tipos de lista:"
                 "\n1) Lista numérica."
                 "\n2) Lista textual."
                 "\n: "))
if tipo == 1:
    while True:
        r = int(input("Menú:"
                      "\n1) Agregar valores a la lista."
                      "\n2) Eliminar valores."
                      "\n3) Ordenar la lista directamente."
                      "\n4) Generar la lista ordenada."
                      "\n5) Mostrar el índice de un dato específico."
                      "\n6) Calcular el valor máximo, mínimo, suma y promedio."
                      "\n7) Finalizar el programa."
                      "\n: "))
        if r == 1:
            cant = int(input("Ingrese el número de datos por agregar: "))
            for i in range(cant):
                num = float(input("Ingrese un número: "))
                lista.append(num)
            print(lista)
        elif r == 2:
            if len(lista) == 0:
                print("Lista vacía.")
            else:
                forma = int(input("\n1) Eliminar por índice."
                                  "\n2) Eliminar por valor."
                                  "\n: "))
                if forma == 1:
                    posicion = int(input("Ingrese el número del índice: "))
                    if posicion >= 0 and posicion < len(lista):
                        n = posicion - 1
                        lista.pop(n)
                        print("Dato eliminado")
                elif forma == 2:
                    valor = float(input("Ingrese el valor a eliminar: "))
                    if valor in lista:
                        lista.remove(valor)
                        print("Dato eliminado")
                else:
                    print("El dato no existe")
            print(lista)
        elif r == 3:
            lista.sort()
            print(lista)
        elif r == 4:
            print(sorted(lista))
        elif r == 5:
            valor = float(input("Ingrese el valor a buscar: "))
            if valor in lista:
                pos = lista.index(valor)
                print("La posición de", valor, "es:", pos)
            else:
                print("No existe.")
        elif r == 6:
            if len(lista) > 0:
                print("Máximo:", max(lista),
                      "\nMínimo:", min(lista),
                      "\nSuma:", sum(lista),
                      "\nPromedio:", sum(lista)/len(lista))
            else:
                print("Lista vacía.")
        elif r == 7:
            print("Programa terminado.")
            sys.exit()
        else:
            print("Opción inválida.")
            
elif tipo == 2:
    while True:
        r = int(input("Menú:"
                      "\n1) Agregar valores a la lista."
                      "\n2) Eliminar valores."
                      "\n3) Ordenar la lista directamente."
                      "\n4) Generar la lista ordenada."
                      "\n5) Mostrar el índice de un dato específico."
                      "\n6) Finalizar el programa."
                      "\n: "))
        if r == 1:
            cant = int(input("Ingrese el número de datos por agregar: "))
            for i in range(cant):
                texto = input("Ingrese un texto: ")
                lista.append(texto)
            print(lista)
        elif r == 2:
            if len(lista) == 0:
                print("Lista vacía.")
            else:
                forma = int(input("\n1) Eliminar por índice."
                                  "\n2) Eliminar por valor."
                                  "\n: "))
                if forma == 1:
                    posicion = int(input("Ingrese el número de la posición: "))
                    if posicion >= 0 and posicion < len(lista):
                        n = posicion - 1
                        lista.pop(n)
                        print("Dato eliminado")
                elif forma == 2:
                    valor = input("Ingrese el valor a eliminar: ")
                    if valor in lista:
                        lista.remove(valor)
                        print("Dato eliminado")
                else:
                    print("El dato no existe")
             print(lista)
        elif r == 3:
            lista.sort()
            print(lista)
        elif r == 4:
            print(sorted(lista))
        elif r == 5:
            valor = input("Ingrese el valor a buscar: ")
            if valor in lista:
                pos = lista.index(valor)
                print("La posición de", valor, "es:", pos)
            else:
                print("No existe.")
        elif r == 6:
            print("Programa terminado.")
            sys.exit()
        else:
            print("Opción inválida.")
