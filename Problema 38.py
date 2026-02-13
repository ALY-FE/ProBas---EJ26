#-----------------------------------------------------------------------
#       Problema 38: Validación de un número entre 1 y 5
#-----------------------------------------------------------------------
print("Programa que solo valida del 1 al 5")
num = 0
while num < 1 or num > 5:
    num = float(input("Ingrese un numero del 1 al 5: "))
    if num < 1 or num > 5:
        print("Número inválido")
print("Número válido")
   
