# 7. Sistema de facturación electrónica
"""
Desarrolla una clase para generar facturas electrónicas. Requisitos:

· Clase Factura con atributos: numero, cliente, fecha, monto_total.

· Métodos:

o agregar_item(descripcion, cantidad, precio_unitario): Añade un producto o servicio a la factura y actualiza el monto total.

o mostrar_detalles(): Imprime los detalles de la factura.

o aplicar_descuento(porcentaje): Aplica un descuento al monto total.
"""

class Factura:

  # Clase Factura electronica

    def __init__(self, numero, cliente, fecha):
        self.numero = numero
        self.cliente = cliente
        self.fecha = fecha
        self.monto_total = 0
        self.items = []

    def agregar_item(self, descripcion, cantidad, precio_unitario):
        subtotal = cantidad * precio_unitario
        self.items.append((descripcion, cantidad, precio_unitario, subtotal))
        self.monto_total += subtotal

    def mostrar_detalles(self):
        print(f"Factura {self.numero} para {self.cliente} - Fecha: {self.fecha}")
        for item in self.items:
            print(f"{item[0]}: {item[1]} x {item[2]:.2f} = {item[3]:.2f}")
        print(f"Monto total: {self.monto_total:.2f}")

# Programa principal
factura1 = Factura(1, "Cliente A", "2024-11-18")
factura1.agregar_item("Manzanas", 5, 1000)
factura1.agregar_item("Peras", 3, 1200)
factura1.mostrar_detalles()
