#Problema 25: Ecuación de la recta.
print("Programa que calcula la pendiente de la recta en la ec. pendinete-int (y = mx+b)")
x1 = float(input("Ingrese la abscisa del primer punto: "))
y1 = float(input("Ingrese la ordenada del primer punto: "))
x2 = float(input("Ingrese la abscisa del segundo punto: "))
y2 = float(input("Ingrese la ordenada del segundo punto: "))
m = (y2 - y1)/(x2 - x1)
b = y1 - m*x1
print("La ecuación pendinete-int. de los puntos A(", x1,",", y1, ") y B(", x2,",", y2, "), es y =",m,"x + (", b, ")")
