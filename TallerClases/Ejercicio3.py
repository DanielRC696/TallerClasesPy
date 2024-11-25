# 3. Sistema de Vehículos

"""Diseña una clase que represente vehículos en general. Requisitos:

· Clase Vehiculo con atributos: marca, modelo, año, kilometraje.

· Métodos:

o conducir(): Incrementa el kilometraje.

o mostrar_detalles(): Imprime todos los detalles del vehículo.

o es_vehiculo_antiguo(): Devuelve True si el vehículo tiene más de 20 años."""

class Vehiculo:

    # Clase Vehiculo

    def __init__(self, marca, modelo, año, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def conducir(self, km):
        self.kilometraje += km


    def mostrar_detalles(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje}")


    def es_vehiculo_antiguo(self):
        return (2024 - self.año) > 20


vehiculo1 = Vehiculo("Toyota", "Corolla", 2000, 120000)
vehiculo1.conducir(150)
vehiculo1.mostrar_detalles()
print("¿Es antiguo?", vehiculo1.es_vehiculo_antiguo())
