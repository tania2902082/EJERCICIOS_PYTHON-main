class ListaPersonalizada:
    def __init__(self):
        self.lista = []

    def agregar_una_vez(self, el):
        try:
            if el in self.lista:
                raise ValueError(f"Error: Imposible añadir elementos duplicados => {el}.")
            self.lista.append(el)
            print(f"Elemento '{el}' agregado correctamente a la lista.")
        except ValueError as e:
            print(e)
        finally:
            print("Gracias por usar este programa")

# Ejemplo de uso
if __name__ == "__main__":
    mi_lista = ListaPersonalizada()
    mi_lista.agregar_una_vez(3)
    mi_lista.agregar_una_vez(5)
    mi_lista.agregar_una_vez(3)  # Intenta añadir un elemento duplicado