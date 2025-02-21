
class ParkingService:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.vehiculos = []

    def estacionar_vehiculo(self, vehiculo):
        if len(self.vehiculos) < self.capacidad:
            print(len(self.vehiculos)+1,"--",self.capacidad)
            self.vehiculos.append(vehiculo)
            print(f"Vehículo con placa {vehiculo.placa} estacionado.")
        else:
            print("No hay espacio disponible para estacionar más vehículos.")

    def retirar_vehiculo(self, placa):
        vehiculo = self.buscar_vehiculo(placa)
        if vehiculo:
            self.vehiculos.remove(vehiculo)
            print(f"Vehículo con placa {placa} retirado.")
        else:
            print("Vehículo no encontrado en el parking.")
    
    def buscar_vehiculo(self, placa):
        for vehiculo in self.vehiculos:
            if vehiculo.placa == placa:
                return vehiculo
        return None
