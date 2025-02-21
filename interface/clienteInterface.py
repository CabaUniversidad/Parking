from abc import ABC, abstractmethod
class clienteInterface(ABC):
    @abstractmethod
    def agregar_vehiculo(self,vehiculo):
        pass
    def remover_vehiculo(self,vehiculo):
        pass