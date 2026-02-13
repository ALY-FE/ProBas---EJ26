#-------------------------------------------------------
#      Problema 41: Confirmación de contraseña
#-------------------------------------------------------
print("Programa que confirma la contraseña ingresada.")
contra = input("Ingrese su contraseña: ")
Int2 = input("Ingrese nuevamente su contraseña: ")
while contra != Int2:
    Int2 = input("Contraseña incorrecta, intentelo de nuevo: ")
print("Las contraseñas coinciden.")
    
