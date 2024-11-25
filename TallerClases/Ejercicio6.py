# 6. Sistema de animales en un zoológico

"""
Crea un sistema para registrar animales en un zoológico. Requisitos:

· Clase Animal con atributos: nombre, especie, edad, habitat.

· Métodos:

o cumplir_años(): Incrementa la edad del animal en un año.

o cambiar_habitat(): Modifica el hábitat del animal.

o mostrar_detalles(): Imprime los detalles del animal.
"""

class Animal:

  # Clase animal

    def __init__(self, nombre, especie, edad, habitat):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.habitat = habitat

    def cumplir_años(self):
        self.edad += 1

    def cambiar_habitat(self, nuevo_habitat):
        self.habitat = nuevo_habitat

    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}, Hábitat: {self.habitat}")

# Programa principal
animal1 = Animal("Neron", "León", 5, "Sabana")
animal1.cumplir_años()
animal1.cambiar_habitat("Selva")
animal1.mostrar_detalles()
