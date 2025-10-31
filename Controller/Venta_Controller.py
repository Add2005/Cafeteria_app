from Services.Venta_Service import VentaService
from Model.venta_Model import VentaModel
from Entities.detalle_venta import detalle_venta
from Entities.venta import Venta

class VentaController:
    
    def __init__(self):
        self.service = VentaService()
        self.model = VentaModel()
    
    def AgregarVenta(self, TotalVenta,FechaHora,IdCliente,IdEmpleado, lista_detalles: list[detalle_venta]):
        v = Venta(TotalVenta,FechaHora,IdCliente,IdEmpleado)
        self.service.AgregarVentaCompleta(v, lista_detalles)

    def HistorialVenta(self):
        return self.model.HistorialVentas()
    
    def Historial_Fecha_ASC(self):
        return self.model.Historial_Fecha_ASC()
    
    def Historial_Fecha_DESC(self):
        return self.model.Historial_Fecha_DESC()
    
    def Historial_Total_ASC(self):
        return self.model.Historial_Total_ASC()
    
    def Historial_Total_DESC(self):
        return self.model.Historial_Total_DESC()
    