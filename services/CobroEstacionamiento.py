class CobroEstacionamiento:
    def __init__(self, tarifa_auto, tarifa_moto):
        self.tarifa_auto = tarifa_auto
        self.tarifa_moto = tarifa_moto

    def calcular_cobro(self, vehiculo, horas_estacionado):
        if vehiculo.tipo() == "Auto":
            costo = self.tarifa_auto * horas_estacionado
        elif vehiculo.tipo() == "Moto":
            costo = self.tarifa_moto * horas_estacionado
        
        print(f"Cobro por {vehiculo.tipo()} con placa {vehiculo.placa}: {costo} unidades monetarias.")
        return costo