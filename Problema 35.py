#Problema 35: Orden descendente de tres umeros.
print("Programa que ordena de manera descendente tres numeros.")
num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro numero entero: "))
num3 = int(input("Ingrese un ultimo numero entero: "))
if num1 > num2 and num2 > num3:
    print("El orden descendente es: ", num1, num2, num3)
elif num2 > num1 and num1 > num3:
    print("El orden descendente es: ", num2, num1, num3)
elif num2 > num3 and num3 > num1:
    print("El orden descendente es: ", num2, num3, num1)
elif num1 > num3 and num3 > num2:
    print("El orden descendente es: ", num1, num3, num2)
elif num3 > num2 and num2 > num1:
    print("El orden descendente es: ", num3, num2, num1)
else:
    print("El orden descendente es: ", num3, num1, num2)
