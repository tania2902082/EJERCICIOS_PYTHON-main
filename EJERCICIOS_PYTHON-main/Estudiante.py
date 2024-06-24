#Ejercicio 1
class Estudiante:
    # Constructor que inicializa los atributos nombre, nota1 y nota2
    __init__ = lambda self, nombre, nota1, nota2: setattr(self, 'nombre', nombre) or setattr(self, 'nota1', nota1) or setattr(self, 'nota2', nota2)
    
    # Método para obtener la nota promedio
    obtener_nota_promedio = lambda self: (self.nota1 + self.nota2) / 2
    
    # Método para mostrar la información del estudiante
    mostrar_informacion = lambda self: print(f"Información del estudiante:\nNombre: {self.nombre}\nNota 1: {self.nota1}\nNota 2: {self.nota2}\nNota promedio: {self.obtener_nota_promedio():.2f}")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de Estudiante
    estudiante1 = Estudiante("Juan Pérez", 85, 92)
    
    # Mostrar la información del estudiante
    estudiante1.mostrar_informacion()



#Ejercicio 2
class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.__nombre = nombre
        self.__nota1 = self.__validar_nota(nota1)
        self.__nota2 = self.__validar_nota(nota2)
    
    def __validar_nota(self, nota):
        if nota < 0 or nota > 5:
            raise ValueError("La nota debe estar entre 0 y 5")
        return nota
    
    def obtener_nota_promedio(self):
        return (self.__nota1 + self.__nota2) / 2
    
    def mostrar_informacion(self):
        promedio = self.obtener_nota_promedio()
        print(f"Información del estudiante:")
        print(f"Nombre: {self.__nombre}")
        print(f"Nota 1: {self.__nota1}")
        print(f"Nota 2: {self.__nota2}")
        print(f"Nota promedio: {promedio:.2f}")
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nota1(self, nota1):
        self.__nota1 = self.__validar_nota(nota1)
    
    def get_nota1(self):
        return self.__nota1
    
    def set_nota2(self, nota2):
        self.__nota2 = self.__validar_nota(nota2)
    
    def get_nota2(self):
        return self.__nota2

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de Estudiante
    estudiante1 = Estudiante("Juan Pérez", 3, 4)
    
    # Intentar asignar una nota fuera del rango permitido
    try:
        estudiante1.set_nota2(6)
    except ValueError as e:
        print(e)
    
    # Mostrar la información del estudiante
    estudiante1.mostrar_informacion()



#Ejercicio 3
class Estudiante: #Estudiante: Define una clase con atributos privados (__nombre, __nota1, __nota2) utilizando el doble guion bajo (__) para encapsulamiento.
    def __init__(self, nombre, nota1, nota2):
        #__init__: Constructor que inicializa los atributos nombre, nota1 y nota2. Se asegura de que las notas estén dentro del rango permitido utilizando el método __validar_nota.
        self.__nombre = nombre
        self.__nota1 = self.__validar_nota(nota1)
        self.__nota2 = self.__validar_nota(nota2)
    
    def __validar_nota(self, nota):
        if nota < 0 or nota > 5:
            raise ValueError("La nota debe estar entre 0 y 5")
        return nota
    
    def obtener_nota_promedio(self):
        return (self.__nota1 + self.__nota2) / 2
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Nota promedio: {self.obtener_nota_promedio():.2f}"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de Estudiante
    estudiante1 = Estudiante("Juan Pérez", 3, 4)
    
    # Imprimir el objeto estudiante1
    print(estudiante1)


#Ejercicio 4
class Estudiante:
    # Atributos de clase
    institucion = "Instituto XYZ"
    total_estudiantes = 0
    
    def __init__(self, nombre, nota1, nota2):
        self.__nombre = nombre
        self.__nota1 = self.__validar_nota(nota1)
        self.__nota2 = self.__validar_nota(nota2)
        Estudiante.total_estudiantes += 1
    
    def __validar_nota(self, nota):
        if nota < 0 or nota > 5:
            raise ValueError("La nota debe estar entre 0 y 5")
        return nota
    
    def obtener_nota_promedio(self):
        return (self.__nota1 + self.__nota2) / 2
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Nota promedio: {self.obtener_nota_promedio():.2f}, Institución: {self.institucion}"
    
    def cambiar_institucion(self, nueva_institucion):
        Estudiante.institucion = nueva_institucion
    
    @classmethod
    def obtener_total_estudiantes(cls):
        return cls.total_estudiantes

# Ejemplo de uso
if __name__ == "__main__":
    # Crear algunos estudiantes
    estudiante1 = Estudiante("Juan Pérez", 3, 4)
    estudiante2 = Estudiante("María López", 4, 5)
    
    # Mostrar información de los estudiantes
    print(estudiante1)
    print(estudiante2)
    
    # Cambiar la institución para todos los estudiantes
    estudiante1.cambiar_institucion("Colegio ABC")
    
    # Mostrar nuevamente la información de los estudiantes
    print(estudiante1)
    print(estudiante2)
    
    # Obtener el total de estudiantes
    print(f"Total estudiantes: {Estudiante.obtener_total_estudiantes()}")
