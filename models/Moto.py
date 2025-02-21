from models.Vehiculo import Vehiculo
from interface.TipoVehiculoInteface import TipoVehiculoInteface
class Moto(Vehiculo,TipoVehiculoInteface):
    def __init__(self, placa, color, marca, modelo, tipo_moto):
        super().__init__(placa, color, marca, modelo)
        self.tipo_moto = tipo_moto
    def tipo(self):
        return "Moto"