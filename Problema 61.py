#--------------------------------------------
#      Problema 61: Función promedio
#--------------------------------------------

print("Programa que crea una función que calcula el perímetro de un rectángulo.")

   #Se define la función.
def perimetro():
   altura = float(input("Ingrese la medida de la altura: "))
   base = float(input("Ingrese la medida de la base: "))
   resultado = ( 2*base ) + ( 2*altura )
   return resultado

   #Muestra del resultado.
print("El perímetro del rectángulo es: ", perimetro())
