# 4. Sistema de reservas en un hotel

"""Crea un sistema para manejar reservas en un hotel. Requisitos:

· Clase Habitacion con atributos: numero, tipo, precio, disponible.

· Métodos:

o reservar(): Marca la habitación como no disponible.

o liberar(): Marca la habitación como disponible.

o mostrar_informacion(): Imprime todos los detalles de la habitación."""


class Habitacion:

    # Clase Habitacion

    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True


    def reservar(self):
        self.disponible = False


    def liberar(self):
        self.disponible = True


    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        print(f"Habitación {self.numero}: Tipo: {self.tipo}, Precio: {self.precio:.2f}, Estado: {estado}")



habitacion1 = Habitacion(101, "Doble", 200000)
habitacion1.mostrar_informacion()
habitacion1.reservar()
habitacion1.mostrar_informacion()


