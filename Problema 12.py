# Problema 12: Saludo con año de nacimiento.
print("Programa que te saluda según tu nombre y posible año de nacimiento")
nombre = input("Por favor, inserte su nombre: ")
edad = int(input("Por favor, inserte su edad: "))
año = 2026 - edad       #Aquí se podría pedir al usuario que ingrese el año actual para que el dato sea más preciso.
print("Hola ", nombre, "de ", año)
