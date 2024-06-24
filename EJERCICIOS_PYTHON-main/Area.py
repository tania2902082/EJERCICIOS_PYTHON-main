#Área del cuadrado 
lado = float(input("Ingrese el valor del lado del cuadrado: "))
area_cuadrado = lado ** 2
print("El área del cuadrado es:", area_cuadrado)

#Área del rectángulo
base = float(input("Ingrese el valor de la base del rectángulo: "))
altura = float(input("Ingrese el valor de la altura del rectángulo: "))
area_rectangulo = base * altura
print(f"El área del rectángulo es: {area_rectangulo}")

#Área del triángulo
base = float(input("Ingrese el valor de la base del triángulo: "))
altura = float(input("Ingrese el valor de la altura del triángulo: "))
area_triangulo = base * altura
print("El área del rectángulo es: ", area_triangulo)

#Área del rombo
diagonal_mayor = float(input("Ingrese el valor de la diagonal mayor del rombo: "))
diagonal_menor = float(input("Ingrese el valor de la diagonal menor del rombo: "))
area_rombo = diagonal_mayor * diagonal_menor / 2
print("El área del rombo es: ", area_rombo)