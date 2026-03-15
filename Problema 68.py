#------------------------------------------------------------
#      Problema 68: Funciones para números primos
#------------------------------------------------------------

print("Programa que determina si un número es primo o no.")

  #Se crea la función para ello.
def primo(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

  #Se le pide al usario un número.
num = int(input("Ingrese un número: "))
if primo(num):
    print("El número", num, "ES primo.")
else:
    print("El número", num, "NO es primo.")
            
