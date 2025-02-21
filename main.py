from models.Cliente import Cliente
from models.Auto import Auto
from models.Moto import Moto
from services.ParkingService import ParkingService
from services.ReporteEstacionamiento import ReporteEstacionamiento
from services.CobroEstacionamiento import CobroEstacionamiento
class ControlEstacionamiento:
    def __init__(self, capacidad, tarifa_auto, tarifa_moto):
        self.parking = ParkingService(capacidad)
        self.reporte_service = ReporteEstacionamiento()
        self.cobro_service = CobroEstacionamiento(tarifa_auto, tarifa_moto)

    def estacionar(self, vehiculo):
        self.parking.estacionar_vehiculo(vehiculo)

    def retirar(self, placa, horas_estacionado):
        self.parking.retirar_vehiculo(placa)
        vehiculo = self.parking.buscar_vehiculo(placa)
        if vehiculo:
            self.cobro_service.calcular_cobro(vehiculo, horas_estacionado)

    def generar_reporte(self):
        reporte = self.reporte_service.generar_reporte(self.parking)
        self.reporte_service.imprimir_reporte(reporte)
if __name__ == "__main__":
    # 1. Crear el control de estacionamiento con tarifas diferenciadas
    control = ControlEstacionamiento(capacidad=5, tarifa_auto=10, tarifa_moto=5)

    cli = Cliente(1, "franz", "caballero", "gmail")
    # 2. Crear vehículos (auto y moto)
    auto1 = Auto("ABC-123", "Rojo", "Toyota", "Corolla", 4)
    moto1 = Moto("XYZ-456", "Azul", "Yamaha", "MT-07", "Deportiva")

    cli.agregar_vehiculo(moto1)
    # 3. Estacionar vehículos
    control.estacionar(auto1)
    control.estacionar(moto1)

    # 4. Generar reporte
    control.generar_reporte()

    # 5. Retirar un vehículo y calcular cobro
    control.retirar("ABC-123", horas_estacionado=3)

    # 6. Generar reporte después de retirar un vehículo
    control.generar_reporte()
