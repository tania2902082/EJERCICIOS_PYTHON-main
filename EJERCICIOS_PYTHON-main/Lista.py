Lista = [3, 5, 6, 8]

while True:
    try:
        pos = int(input("Ingrese la posición del elemento que desea obtener: "))
        print(f"El valor en la posición {pos} es {Lista[pos]}")
        break  # Salimos del bucle si todo fue correcto
    except ValueError:
        print("Error: La posición ingresada no es un número entero válido.")
    except IndexError:
        print(f"Error: La posición {pos} está fuera de rango para la lista.")
    except Exception as e:
        print(f"Error inesperado: {e}")

