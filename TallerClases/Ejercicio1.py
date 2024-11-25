# 1. Sistema de gestión de productos

"""Crea un sistema para gestionar productos en una tienda. Requisitos:

· Clase Producto con atributos: nombre, precio, cantidad.

· Métodos:

o actualizar_precio(): Cambia el precio del producto.

o ajustar_inventario(): Incrementa o disminuye la cantidad disponible.

o mostrar_informacion(): Muestra los detalles del producto."""

class Producto:

   # Clase que representa  producto

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio


    def ajustar_inventario(self, cambio_cantidad):
        self.cantidad += cambio_cantidad


    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio:.2f}, Cantidad: {self.cantidad}")


producto1 = Producto("Mango", 1000, 50)
producto2 = Producto("Pera", 800, 30)
producto3 = Producto("Naranja", 1200, 20)

producto1.actualizar_precio(1100)
producto2.ajustar_inventario(10)
producto3.mostrar_informacion()
