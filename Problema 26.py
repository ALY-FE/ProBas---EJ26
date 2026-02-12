#Problema 26: Comparar dos numeros.
print("Programa que compara dos numeros enteros")
num1=int(input("Por favor ingrese el primer numero: "))
num2=int(input("Por favor ingrese el segundo numero: "))
if num1 > num2:
    print("El", num1, "es mayor.")
elif num1 < num2:
    print("El", num2, "es mayor.")
else:
    print("Es el mismo valor.")
