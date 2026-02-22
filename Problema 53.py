#-------------------------------------------------------
#         Problema 53: Lista ordenada
#-------------------------------------------------------
print("Programa que ingresa la cantidad de datos que desee el usuario y los enlista.")
lista = []
r = int(input("Ingrese 1 si es una lista númerica o 2 si es una lista con nombres: "))
if r == 1:
    while True:
        res = int(input("¿Desea ingresar un dato?"
                        "\nIngrese 1 para continuar o cualquier otro número para salir: "))
        if res == 1:
            num = float(input("Ingrese un número: "))
            lista.append(num)
        else:
            print("Ha terminado de ingresar los datos de la lista.")
            break
elif r == 2:
    while True:
        res = int(input("¿Desea ingresar un dato?"
                        "\nIngrese 1 para continuar o cualquier otro número para salir: "))
        if res == 1:
            nom = (input("Ingrese un nombre: "))
            lista.append(nom)
        else:
            print("Ha terminado de ingresar los datos de la lista.")
            break
lista.sort()
print("\nLa lista ya ordenada es: ")
print("\n", lista)


