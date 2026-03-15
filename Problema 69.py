#------------------------------------------------------------
#      Problema 69: Funciones para números primos
#------------------------------------------------------------

print("Programa que utiliza una función para verificar si la entrada es válida.")

  #Se crea la función.
def validacion(correo):
    if "@" in correo:
        return True
    else:
        return False

  #Se le pide al usuario una cadena de caracteres.
correo = input("Ingrese su correo: ")
if validacion(correo):
    print("Dirección válida")
else:
    print("Entrada inválida, falta '@'")
