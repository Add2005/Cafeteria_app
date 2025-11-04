from Model.reportes_model import reportesModel

class ReporteController:
    
    def __init__(self):
        self.model = reportesModel()
        
    def ObtenerVentasMensuales(self):
        return self.model.obtener_reportes_mensuales()
    
    def ObtenerProductosMasVendidos(self):
        return self.model.obtener_productos_mas_vendidos()
        


