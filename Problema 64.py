#---------------------------------------------------
#      Problema 64: Función EsMultiplo
#---------------------------------------------------

print("Programa que crea una función que determina si un número es múltiplo del otro.")

   #Se define la función EsMultiplo.
def EsMultiplo():
    num1 = int(input("Ingrese el número que quiere determinar si es múltiplo o no: "))
    num2 = int(input("Ingrese el número del que será múltiplo: "))
    residuo = num1 % num2
    if residuo == 0:
        print(num1, "SI es múltiplo de", num2)
    else:
        print(num1, "NO es múltiplo de", num2)

   #Se llama a la función EsMultiplo.
EsMultiplo()
    
