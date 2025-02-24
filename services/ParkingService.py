
class ParkingService:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.vehiculos = []

    def estacionar_vehiculo(self, vehiculo):
        if len(self.vehiculos) < self.capacidad:
            print(len(self.vehiculos)+1,"--",self.capacidad)
            print("--[:",self.vehiculos)
            self.vehiculos.append(vehiculo)
            """print(f"otr--:{vehiculo.vehiculos[0].placa}")
            print(f"Vehículo con placa {vehiculo.vehiculos[0].placa} estacionado.")
            print(f"n-Auto estacionados:{self.vehiculos[0].vehiculos[0].placa}")
            for i in self.vehiculos:
                print(i.vehiculos[0].placa)"""
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
