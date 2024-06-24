# Funciones básicas de operaciones matemáticas sin usar def
suma = lambda a, b: a + b
resta = lambda a, b: a - b
multiplicacion = lambda a, b: a * b
division = lambda a, b: a / b if b != 0 else None  # Manejo de división por cero

# Importamos las expresiones lambda del módulo matematicas
from Matematicas import suma, resta, multiplicacion, division

# Variables de ejemplo
a = 4
b = 20

# Uso de las operaciones
print(f"Suma de {a} y {b} es: {suma(a, b)}")
print(f"Resta de {a} y {b} es: {resta(a, b)}")
print(f"Multiplicación de {a} y {b} es: {multiplicacion(a, b)}")

# Manejo de la división
resultado_division = division(a, b)
if resultado_division is not None:
    print(f"División de {a} y {b} es: {resultado_division}")
else:
    print("No se puede dividir entre cero")