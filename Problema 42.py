#----------------------------------------------------------
#        Problema 42:Confirmación de contraseña.
#----------------------------------------------------------
print("Programa que limita intentos de ingresar la contraseña.")
contra = input("Ingrese su contraseña: ")
Int2 = input("Ingrese su contraseña nuevamente: ")
c = 0
while contra != Int2 and c < 3:
    Int2 = input("Contraseña incorrecta, intentelo nuevamente: ")
    c = c + 1
if c >= 3:
    print("Cuenta cancelada")
else:
    print("Las contraseñas coinciden")
