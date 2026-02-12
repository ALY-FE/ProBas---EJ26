import math
#Problema 18: Operaciones matemáticas
print("Programa que realiza la suma, resta, división, multiplicación, potenciación, raíz cuadrada del primer y módulo de dos números.")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print("El resultado de su suma es: ", num1+num2)
print("El resultado de su resta es: ", num1-num2)
print("El resultado de su división es: ", num1/num2)
print("El resultado de su multiplicación es: ", num1*num2)
print("El resultado de su potenciación (el primero elevado al segundo) es: ", num1**num2)
print("El resultado de la raíz cuadrada del primero es: ", math.sqrt(num1))
print("El residuo de su división es: ", num1%num2)
