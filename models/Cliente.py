
from .Persona import Persona
from interface.clienteInterface import clienteInterface


class Cliente(Persona, clienteInterface):
    def __init__(self, id, nombre, apellido,telefono, direccion):
        super().__init__(nombre, apellido)
        self.id = id
        self.telefono = telefono
        self.direccion = direccion
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(self.vehiculos)
        print(len(self.vehiculos))

    def remover_vehiculo(self, vehiculo):
        self.vehiculos.remove(vehiculo)

