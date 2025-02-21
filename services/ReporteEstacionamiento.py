
class ReporteEstacionamiento:
    def generar_reporte(self, parking):
        """
        Genera un reporte sobre los vehículos estacionados en el parking.
        """
        reporte = f"Reporte de Estacionamiento (Capacidad total: {parking.capacidad}):\n"
        for vehiculo in parking.vehiculos:
            reporte += f"Placa: {vehiculo.placa}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Color: {vehiculo.color}\n"
        return reporte

    def imprimir_reporte(self, reporte):
        """
        Imprime el reporte generado.
        """
        print("==== Reporte de Estacionamiento ====")
        print(reporte)
        print("===============================")
