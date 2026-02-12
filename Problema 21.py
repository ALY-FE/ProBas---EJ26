#Problema 21: Banquete por evento.
print("Programa que calcula y muestra la cantidad total de agua, carne y salsa necesarias para un evento.")
evento = input("Ingrese el nombre del evento: ")
fecha = input("Ingrese la fecha del evento: ")
cant = int(input("Ingrese la cantidad de invitados: "))
agua = cant*1.5
carne = cant*350
salsa = agua*0.25
print("Para el evento", evento, "de", fecha, "se ocupan:", agua, "litros de agua,", carne, "gramos de carne y", salsa, "litros de salsa.")
