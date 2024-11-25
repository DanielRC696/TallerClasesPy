# 5. Sistema de gestión de libros

"""Diseña un sistema para registrar y gestionar libros en una librería. Requisitos:

· Clase Libro con atributos: titulo, autor, genero, precio.

· Métodos:

o aplicar_descuento(): Reduce el precio en un porcentaje dado.

o mostrar_informacion(): Imprime los detalles del libro.

o es_mas_caro_que(otro_libro): Compara precios entre dos libros y devuelve el más caro."""

class Libro:

  # Clase libro

    def __init__(self, titulo, autor, genero, precio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        self.precio *= (1 - porcentaje / 100)


    def mostrar_informacion(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Precio: {self.precio:.2f}")



libro1 = Libro("Cuerpos", "nohemiy kasquet", "Sexualida"
                                             "", 50000)
libro1.aplicar_descuento(10)
libro1.mostrar_informacion()


