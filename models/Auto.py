from models.Vehiculo import Vehiculo
from interface.TipoVehiculoInteface import TipoVehiculoInteface
class Auto(Vehiculo,TipoVehiculoInteface):
    def __init__(self, placa, color, marca, modelo, puertas):
        super().__init__(placa, color, marca, modelo)
        self.puertas = puertas
    def tipo(self):
        return "Auto"