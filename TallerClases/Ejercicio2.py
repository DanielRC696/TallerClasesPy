# 2. Registro de Estudiantes

"""Desarrolla un sistema para gestionar estudiantes en una escuela. Requisitos:

· Clase Estudiante con atributos: nombre, edad, grado, materias.

· Métodos:

o inscribir_materia(): Agrega una materia a la lista de materias del estudiante.

o mostrar_materias(): Muestra las materias inscritas.

o actualizar_grado(): Cambia el grado del estudiante."""

class Estudiante:

    # Clase estudiante

    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.materias = []

    def inscribir_materia(self, materia):
        self.materias.append(materia)


    def mostrar_materias(self):
        print(f"{self.nombre} está inscrito en: {', '.join(self.materias)}")


    def actualizar_grado(self, nuevo_grado):
        self.grado = nuevo_grado



estudiante1 = Estudiante("Ana", 15, "10°")
estudiante1.inscribir_materia("Matemáticas")
estudiante1.inscribir_materia("Historia")
estudiante1.mostrar_materias()
estudiante1.actualizar_grado("11°")
